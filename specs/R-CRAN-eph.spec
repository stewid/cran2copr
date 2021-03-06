%global packname  eph
%global packver   0.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.0
Release:          2%{?dist}
Summary:          Argentina's Permanent Household Survey Data and ManipulationUtilities

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-expss 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-questionr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-attempt 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-expss 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-questionr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-utils 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-attempt 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-xml2 
Requires:         R-stats 

%description
Tools to download and manipulate the Permanent Household Survey from
Argentina (EPH is the Spanish acronym for Permanent Household Survey).
e.g: get_microdata() for downloading the datasets, get_poverty_lines() for
downloading the official poverty baskets, calculate_poverty() for the
calculation of stating if a household is in poverty or not, following the
official methodology. organize_panels() is used to concatenate
observations from different periods, and organize_labels() adds the
official labels to the data. The implemented methods are based on INDEC
(2016)
<http://www.estadistica.ec.gba.gov.ar/dpe/images/SOCIEDAD/EPH_metodologia_22_pobreza.pdf>.
As this package works with the argentinian Permanent Household Survey and
its main audience is from this country, the documentation was written in
Spanish.

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
