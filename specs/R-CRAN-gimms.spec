%global packname  gimms
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}
Summary:          Download and Process GIMMS NDVI3g Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-CRAN-zyp 
Requires:         R-CRAN-raster 
Requires:         R-methods 
Requires:         R-CRAN-curl 
Requires:         R-parallel 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-ncdf4 
Requires:         R-CRAN-zyp 

%description
This is a set of functions to retrieve information about GIMMS NDVI3g
files currently available online; download (and re-arrange, in the case of
NDVI3g.v0) the half-monthly data sets from NASA Ames Ecological
Forecasting Lab (ECOCAST); import downloaded files from ENVI binary
(NDVI3g.v0) or NetCDF format (NDVI3g.v1) directly into R based on the
widespread 'raster' package; conduct quality control; and generate monthly
composites (e.g., maximum values) from the half-monthly input data. As a
special gimmick, a method is included to conveniently apply the
Mann-Kendall trend test upon 'Raster*' images, optionally featuring
trend-free pre-whitening to account for lag-1 autocorrelation.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
