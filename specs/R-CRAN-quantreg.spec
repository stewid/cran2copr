%global packname  quantreg
%global packver   5.61
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.61
Release:          1%{?dist}
Summary:          Quantile Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6
Requires:         R-core >= 2.6
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-MatrixModels 
BuildRequires:    R-CRAN-conquer 
Requires:         R-stats 
Requires:         R-CRAN-SparseM 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-Matrix 
Requires:         R-CRAN-MatrixModels 
Requires:         R-CRAN-conquer 

%description
Estimation and inference methods for models of conditional quantiles:
Linear and nonlinear parametric and non-parametric (total variation
penalized) models for conditional quantiles of a univariate response and
several methods for handling censored survival data.  Portfolio selection
methods based on expected shortfall risk are also now included.

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
