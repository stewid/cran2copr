%global packname  projects
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          3%{?dist}
Summary:          A Project Infrastructure for Researchers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 3.0.1
BuildRequires:    R-CRAN-zip >= 2.0.4
BuildRequires:    R-CRAN-lubridate >= 1.7.8
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-fs >= 1.4.1
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-sessioninfo >= 1.1.1
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-vctrs >= 0.2.4
BuildRequires:    R-CRAN-rstudioapi >= 0.11
BuildRequires:    R-methods 
Requires:         R-CRAN-tibble >= 3.0.1
Requires:         R-CRAN-zip >= 2.0.4
Requires:         R-CRAN-lubridate >= 1.7.8
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-fs >= 1.4.1
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-sessioninfo >= 1.1.1
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-vctrs >= 0.2.4
Requires:         R-CRAN-rstudioapi >= 0.11
Requires:         R-methods 

%description
Provides a project infrastructure with a focus on manuscript creation.
Creates a project folder with a single command, containing subdirectories
for specific components, templates for manuscripts, and so on.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/templates
%{rlibdir}/%{packname}/INDEX
