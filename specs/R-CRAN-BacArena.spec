%global packname  BacArena
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          1%{?dist}
Summary:          Modeling Framework for Cellular Communities in theirEnvironments

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-ReacTran >= 1.4.2
BuildRequires:    R-CRAN-sybil >= 1.3.0
BuildRequires:    R-Matrix >= 1.2
BuildRequires:    R-CRAN-deSolve >= 1.12
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-glpkAPI 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-ReacTran >= 1.4.2
Requires:         R-CRAN-sybil >= 1.3.0
Requires:         R-Matrix >= 1.2
Requires:         R-CRAN-deSolve >= 1.12
Requires:         R-CRAN-igraph 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-glpkAPI 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-Rcpp 

%description
Can be used for simulation of organisms living in communities. Each
organism is represented individually and genome scale metabolic models
determine the uptake and release of compounds. Biological processes such
as movement, diffusion, chemotaxis and kinetics are available along with
data analysis techniques.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
