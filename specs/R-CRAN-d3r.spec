%global packname  d3r
%global packver   0.8.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.7
Release:          1%{?dist}
Summary:          'd3.js' Utilities for R

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 0.7.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-tidyr >= 0.7.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-htmltools 

%description
Provides a suite of functions to help ease the use of 'd3.js' in R. These
helpers include 'htmltools::htmlDependency' functions, hierarchy builders,
and conversion tools for 'partykit', 'igraph,' 'table', and 'data.frame' R
objects into the 'JSON' that 'd3.js' expects.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
