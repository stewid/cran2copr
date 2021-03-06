%global packname  smicd
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Statistical Methods for Interval-Censored Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ineq 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-laeken 
BuildRequires:    R-CRAN-weights 
BuildRequires:    R-graphics 
Requires:         R-CRAN-ineq 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-laeken 
Requires:         R-CRAN-weights 
Requires:         R-graphics 

%description
Functions that provide statistical methods for interval-censored (grouped)
data. The package supports the estimation of linear and linear mixed
regression models with interval-censored dependent variables. Parameter
estimates are obtained by a stochastic expectation maximization algorithm.
Furthermore, the package enables the direct (without covariates)
estimation of statistical indicators from interval-censored data via an
iterative kernel density algorithm. Survey and Organisation for Economic
Co-operation and Development (OECD) weights can be included into the
direct estimation (see, Walter, P. (2019) <doi:10.17169/refubium-1621>).

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
