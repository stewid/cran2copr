%global packname  projects
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          A Project Infrastructure for Researchers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zip >= 2.0.2
BuildRequires:    R-CRAN-tibble >= 2.0.1
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-fs >= 1.2.6
BuildRequires:    R-CRAN-readr >= 1.1.1
BuildRequires:    R-CRAN-sessioninfo >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.8.0.1
BuildRequires:    R-CRAN-rstudioapi >= 0.7
BuildRequires:    R-CRAN-rlang >= 0.3.4
BuildRequires:    R-CRAN-purrr >= 0.2.5
BuildRequires:    R-methods 
Requires:         R-CRAN-zip >= 2.0.2
Requires:         R-CRAN-tibble >= 2.0.1
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-fs >= 1.2.6
Requires:         R-CRAN-readr >= 1.1.1
Requires:         R-CRAN-sessioninfo >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.8.0.1
Requires:         R-CRAN-rstudioapi >= 0.7
Requires:         R-CRAN-rlang >= 0.3.4
Requires:         R-CRAN-purrr >= 0.2.5
Requires:         R-methods 

%description
Provides a project infrastructure with a focus on manuscript creation.
Creates a project folder with a single command, containing subdirectories
for specific components, templates for manuscripts, and so on.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX