%global packname  stormwindmodel
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Model Tropical Cyclone Wind Speeds

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-maps >= 3.3.0
BuildRequires:    R-CRAN-plyr >= 1.8.6
BuildRequires:    R-CRAN-lubridate >= 1.7.9
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-weathermetrics >= 1.2.2
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-maps >= 3.3.0
Requires:         R-CRAN-plyr >= 1.8.6
Requires:         R-CRAN-lubridate >= 1.7.9
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-weathermetrics >= 1.2.2
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.7

%description
Allows users to input tracking data for a hurricane or other tropical
storm, along with a data frame of grid points at which to model wind
speeds. Functions in this package will then calculate wind speeds at each
point based on wind model equations. This modeling framework is currently
set up to model winds for North American locations with Atlantic basin
storms. This work was supported in part by grants from the National
Institute of Environmental Health Sciences (R00ES022631), the National
Science Foundation (1331399), and the Department of Energy
(DE-FG02-08ER64644).

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
