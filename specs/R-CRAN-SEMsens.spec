%global packname  SEMsens
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          A Tool for Sensitivity Analysis in Structural Equation Modeling

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-stats 
Requires:         R-CRAN-lavaan 
Requires:         R-stats 

%description
Perform sensitivity analysis in structural equation modeling using
meta-heuristic optimization methods (e.g., ant colony optimization and
others). The references for the proposed methods are: (1) Harring, J. R.,
McNeish, D. M., & Hancock, G. R. (2017)
<doi:10.1080/10705511.2018.1506925>; (2) Socha, K., & Dorigo, M. (2008)
<doi:10.1016/j.ejor.2006.06.046>. We also thank Dr. Krzysztof Socha for
sharing his thesis and R code, which provided the base for the development
of this package.

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
