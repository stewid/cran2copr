%global packname  spData
%global packver   0.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.8
Release:          2%{?dist}
Summary:          Datasets for Spatial Analysis

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 

%description
Diverse spatial datasets for demonstrating, benchmarking and teaching
spatial data analysis. It includes R data of class sf (defined by the
package 'sf'), Spatial ('sp'), and nb ('spdep'). Unlike other spatial data
packages such as 'rnaturalearth' and 'maps', it also contains data stored
in a range of file formats including GeoJSON, ESRI Shapefile and
GeoPackage. Some of the datasets are designed to illustrate specific
analysis techniques. cycle_hire() and cycle_hire_osm(), for example, is
designed to illustrate point pattern analysis techniques.

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
