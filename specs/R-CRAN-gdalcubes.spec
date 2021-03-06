%global packname  gdalcubes
%global packver   0.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Earth Observation Data Cubes from Satellite Image Collections

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel
BuildRequires:    proj-devel
BuildRequires:    libcurl-devel
BuildRequires:    netcdf-devel
BuildRequires:    sqlite-devel
BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppProgress 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-ncdf4 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppProgress 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-ncdf4 

%description
Processing collections of Earth observation images as on-demand
multispectral, multitemporal raster data cubes. Users define cubes by
spatiotemporal extent, resolution, and spatial reference system and let
'gdalcubes' automatically apply cropping, reprojection, and resampling
using the 'Geospatial Data Abstraction Library' ('GDAL'). Implemented
functions on data cubes include reduction over space and time, applying
arithmetic expressions on pixel band values, moving window aggregates over
time, filtering by space, time, bands, and predicates on pixel values,
exporting data cubes as 'netCDF' or 'GeoTIFF' files, and plotting.  The
package implements lazy evaluation and multithreading. All computational
parts are implemented in C++, linking to the 'GDAL', 'netCDF', 'CURL', and
'SQLite' libraries. See Appel and Pebesma (2019) <doi:10.3390/data4030092>
for further details.

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
