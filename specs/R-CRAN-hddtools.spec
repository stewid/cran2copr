%global packname  hddtools
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          3%{?dist}
Summary:          Hydrological Data Discovery Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-rnrfa 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-rnrfa 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-tidyr 

%description
Tools to discover hydrological data, accessing catalogues and databases
from various data providers.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/paper
%{rlibdir}/%{packname}/INDEX
