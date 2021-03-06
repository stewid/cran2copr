%global packname  googleAnalyticsR
%global packver   0.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.0
Release:          2%{?dist}
Summary:          Google Analytics API into R

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 2.0.2
BuildRequires:    R-CRAN-tibble >= 2.0.1
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.3.1
BuildRequires:    R-CRAN-googleAuthR >= 1.3.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.0
BuildRequires:    R-CRAN-purrr >= 0.2.2
BuildRequires:    R-CRAN-assertthat >= 0.2.0
BuildRequires:    R-CRAN-rlang >= 0.1.0
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 2.0.2
Requires:         R-CRAN-tibble >= 2.0.1
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.3.1
Requires:         R-CRAN-googleAuthR >= 1.3.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.0
Requires:         R-CRAN-purrr >= 0.2.2
Requires:         R-CRAN-assertthat >= 0.2.0
Requires:         R-CRAN-rlang >= 0.1.0
Requires:         R-CRAN-memoise 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Interact with the Google Analytics APIs
<https://developers.google.com/analytics/>, including the Core Reporting
API (v3 and v4), Management API, User Activity API and Multi-Channel
Funnel API.

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

%files
%{rlibdir}/%{packname}
