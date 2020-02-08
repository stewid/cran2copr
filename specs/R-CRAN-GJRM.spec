%global packname  GJRM
%global packver   0.2-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Generalised Joint Regression Modelling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-magic 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-trust 
BuildRequires:    R-CRAN-VineCopula 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-scam 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-distrEx 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-trustOptim 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-ismev 
Requires:         R-mgcv 
Requires:         R-CRAN-magic 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-trust 
Requires:         R-CRAN-VineCopula 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-scam 
Requires:         R-survival 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-distrEx 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-trustOptim 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-ismev 

%description
Routines for fitting various joint (and univariate) regression models,
with several types of covariate effects, in the presence of equations'
errors association, endogeneity, non-random sample selection or partial
observability.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
