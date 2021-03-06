%global packname  bookdown
%global packver   0.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.20
Release:          2%{?dist}
Summary:          Authoring Books and Technical Documents with R Markdown

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 2.3
BuildRequires:    R-CRAN-knitr >= 1.22
BuildRequires:    R-CRAN-xfun >= 0.6
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-tinytex >= 0.12
Requires:         R-CRAN-rmarkdown >= 2.3
Requires:         R-CRAN-knitr >= 1.22
Requires:         R-CRAN-xfun >= 0.6
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-tinytex >= 0.12

%description
Output formats and utilities for authoring books and technical documents
with R Markdown.

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

%files
%{rlibdir}/%{packname}
