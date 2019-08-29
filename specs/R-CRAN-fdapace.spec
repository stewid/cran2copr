%global packname  fdapace
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Functional Data Analysis and Empirical Dynamics

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-CRAN-Hmisc 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-numDeriv 

%description
Provides implementation of various methods of Functional Data Analysis
(FDA) and Empirical Dynamics. The core of this package is Functional
Principal Component Analysis (FPCA), a key technique for functional data
analysis, for sparsely or densely sampled random trajectories and time
courses, via the Principal Analysis by Conditional Estimation (PACE)
algorithm or numerical integration. PACE is useful for the analysis of
data that have been generated by a sample of underlying (but usually not
fully observed) random trajectories. It does not rely on pre-smoothing of
trajectories, which is problematic if functional data are sparsely
sampled. PACE provides options for functional regression and correlation,
for Longitudinal Data Analysis, the analysis of stochastic processes from
samples of realized trajectories, and for the analysis of underlying
dynamics. The core computational algorithms are implemented using the
'Eigen' C++ library for numerical linear algebra and 'RcppEigen' "glue".

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
