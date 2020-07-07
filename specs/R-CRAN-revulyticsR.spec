%global packname  revulyticsR
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          2%{?dist}
Summary:          Connect to Your 'Revulytics' Data

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.6.1
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-httr >= 1.4.1
BuildRequires:    R-CRAN-tibble >= 1.0.3
BuildRequires:    R-CRAN-tidyselect >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.4
BuildRequires:    R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-jsonlite >= 1.6.1
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-httr >= 1.4.1
Requires:         R-CRAN-tibble >= 1.0.3
Requires:         R-CRAN-tidyselect >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.4
Requires:         R-CRAN-purrr >= 0.3.3

%description
Facilitates making a connection to the 'Revulytics' API and executing
various queries. You can use it to get event data and metadata. The
Revulytics documentation is available at
<https://docs.flexera.com/ui551/report/>. This package is not supported by
'Flexera' (owner of the software).

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
