%global packname  BayesPostEst
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Generate Postestimation Quantities for Bayesian MCMC Estimation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 0.5.1
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-coda >= 0.13
BuildRequires:    R-CRAN-carData 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-ggmcmc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ROCR 
BuildRequires:    R-stats 
Requires:         R-CRAN-tidyr >= 0.5.1
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-coda >= 0.13
Requires:         R-CRAN-carData 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-ggmcmc 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ROCR 
Requires:         R-stats 

%description
An implementation of functions to generate and plot postestimation
quantities after estimating Bayesian regression models using Markov chain
Monte Carlo (MCMC). Functionality includes the estimation of the
Precision-Recall curves (see Beger, 2016 <doi:10.2139/ssrn.2765419>), the
implementation of the observed values method of calculating predicted
probabilities by Hanmer and Kalkan (2013)
<doi:10.1111/j.1540-5907.2012.00602.x>, the implementation of the average
value method of calculating predicted probabilities (see King, Tomz, and
Wittenberg, 2000 <doi:10.2307/2669316>), and the generation and plotting
of first differences to summarize typical effects across covariates (see
Long 1997, ISBN:9780803973749; King, Tomz, and Wittenberg, 2000
<doi:10.2307/2669316>). This package can be used with MCMC output
generated by any Bayesian estimation tool including 'JAGS', 'BUGS',
'MCMCpack', and 'Stan'.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
