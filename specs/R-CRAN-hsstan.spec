%global packname  hsstan
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          2%{?dist}
Summary:          Hierarchical Shrinkage Stan Models for Biomarker Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-rstan >= 2.18.1
BuildRequires:    R-CRAN-StanHeaders >= 2.17.2
BuildRequires:    R-CRAN-loo >= 2.1.0
BuildRequires:    R-CRAN-rstantools >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.66.0.1
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.15
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-rstan >= 2.18.1
Requires:         R-CRAN-loo >= 2.1.0
Requires:         R-CRAN-rstantools >= 2.0.0
Requires:         R-CRAN-ggplot2 
Requires:         R-parallel 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-Rcpp >= 0.12.15
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Linear and logistic regression models penalized with hierarchical
shrinkage priors for selection of biomarkers (or more general variable
selection), which can be fitted using Stan (Carpenter et al. (2017)
<doi:10.18637/jss.v076.i01>). It implements the horseshoe and regularized
horseshoe priors (Piironen and Vehtari (2017) <doi:10.1214/17-EJS1337SI>),
as well as the projection predictive selection approach to recover a
sparse set of predictive biomarkers (Piironen, Paasiniemi and Vehtari
(2020) <doi:10.1214/20-EJS1711>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
