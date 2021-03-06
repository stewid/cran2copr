%global packname  Rcmdr
%global packver   2.7-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Commander

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    xorg-x11-server-Xvfb
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-effects >= 4.0.3
BuildRequires:    R-CRAN-car >= 3.0.8
BuildRequires:    R-CRAN-RcmdrMisc >= 2.7.1
BuildRequires:    R-CRAN-tcltk2 >= 1.2.6
BuildRequires:    R-CRAN-relimp >= 1.0.5
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-splines 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-lme4 
Requires:         R-CRAN-effects >= 4.0.3
Requires:         R-CRAN-car >= 3.0.8
Requires:         R-CRAN-RcmdrMisc >= 2.7.1
Requires:         R-CRAN-tcltk2 >= 1.2.6
Requires:         R-CRAN-relimp >= 1.0.5
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-splines 
Requires:         R-tcltk 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-lme4 

%description
A platform-independent basic-statistics GUI (graphical user interface) for
R, based on the tcltk package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
