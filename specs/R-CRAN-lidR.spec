%global packname  lidR
%global packver   3.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.3
Release:          1%{?dist}
Summary:          Airborne LiDAR Data Manipulation and Visualization for ForestryApplications

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-BH >= 1.72.0
BuildRequires:    R-CRAN-sp >= 1.4.2
BuildRequires:    R-CRAN-rlas >= 1.3.5
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-RCSF 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-sp >= 1.4.2
Requires:         R-CRAN-rlas >= 1.3.5
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-future 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-glue 
Requires:         R-grDevices 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-RCSF 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-sf 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Airborne LiDAR (Light Detection and Ranging) interface for data
manipulation and visualization. Read/write 'las' and 'laz' files,
computation of metrics in area based approach, point filtering, artificial
point reduction, classification from geographic data, normalization,
individual tree segmentation and other manipulations.

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
