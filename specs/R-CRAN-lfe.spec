%global packname  lfe
%global packver   2.8-5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.5.1
Release:          2%{?dist}
Summary:          Linear Group Fixed Effects

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.2
Requires:         R-core >= 2.15.2
BuildRequires:    R-Matrix >= 1.1.2
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-parallel 
Requires:         R-Matrix >= 1.1.2
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-xtable 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-sandwich 
Requires:         R-parallel 

%description
Transforms away factors with many levels prior to doing an OLS. Useful for
estimating linear models with multiple group fixed effects, and for
estimating linear models which uses factors with many levels as pure
control variables. Includes support for instrumental variables,
conditional F statistics for weak instruments, robust and multi-way
clustered standard errors, as well as limited mobility bias correction.

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
