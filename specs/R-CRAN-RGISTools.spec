%global packname  RGISTools
%global packver   0.9.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.7
Release:          1%{?dist}
Summary:          Handling Multiplatform Satellite Images

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-gdalUtils 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-urltools 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-tools 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-httr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-gdalUtils 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-xml2 
Requires:         R-utils 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-urltools 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-rvest 
Requires:         R-tools 
Requires:         R-methods 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-httr 

%description
Downloading, customizing, and processing time series of satellite images
for a region of interest. 'RGISTools' functions allow a unified access to
multispectral images from Landsat, MODIS and Sentinel repositories.
'RGISTools' also offers capabilities for customizing satellite images,
such as tile mosaicking and image cropping. Finally, 'RGISTools' covers
the processing, including cloud masking, deriving new variables, and
gap-filling/smoothing time series of images (Militino et al., 2018
<doi:10.3390/rs10030398> and Militino et al., 2019
<doi:10.1109/TGRS.2019.2904193>).

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/ExNavarreVar
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX