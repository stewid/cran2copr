%global packname  reproducible
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          A Set of Tools that Enhance Reproducibility Beyond PackageManagement

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-sp >= 1.4.2
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-fpCompare 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Require 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-sp >= 1.4.2
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-fpCompare 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-Require 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

%description
Collection of high-level, machine- and OS-independent tools for making
deeply reproducible and reusable content in R. The two workhorse functions
are Cache and prepInputs; these allow for: nested caching, robust to
environments, and objects with environments (like functions); and data
retrieval and processing in continuous workflow environments. In all
cases, efforts are made to make the first and subsequent calls of
functions have the same result, but vastly faster at subsequent times by
way of checksums and digesting. Several features are still under active
development, including cloud storage of cached objects, allowing for
sharing between users. Several advanced options are available, see
?reproducibleOptions.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
