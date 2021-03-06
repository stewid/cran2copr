%global packname  leafem
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          'leaflet' Extensions for 'mapview'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet >= 2.0.1
BuildRequires:    R-CRAN-htmltools >= 0.3
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-png 
Requires:         R-CRAN-leaflet >= 2.0.1
Requires:         R-CRAN-htmltools >= 0.3
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-png 

%description
Provides extensions for packages 'leaflet' & 'mapdeck', many of which are
used by package 'mapview'. Focus is on functionality readily available in
Geographic Information Systems such as 'Quantum GIS'. Includes functions
to display coordinates of mouse pointer position, query image values via
mouse pointer and zoom-to-layer buttons. Additionally, provides a feature
type agnostic function to add points, lines, polygons to a map.

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
