%global packname  boral
%global packver   1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Bayesian Ordination and Regression AnaLysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-fishMod 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-abind 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-fishMod 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-abind 

%description
Bayesian approaches for analyzing multivariate data in ecology. Estimation
is performed using Markov Chain Monte Carlo (MCMC) methods via Three. JAGS
types of models may be fitted: 1) With explanatory variables only, boral
fits independent column Generalized Linear Models (GLMs) to each column of
the response matrix; 2) With latent variables only, boral fits a purely
latent variable model for model-based unconstrained ordination; 3) With
explanatory and latent variables, boral fits correlated column GLMs with
latent variables to account for any residual correlation between the
columns of the response matrix.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX