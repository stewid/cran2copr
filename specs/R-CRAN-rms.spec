%global packname  rms
%global packver   6.0-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          6.0.1
Release:          1%{?dist}
Summary:          Regression Modeling Strategies

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Hmisc >= 4.3.0
BuildRequires:    R-nlme >= 3.1.123
BuildRequires:    R-survival >= 3.1.12
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-htmlTable >= 1.11.0
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-MASS 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-Hmisc >= 4.3.0
Requires:         R-nlme >= 3.1.123
Requires:         R-survival >= 3.1.12
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-htmlTable >= 1.11.0
Requires:         R-lattice 
Requires:         R-CRAN-SparseM 
Requires:         R-methods 
Requires:         R-CRAN-quantreg 
Requires:         R-rpart 
Requires:         R-CRAN-polspline 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-htmltools 
Requires:         R-MASS 
Requires:         R-cluster 
Requires:         R-CRAN-digest 

%description
Regression modeling, testing, estimation, validation, graphics,
prediction, and typesetting by storing enhanced model design attributes in
the fit.  'rms' is a collection of functions that assist with and
streamline modeling.  It also contains functions for binary and ordinal
logistic regression models, ordinal models for continuous Y with a variety
of distribution families, and the Buckley-James multiple regression model
for right-censored responses, and implements penalized maximum likelihood
estimation for logistic and ordinary linear models.  'rms' works with
almost any regression model, but it was especially written to work with
binary or ordinal regression models, Cox regression, accelerated failure
time models, ordinary linear models, the Buckley-James model, generalized
least squares for serially or spatially correlated observations,
generalized linear models, and quantile regression.

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
