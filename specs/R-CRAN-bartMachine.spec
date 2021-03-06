%global packname  bartMachine
%global packver   1.2.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Additive Regression Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         java
BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bartMachineJARs >= 1.0
BuildRequires:    R-CRAN-rJava >= 0.9.8
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-bartMachineJARs >= 1.0
Requires:         R-CRAN-rJava >= 0.9.8
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-missForest 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 

%description
An advanced implementation of Bayesian Additive Regression Trees with
expanded features for data analysis and visualization.

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
