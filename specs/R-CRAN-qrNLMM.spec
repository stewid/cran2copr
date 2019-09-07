%global packname  qrNLMM
%global packver   1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Quantile Regression for Nonlinear Mixed-Effects Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ghyp 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-ald 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ghyp 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-psych 
Requires:         R-tcltk 
Requires:         R-CRAN-ald 

%description
Quantile regression (QR) for Nonlinear Mixed-Effects Models via the
asymmetric Laplace distribution (ALD). It uses the Stochastic
Approximation of the EM (SAEM) algorithm for deriving exact maximum
likelihood estimates and full inference results for the fixed-effects and
variance components. It also provides graphical summaries for assessing
the algorithm convergence and fitting results.

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
%{rlibdir}/%{packname}/INDEX
