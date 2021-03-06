%global packname  CBPS
%global packver   0.21
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.21
Release:          3%{?dist}
Summary:          Covariate Balancing Propensity Score

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-MatchIt 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-glmnet 
Requires:         R-MASS 
Requires:         R-CRAN-MatchIt 
Requires:         R-nnet 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-glmnet 

%description
Implements the covariate balancing propensity score (CBPS) proposed by
Imai and Ratkovic (2014) <DOI:10.1111/rssb.12027>. The propensity score is
estimated such that it maximizes the resulting covariate balance as well
as the prediction of treatment assignment. The method, therefore, avoids
an iteration between model fitting and balance checking.  The package also
implements optimal CBPS from Fan et al. (2016)
<https://imai.fas.harvard.edu/research/CBPStheory.html>, several
extensions of the CBPS beyond the cross-sectional, binary treatment
setting. They include the CBPS for longitudinal settings so that it can be
used in conjunction with marginal structural models from Imai and Ratkovic
(2015) <DOI:10.1080/01621459.2014.956872>, treatments with three- and
four-valued treatment variables, continuous-valued treatments from Fong,
Hazlett, and Imai (2018) <DOI:10.1214/17-AOAS1101>, propensity score
estimation with a large number of covariates from Ning, Peng, and Imai
(2018) <arXiv:1812.08683>, and the situation with multiple distinct binary
treatments administered simultaneously. In the future it will be extended
to other settings including the generalization of experimental and
instrumental variable estimates.

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
