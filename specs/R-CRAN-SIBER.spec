%global debug_package %{nil}
%global packname  SIBER
%global packver   2.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.4
Release:          1%{?dist}
Summary:          Stable Isotope Bayesian Ellipses in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-hdrcde 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-spatstat.utils 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-hdrcde 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-spatstat.utils 
Requires:         R-stats 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 

%description
Fits bi-variate ellipses to stable isotope data using Bayesian inference
with the aim being to describe and compare their isotopic niche.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
