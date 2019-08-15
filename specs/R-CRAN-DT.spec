%global packname  DT
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
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


%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/htmlwidgets
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
