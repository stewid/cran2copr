%global packname  RobustGaSP
%global packver   0.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.0
Release:          1%{?dist}
Summary:          Robust Gaussian Stochastic Process Emulation

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-nloptr >= 1.0.4
BuildRequires:    R-CRAN-Rcpp >= 0.12.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-nloptr >= 1.0.4
Requires:         R-CRAN-Rcpp >= 0.12.3
Requires:         R-methods 

%description
Robust parameter estimation and prediction of Gaussian stochastic process
emulators. It allows for robust parameter estimation and prediction using
Gaussian stochastic process emulator. It also implements the parallel
partial Gaussian stochastic process emulator for computer model with
massive outputs See the reference: Mengyang Gu and Jim Berger, 2016,
Annals of Applied Statistics; Mengyang Gu, Xiaojing Wang and Jim Berger,
2018, Annals of Statistics.

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
