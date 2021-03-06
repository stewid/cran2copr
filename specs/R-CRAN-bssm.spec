%global packname  bssm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Bayesian Inference of Non-Gaussian State Space Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildRequires:    R-CRAN-coda >= 0.18.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-CRAN-diagis 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-ramcmc 
BuildRequires:    R-CRAN-sitmo 
Requires:         R-CRAN-coda >= 0.18.1
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-CRAN-diagis 

%description
Efficient methods for Bayesian inference of state space models via
particle Markov chain Monte Carlo (MCMC) and MCMC based on parallel
importance sampling type weighted estimators (Vihola, Helske, and Franks,
2020, <arXiv:1609.02541>). Gaussian, Poisson, binomial, negative binomial,
and Gamma observation densities and basic stochastic volatility models
with Gaussian state dynamics, as well as general non-linear Gaussian
models and discretised diffusion models are supported.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
