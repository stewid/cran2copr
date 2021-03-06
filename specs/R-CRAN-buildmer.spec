%global packname  buildmer
%global packver   1.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Stepwise Elimination and Term Reordering for Mixed-EffectsRegression

License:          FreeBSD
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
BuildRequires:    R-mgcv 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-lme4 
Requires:         R-methods 
Requires:         R-mgcv 
Requires:         R-nlme 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-utils 

%description
Finds the largest possible regression model that will still converge for
various types of regression analyses (including mixed models and
generalized additive models) and then optionally performs stepwise
elimination similar to the forward and backward effect-selection methods
in SAS, based on the change in log-likelihood or its significance,
Akaike's Information Criterion, the Bayesian Information Criterion, the
explained deviance, or the F-test of the change in R².

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
