%global packname  covsim
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          VITA and IG Simulation for Given Covariance and Marginals

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan >= 0.6.5
BuildRequires:    R-CRAN-rvinecopulib >= 0.5.1.1.0
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-PearsonDS 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-gsl 
Requires:         R-CRAN-lavaan >= 0.6.5
Requires:         R-CRAN-rvinecopulib >= 0.5.1.1.0
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-PearsonDS 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-gsl 

%description
User specifies population covariance matrix. Marginal information may be
fully specified, for which the package implements the VITA
(VIne-To-Anything) algorithm. Groenneberg and Foldnes (2017)
<doi:10.1007/s11336-017-9569-6>. Alternatively, marginal skewness and
kurtosis may be specified, for which the package implements the IG
(independent generator) algorithm. Foldnes and Olsson (2016)
<doi:10.1080/00273171.2015.1133274>.

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

%files
%{rlibdir}/%{packname}
