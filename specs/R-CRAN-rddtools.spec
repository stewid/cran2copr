%global packname  rddtools
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Toolbox for Regression Discontinuity Design ('RDD')

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-AER 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-KernSmooth 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rdd 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-Formula 
BuildRequires:    R-CRAN-locpol 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rdrobust 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-AER 
Requires:         R-CRAN-np 
Requires:         R-KernSmooth 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rdd 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-Formula 
Requires:         R-CRAN-locpol 
Requires:         R-methods 
Requires:         R-CRAN-rdrobust 
Requires:         R-CRAN-rmarkdown 

%description
Set of functions for Regression Discontinuity Design ('RDD'), for data
visualisation, estimation and testing.

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
