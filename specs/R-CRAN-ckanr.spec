%global packname  ckanr
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Client for the Comprehensive Knowledge Archive Network ('CKAN')API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.17
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-DBI >= 0.3.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-jsonlite >= 0.9.17
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-DBI >= 0.3.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-magrittr 

%description
Client for 'CKAN' API (<https://ckan.org/>). Includes interface to 'CKAN'
'APIs' for search, list, show for packages, organizations, and resources.
In addition, provides an interface to the 'datastore' API.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX