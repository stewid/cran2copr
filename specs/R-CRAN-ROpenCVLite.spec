%global packname  ROpenCVLite
%global packver   4.30.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.30.2
Release:          2%{?dist}
Summary:          Install 'OpenCV'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    cmake
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pkgbuild 
BuildRequires:    R-parallel 
Requires:         R-utils 
Requires:         R-CRAN-pkgbuild 
Requires:         R-parallel 

%description
Installs 'OpenCV' for use by other packages. 'OpenCV'
<https://opencv.org/> is library of programming functions mainly aimed at
real-time computer vision. This 'Lite' version contains the stable base
version of 'OpenCV' and does not contain any of its externally contributed
modules.

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
