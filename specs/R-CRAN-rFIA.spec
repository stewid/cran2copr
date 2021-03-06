%global packname  rFIA
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}
Summary:          Space-Time Estimation of Forest Variables using the FIA Database

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gganimate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-sf 
Requires:         R-parallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gganimate 
Requires:         R-methods 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-purrr 

%description
The goal of 'rFIA' is to increase the accessibility and use of the United
States Forest Services (USFS) Forest Inventory and Analysis (FIA) Database
by providing a user-friendly, open source toolkit to easily query and
analyze FIA Data. Designed to accommodate a wide range of potential user
objectives, 'rFIA' simplifies the estimation of forest variables from the
FIA Database and allows all R users (experts and newcomers alike) to
unlock the flexibility inherent to the Enhanced FIA design. Specifically,
'rFIA' improves accessibility to the spatio-temporal estimation capacity
of the FIA Database by producing space-time indexed summaries of forest
variables within user-defined population boundaries. Direct integration
with other popular R packages (e.g., 'dplyr', 'tidyr', and 'sf')
facilitates efficient space-time query and data summary, and supports
common data representations and API design. The package implements
design-based estimation procedures outlined by Bechtold & Patterson (2005)
<doi:10.2737/SRS-GTR-80>, and has been validated against estimates and
sampling errors produced by FIA 'EVALIDator'. Current development is
focused on the implementation of spatially-enabled model-assisted
estimators to improve population, change, and ratio estimates.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
