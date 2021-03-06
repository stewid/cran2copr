%global packname  robustHD
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          3%{?dist}
Summary:          Robust Methods for High-Dimensional Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-robustbase >= 0.9.5
BuildRequires:    R-CRAN-ggplot2 >= 0.9.2
BuildRequires:    R-CRAN-Rcpp >= 0.9.10
BuildRequires:    R-CRAN-RcppArmadillo >= 0.3.0
BuildRequires:    R-CRAN-perry >= 0.2.0
BuildRequires:    R-MASS 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-robustbase >= 0.9.5
Requires:         R-CRAN-ggplot2 >= 0.9.2
Requires:         R-CRAN-Rcpp >= 0.9.10
Requires:         R-CRAN-perry >= 0.2.0
Requires:         R-MASS 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Robust methods for high-dimensional data, in particular linear model
selection techniques based on least angle regression and sparse
regression.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
