%global packname  dLagM
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Time Series Regression Models with Distributed Lag Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-nardl 
BuildRequires:    R-CRAN-dynlm 
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-wavethresh 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-roll 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-nardl 
Requires:         R-CRAN-dynlm 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-wavethresh 
Requires:         R-MASS 
Requires:         R-CRAN-roll 
Requires:         R-CRAN-sandwich 

%description
Provides time series regression models with one predictor using finite
distributed lag models, polynomial (Almon) distributed lag models,
geometric distributed lag models with Koyck transformation, and
autoregressive distributed lag models. It also consists of functions for
computation of h-step ahead forecasts from these models. See Demirhan
(2020)(<doi:10.1371/journal.pone.0228812>) and Baltagi
(2011)(<doi:10.1007/978-3-642-20059-5>) for more information.

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
