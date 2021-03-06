%global packname  BayesSUR
%global packver   1.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Bayesian Seemingly Unrelated Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.000
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-tikzDevice 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-igraph 
Requires:         R-Matrix 
Requires:         R-CRAN-tikzDevice 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Bayesian seemingly unrelated regression with general variable selection
and dense/sparse covariance matrix. The sparse seemingly unrelated
regression is described in Banterle et al. (2018) <doi:10.1101/467019>.

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
