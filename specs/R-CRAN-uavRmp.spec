%global packname  uavRmp
%global packver   0.5.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.7
Release:          2%{?dist}
Summary:          UAV Mission Planner

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-log4r 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-brew 
BuildRequires:    R-CRAN-exifr 
BuildRequires:    R-CRAN-link2GI 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-geosphere 
Requires:         R-tools 
Requires:         R-CRAN-log4r 
Requires:         R-CRAN-zoo 
Requires:         R-methods 
Requires:         R-CRAN-brew 
Requires:         R-CRAN-exifr 
Requires:         R-CRAN-link2GI 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-rlang 

%description
The Unmanned Aerial Vehicle Mission Planner provides an easy to use work
flow for planning autonomous obstacle avoiding surveys of (almost) ready
to fly unmanned aerial vehicles to retrieve aerial or spot related data.
It creates either intermediate flight control files for the DJI phantom
series or ready to upload control files for the pixhawk based flight
controller as used in the 3DR Solo. Additionally it contains some useful
tools for digitizing and data manipulation.

%prep
%setup -q -c -n %{packname}
find %{packname} -type f -exec sed -Ei 's@#!( )*(/usr)*/bin/(env )*python@#!/usr/bin/python2@g' {} \;
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
