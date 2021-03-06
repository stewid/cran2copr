%global packname  ragg
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          2%{?dist}
Summary:          Graphic Devices Based on AGG

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    freetype-devel
BuildRequires:    libpng-devel
BuildRequires:    libtiff-devel
BuildRequires:    libjpeg-turbo-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-systemfonts >= 0.2.1
Requires:         R-CRAN-systemfonts >= 0.2.1

%description
Anti-Grain Geometry (AGG) is a high-quality and high-performance 2D
drawing library. The 'ragg' package provides a set of graphic devices
based on AGG to use as alternative to the raster devices provided through
the 'grDevices' package.

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
