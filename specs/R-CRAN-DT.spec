%global packname  DT
%global packver   0.15
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.15
Release:          1%{?dist}
Summary:          A Wrapper of the JavaScript Library 'DataTables'

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets >= 1.3
BuildRequires:    R-CRAN-jsonlite >= 0.9.16
BuildRequires:    R-CRAN-htmltools >= 0.3.6
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-promises 
Requires:         R-CRAN-htmlwidgets >= 1.3
Requires:         R-CRAN-jsonlite >= 0.9.16
Requires:         R-CRAN-htmltools >= 0.3.6
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-promises 

%description
Data objects in R can be rendered as HTML tables using the JavaScript
library 'DataTables' (typically via R Markdown or Shiny). The 'DataTables'
library has been included in this R package. The package name 'DT' is an
abbreviation of 'DataTables'.

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
