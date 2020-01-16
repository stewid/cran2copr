%global packname  OncoBayes2
%global packver   0.4-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.4
Release:          1%{?dist}
Summary:          Bayesian Logistic Regression for Oncology Dose-Escalation Trials

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.18.0
BuildRequires:    R-CRAN-BH >= 1.66.0
BuildRequires:    R-CRAN-rstantools >= 1.4.0
BuildRequires:    R-CRAN-bayesplot >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 0.7.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-RBesT 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-rstantools >= 1.4.0
Requires:         R-CRAN-bayesplot >= 1.4.0
Requires:         R-CRAN-dplyr >= 0.7.1
Requires:         R-CRAN-Rcpp >= 0.12.0
Requires:         R-methods 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-RBesT 

%description
Bayesian logistic regression model with optional
EXchangeability-NonEXchangeability parameter modelling for flexible
borrowing from historical or concurrent data-sources. The safety model can
guide dose-escalation decisions for adaptive oncology Phase I
dose-escalation trials which involve an arbitrary number of drugs. Please
refer to Neuenschwander et al. (2008) <doi:10.1002/sim.3230> and
Neuenschwander et al. (2016) <doi:10.1080/19466315.2016.1174149> for
details on the methodology.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/sbc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs