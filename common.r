script_name <- function()
  strsplit(grep("--file=", commandArgs(FALSE), value=TRUE), "=")[[1]][2]

get_args <- function(...) {
  args <- commandArgs(TRUE)
  if (!length(args) || "-h" %in% args) {
    message(...)
    quit(status=1)
  }
  args
}

copr_call <- function(...) {
  copr.cmd <- getOption("copr.cmd")
  if (Sys.which(copr.cmd) == "")
    stop("command '", copr.cmd, "' not found", call.=FALSE)
  args <- paste(..., collapse=" ")
  out <- suppressWarnings(system2(copr.cmd, args, stdout=TRUE, stderr=TRUE))
  if (!is.null(attr(out, "status")))
    stop(paste(out, collapse="\n"), "\n", paste(copr.cmd, args), "' failed", call.=FALSE)
  out
}

copr_version <- function() {
  vstr <- strsplit(copr_call("--version"), " ")[[1]]
  package_version(vstr[length(vstr)])
}

check_copr <- function() {
  tryCatch(invisible(copr_call("whoami")), error=function(e)
    stop("file '~/.config/copr' not found or outdated", call.=FALSE))
}

list_pkgs <- function() {
  copr_call("list-package-names", getOption("copr.repo"))
}

watch_builds <- function(ids) {
  if (!getOption("copr.watch", TRUE)) return(FALSE)
  if (!length(ids)) return(logical(0))

  out <- try(copr_call("watch-build", paste(ids, collapse=" ")), silent=TRUE)
  if (class(out) == "try-error") out <- strsplit(out, "\n")[[1]]
  sapply(ids, function(i) {
    build <- paste0(".* Build ", i, ": ")
    status <- grep(paste0(build, "(succeeded|failed)"), out, value=TRUE)
    ifelse(sub(build, "", status) == "failed", TRUE, FALSE)
  })
}

delete_builds <- function(ids) {
  if (copr_version() >= "1.87")
    ids <- paste(ids, collapse=" ")
  for (id in ids)
    copr_call("delete-build", id)
}

build_spec <- function(spec, chroots=getOption("copr.chroots")) {
  chroots <- if (is.null(chroots)) "" else paste("-r", chroots, collapse=" ")
  pkg <- sub("\\.spec", "", basename(spec))
  out <- copr_call("build", "--nowait", getOption("copr.bflags"),
                   getOption("copr.repo"), spec, chroots)
  out <- grep("Created builds", out, value=TRUE)
  out <- as.numeric(strsplit(out, ": ")[[1]][2])
  message("  Build ", out, " for ", pkg, " created from SPEC")
  out
}

build_pkg <- function(pkg, chroots=getOption("copr.chroots")) {
  chroots <- if (is.null(chroots)) "" else paste("-r", chroots, collapse=" ")
  out <- copr_call("build-package", "--nowait", getOption("copr.bflags"),
                   getOption("copr.repo"), "--name", pkg, chroots)
  out <- grep("Created builds", out, value=TRUE)
  out <- as.numeric(strsplit(out, ": ")[[1]][2])
  message("  Build ", out, " for ", pkg, " created from repo")
  out
}

add_pkg_scm <- function(pkg) {
  out <- copr_call(
    "add-package-scm", getOption("copr.repo"), "--name", pkg,
    "--clone-url", getOption("copr.clone.url"),
    "--subdir", getOption("copr.subdir"), "--spec", paste0(pkg, ".spec"))
  message("  New package ", pkg, " added")
}

delete_pkg_scm <- function(pkg) {
  out <- copr_call("delete-package", getOption("copr.repo"), "--name", pkg)
  message("  Package ", pkg, " removed")
}

available_packages <- function(...) {
  cran <- available.packages()
  cran[!duplicated(cran[, "Package"]), ]
}

with_deps <- function(pkgs, cran=available_packages(), reverse=FALSE) {
  if (!length(pkgs)) return(list())

  base <- rownames(installed.packages(priority="high"))
  excl <- unlist(sapply(dir(pattern="excl-.*\\.txt"), readLines))
  if (!is.null(excl))
    excl <- sapply(strsplit(excl, " "), head, 1)
  pkgs <- setdiff(pkgs, base)

  if (!reverse) {
    avail <- pkgs %in% cran[,"Package"]
    if (any(!avail))
      warning("ignoring ", length(pkgs[!avail]), " packages ",
              "(reason: not on CRAN): ",
              paste(pkgs[!avail], collapse=", "), call.=FALSE)
    pkgs <- pkgs[avail]

    avail <- !pkgs %in% excl
    if (any(!avail))
      warning("ignoring ", length(pkgs[!avail]), " packages ",
              "(reason: exclusions): ",
              paste(pkgs[!avail], collapse=", "), call.=FALSE)
    pkgs <- pkgs[avail]
  }

  deps <- tools::package_dependencies(pkgs, db=cran, recursive=TRUE, reverse=reverse)

  avail <- sapply(deps, function(i) all(setdiff(i, base) %in% cran[,"Package"]))
  if (any(!avail))
    warning("ignoring ", length(names(avail)[!avail]), " packages ",
            "(reason: dependencies not on CRAN): ",
            paste(names(avail)[!avail], collapse=", "), call.=FALSE)
  deps <- deps[avail]

  if (!reverse) {
    avail <- sapply(deps, function(i) all(!setdiff(i, base) %in% excl))
    if (any(!avail))
      warning("ignoring ", length(names(avail)[!avail]), " packages ",
              "(reason: dependencies are exclusions): ",
              paste(names(avail)[!avail], collapse=", "), call.=FALSE)
    deps <- deps[avail]
  }

  setdiff(unique(c(names(deps), unlist(deps))), base)
}

get_build_list <- function(pkgs, cran=available_packages()) {
  base <- rownames(installed.packages(priority="high"))
  pkgs <- lapply(tools::package_dependencies(pkgs, db=cran), setdiff, base)
  pkgs <- lapply(Filter(Negate(is.null), pkgs), intersect, names(pkgs))

  build <- list()
  while (length(pkgs)) {
    x <- names(Filter(function(i) all(i %in% unlist(build)), pkgs))
    build[[length(build)+1]] <- x
    pkgs <- pkgs[!names(pkgs) %in% x]
  }

  build
}

get_copr_list <- function(subset) {
  pkgs <- grep(getOption("copr.prefix"), list_pkgs(), value=TRUE)
  pkgs <- sub(getOption("copr.prefix"), "", pkgs)
  if (missing(subset) || "--all" %in% subset)
    return(pkgs)
  avail <- subset %in% pkgs
  if (any(!avail))
    warning("ignoring ", paste(subset[!avail], collapse=", "), call.=FALSE)
  intersect(pkgs, subset)
}

get_spec_version <- function(spec) {
  if (!file.exists(spec)) return("0.0")
  pattern <- "^\\%global packver[[:space:]]*"
  sver <- grep(pattern, readLines(spec), value=TRUE)
  sub(pattern, "", sver)
}

need_update <- function(pkgs, cran=available_packages()) {
  indb <- cran[cran[,"Package"] %in% pkgs, "Version"]
  if (length(indb) != length(pkgs))
    stop("cannot update packages removed from CRAN")
  nver <- package_version(indb[rank(pkgs)])

  spec <- paste0(getOption("copr.subdir"), "/", getOption("copr.prefix"), pkgs, ".spec")
  over <- package_version(sapply(spec, get_spec_version))

  over < nver
}

.fix_version <- function(deps, cran=available_packages()) {
  # fix 2-component versions declared as 3-component
  two_comp <- grep("^[0-9]+.[0-9]+$", cran[,"Version"], value=TRUE)
  two_comp <- deps$pkg %in% names(two_comp)
  deps[two_comp,]$ver <- sub("([0-9]+.[0-9]+).[0-9]+", "\\1", deps[two_comp,]$ver)

  deps
}

.r_deps <- function(desc, cran=available_packages()) {
  keys <- c("Depends", "Imports", "LinkingTo")
  for (i in keys) if (is.null(desc[[i]]))
    desc[[i]] <- ""

  deps <- gsub("\n", " ", as.matrix(desc)[,keys])
  deps <- gsub("compiler[0-9\\(\\)[:space:]>=.]*,", "", deps)
  deps <- sub("[[:space:]]*,[[:space:]]*$", "", deps)
  deps <- strsplit(deps, "[[:space:]]*,[[:space:]]*")
  deps <- do.call(rbind, lapply(deps, function(i) {
    pkg <- trimws(sub("[[:space:]]*\\(.*\\)$", "", i))
    ver <- mapply(function(x, y) sub(x, "", y), pkg, i)
    ver <- sub("\\((.*)\\)", "\\1", ver)
    ver <- gsub("-", ".", ver)
    data.frame(pkg=pkg, ver=ver, stringsAsFactors=FALSE)
  }))
  if (nrow(deps)) deps$ver <- paste0(" ", trimws(deps$ver))
  deps <- deps[order(deps$ver, decreasing=TRUE),]
  dups <- deps$pkg[duplicated(deps$pkg)]
  for (dup in dups)
    deps$ver[deps$pkg==dup] <- deps$ver[deps$pkg==dup][1]

  .fix_version(deps, cran)
}

.sys_deps <- function(desc) {
  deps <- read.csv("sysreqs.csv", na.strings="", stringsAsFactors=FALSE)
  deps <- deps[deps$pkg == desc$Package,]
  if (!nrow(deps))
    return(character(0))

  x <- character(0)
  if (!is.na(deps$build))
    x <- c(x, paste0("BuildRequires:    ", strsplit(deps$build, ", ")[[1]]))
  if (!is.na(deps$run))
    x <- c(x, paste0("Requires:         ", strsplit(deps$run, ", ")[[1]]))
  x
}

pkg_deps <- function(desc, cran=available_packages()) {
  x <- .sys_deps(desc)
  deps <- .r_deps(desc, cran)

  rdep <- deps$pkg == "R"
  rver <- deps[rdep, "ver"]
  deps <- deps[!rdep,]
  inbase <- deps$pkg %in% rownames(installed.packages(priority="high"))
  deps$pkg[inbase] <- paste0("R-", deps$pkg[inbase])
  deps$pkg[!inbase] <- paste0(getOption("copr.prefix"), deps$pkg[!inbase])

  x <- c(x, paste0("BuildRequires:    R-devel", rver))
  x <- c(x, paste0("Requires:         R-core", rver))

  if (!isTRUE(cran[cran[,"Package"] == desc$Package, "NeedsCompilation"] == "yes"))
    x <- c(x, "BuildArch:        noarch")

  if (nrow(deps))
    x <- c(x, paste0("BuildRequires:    ", deps$pkg, deps$ver))
  deps <- deps[!grepl("LinkingTo", rownames(deps)),]
  if (nrow(deps))
    x <- c(x, paste0("Requires:         ", deps$pkg, deps$ver))

  x[!duplicated(x)]
}

pkg_exceptions <- function(tpl, pkg, path) {
  # top
  tpl <- c(switch(
    pkg,
    BANOVA=,beam=,Boom=,FastRWeb=,mapdata=,pbdRPC=,pbdPROF=,qtpaint=,RxODE=,
    tth=,wingui=,mixl=,StanHeaders="%global debug_package %{nil}",
    tcltk2="%undefine __brp_mangle_shebangs"), tpl)

  # source
  src <- grep("Source0", tpl)
  tpl[src] <- paste0(tpl[src], "\n", switch(
    pkg,
    h2o = paste0(
      "Source1:          https://s3.amazonaws.com/h2o-release/h2o/",
      readLines(file.path(path, "inst/branch.txt")), "/",
      readLines(file.path(path, "inst/buildnum.txt")), "/Rjar/h2o.jar"),
    rscala = paste0(
      "Source1:          https://downloads.lightbend.com/scala/2.12.8/scala-2.12.8.tgz\n",
      "Source2:          https://github.com/sbt/sbt/releases/download/v1.2.8/sbt-1.2.8.tgz")
  ))

  # setup
  setup <- grep("%setup", tpl)
  tpl[setup] <- paste0(tpl[setup], switch(
    pkg,
    rscala = " -a 1 -a 2"
  ))
  tpl[setup] <- paste0(tpl[setup], "\n", switch(
    pkg,
    rscala = paste(
      "mkdir %{packname}/inst/dependencies",
      "mv scala* %{packname}/inst/dependencies/scala",
      "mv sbt* %{packname}/inst/dependencies/sbt", sep="\n"),
    tcltk2 = paste(
      "sed -i 's@/bin/tclsh8.3@/usr/bin/tclsh@g'",
      "%{packname}/inst/tklibs/ctext3.2/function_finder.tcl"),
    askpass = {
      unlink(dir(file.path(path, "inst"), "^mac.*", full.names=TRUE))
      "rm -f %{packname}/inst/mac*" },
    RUnit = paste(
      "sed -i '/Sexpr/d' %{packname}/man/checkFuncs.Rd\n",
      "sed -i 's/\"runitVirtualClassTest.r\")}/\"runitVirtualClassTest.r\"/g'",
      "%{packname}/man/checkFuncs.Rd"),
    rgeolocate = "echo \"PKG_LIBS += -lrt\" >> %{packname}/src/Makevars.in",
    h2o = "cp %{SOURCE1} %{packname}/inst/java",
    nws=,OpenMx=,irace=,configr=,goldi=,RWebLogo=,rSymPy=,ndl=,scrobbler=,
    chromoR=,uavRmp=,SoilR=,dynwrap=,RcppRedis=,protViz=,PRISMA=paste(
      "find %{packname} -type f -exec",
      "sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \\;"),
    shinyAce=, googleComputeEngineR =
      "find %{packname}/inst -type f -exec chmod a-x {} \\;",
    TMB = "sed -ie '/onAttach/,+4d' %{packname}/R/zzz.R",
    excerptr = paste(
      "find %{packname}/inst -type f -name *.cl -exec chmod a-x {} \\;\n",
      "find %{packname}/inst -type f -exec",
      "sed -Ei 's@#!( )*(/usr)*/bin/(env )*dash@#!/usr/bin/sh@g' {} \\;"),
    funr = paste(
      "find %{packname}/inst -type f -exec",
      "sed -Ei 's@#!( )*(/usr)/bin/(env )*lr@#!/usr/bin/r@g' {} \\;"),
    getopt = paste(
      "find %{packname} -type f -exec",
      "sed -Ei 's@/path/to/Rscript@/usr/bin/Rscript@g' {} \\;"),
    rhli = "rm -f %{packname}/src/Makevars*",
    spcosa = "sed -i '/Sexpr/d' %{packname}/man/spcosa-package.Rd",
    rgexf = "sed -i '/system.file/d' %{packname}/man/plot.gexf.Rd",
    TexExamRandomizer=, SCORPIUS = paste(
      "find %{packname} -type f -exec",
      "sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \\;"),
    svSocket = paste(
      "find %{packname} -type f -exec",
      "sed -Ei 's@/local/bin/tclsh8.4@/bin/tclsh@g' {} \\;")
  ))

  # install
  install <- grep("%install", tpl)
  tpl[install] <- paste0(tpl[install], "\n", switch(
    pkg,
    aws=,biglars=,bsamGP=,deldir=,deSolve=,DRAFT=,DynamicGP=,EDR=,eha=,float=,
    frailtypack=,frontier=,lbfgsb3=,lbfgsb3c=,lsei=,mclust=,mda=,n1qn1=,
    npsp=,robeth=,robustbase=,rootSolve=,sequoia=,subplex=,VGAM=paste(
      "test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R &&",
      "echo \"FFLAGS=$(R CMD config FFLAGS) -fallow-argument-mismatch\" > ~/.R/Makevars"),
    RcppCWB=paste(
      "test $(gcc -dumpversion) -ge 10 && mkdir -p ~/.R &&",
      "find %{packname} -name Makefile -exec sed -i '/^all:.*/i CFLAGS+=-fcommon' {} \\;"),
    rPython = "export RPYTHON_PYTHON_VERSION=3",
    RcppParallel = "export RCPP_PARALLEL_BACKEND=tinythread",
    Rmpi = "%{_openmpi_load}"
  ))
  install <- grep("CMD INSTALL", tpl)
  tpl[install] <- paste0(tpl[install], switch(
    pkg,
    udunits2 = "\\\n  --configure-args='--with-udunits2-include=/usr/include/udunits2'",
    proj4 = "\\\n --configure-vars='PKG_CPPFLAGS=-DACCEPT_USE_OF_DEPRECATED_PROJ_API_H'"
  ))

  # other
  if (pkg %in% c("adapr", "taber"))
    unlink(file.path(path, "data"))

  tpl
}

create_spec <- function(pkg, cran=available_packages()) {
  tarfile <- download.packages(pkg, tempdir(), cran, quiet=TRUE)[,2]
  untar(tarfile, exdir=tempdir())
  path <- file.path(tempdir(), pkg)
  tpl <- readLines(getOption("copr.tpl"))
  tpl <- pkg_exceptions(tpl, pkg, path)

  # fields
  desc <- read.dcf(file.path(path, "DESCRIPTION"))
  desc <- as.data.frame(desc, stringsAsFactors=FALSE)
  if (!dir.exists(file.path(path, "src")))
    cran[cran[,"Package"] == desc$Package, "NeedsCompilation"] = "no"
  deps <- pkg_deps(desc, cran)
  description <- strwrap(desc$Description, 75)

  tpl <- sub("\\{\\{prefix\\}\\}", getOption("copr.prefix"), tpl)
  tpl <- sub("\\{\\{packname\\}\\}", pkg, tpl)
  tpl <- sub("\\{\\{packver\\}\\}", desc$Version, tpl)
  tpl <- sub("\\{\\{version\\}\\}", gsub("-", ".", desc$Version), tpl)
  tpl <- sub("\\{\\{summary\\}\\}", gsub("\n", "", desc$Title), tpl)
  tpl <- sub("\\{\\{license\\}\\}", desc$License, tpl)
  tpl <- sub("\\{\\{dependencies\\}\\}", paste(deps, collapse="\n"), tpl)
  tpl <- sub("\\{\\{description\\}\\}", paste(description, collapse="\n"), tpl)

  # java
  if (any(grepl("BuildRequires:[[:space:]]+R-java-devel", deps))) {
    inst <- grep("R CMD INSTALL", tpl)
    tpl[inst] <- paste0("%{_bindir}/R CMD javareconf -e '", tpl[inst], "'")
  }
  # display
  if (any(grepl("BuildRequires:[[:space:]]+xorg-x11-server-Xvfb", deps))) {
    inst <- grep("R CMD INSTALL", tpl)
    tpl[inst] <- paste("xvfb-run", tpl[inst])
  }

  tpl
}

get_url_copr <- function() paste(
  "https://copr.fedorainfracloud.org/coprs",
  copr_call("whoami"), getOption("copr.repo"), sep="/")

get_url_back <- function() paste(
  "https://copr-be.cloud.fedoraproject.org/results",
  copr_call("whoami"), getOption("copr.repo"), sep="/")

get_url_builds <- function(ids, chroots) {
  stopifnot(is.list(ids))
  pkgs <- ids[[2]]
  ids <- ids[[1]]
  ids <- ifelse(nchar(ids) == 7, paste0(0, ids), ids)
  paste0(get_url_back(), "/", chroots, "/", ids, "-", pkgs)
}

get_chroots <- function() {
  repo <- paste0(copr_call("whoami"), "/", getOption("copr.repo"))
  out <- grep(repo, copr_call("list"), value=TRUE)
  trimws(sapply(strsplit(out, ":"), "[", 1))
}

.read_urls <- function(urls, bytes=NULL) {
  tmp <- tempfile(rep("file", length(urls)))
  file.create(tmp)
  timeout <- getOption("timeout")
  on.exit({
    unlink(tmp)
    options(timeout=timeout)
  })
  options(timeout=3600L)

  headers <- character(0)
  if (!is.null(bytes))
    headers <- c(headers, range=paste0("bytes=0-", bytes-1))
  try(suppressWarnings(
    download.file(urls, tmp, mode="a", headers=headers)), silent=TRUE)
  lapply(tmp, readLines, warn=FALSE)
}

get_monitor <- function() {
  stopifnot(requireNamespace("XML", quietly=TRUE))
  url <- paste(get_url_copr(), "monitor", "detailed", sep="/")
  df <- XML::readHTMLTable(.read_urls(url)[[1]])[[1]]
  colnames(df) <- c("Package", get_chroots())
  na.omit(df)
}

get_builds <- function() {
  stopifnot(requireNamespace("XML", quietly=TRUE))
  url <- paste(get_url_copr(), "builds", sep="/")
  XML::readHTMLTable(.read_urls(url)[[1]])[[1]]
}

subset_failed <- function(x, chroots=seq_len(ncol(x)-1)) {
  x.chrt <- x[, 2:ncol(x), drop=FALSE]
  x.fail <- x.chrt[, chroots, drop=FALSE]
  x.succ <- x.chrt[, setdiff(names(x.chrt), names(x.fail)), drop=FALSE]
  x.fail <- apply(x.fail, 2, function(x) grepl("failed", x))
  x.succ <- apply(x.succ, 2, function(x) grepl("succeeded|forked", x))
  subset(x, apply(cbind(x.fail, x.succ), 1, all))
}

subset_vmismatch <- function(x, chroots=seq_len(ncol(x)-1)) {
  x.chrt <- x[, 2:ncol(x), drop=FALSE]
  x.mism <- x.chrt[, chroots, drop=FALSE]
  x.mism <- apply(x.mism, 2, function(x) {
    ver <- sapply(strsplit(x, "[[:space:]]+"), "[", 3)
    sapply(strsplit(ver, "-"), "[", 1)
  })
  x.mism <- apply(x.mism, 1, function(x) {
    !all(sapply(seq_along(x)[-1], function(i) x[1] == x[i]))
  })
  subset(x, x.mism)
}

have_build_msg <- function(ids, chroots, msg, bytes=NULL) {
  urls <- paste0(get_url_builds(ids, chroots), "/builder-live.log.gz")
  contents <- .read_urls(urls, bytes=bytes)
  grepl(msg, contents)
}
