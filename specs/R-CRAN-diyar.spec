%global packname  diyar
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Multistage Record Linkage and Case Definition forEpidemiological Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate >= 1.7.4
BuildRequires:    R-CRAN-tidyr >= 0.8.2
BuildRequires:    R-CRAN-dplyr >= 0.7.5
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-lubridate >= 1.7.4
Requires:         R-CRAN-tidyr >= 0.8.2
Requires:         R-CRAN-dplyr >= 0.7.5
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 

%description
Perform multistage deterministic linkages, apply case definitions to
datasets, and deduplicate records. Records (rows) from datasets are linked
by different matching criteria and sub-criteria (columns) in a specified
order of certainty. The linkage process handles missing data and
conflicting matches based on this same order of certainty. For episode
grouping, rows of dated events (e.g. sample collection) or interval of
events (e.g. hospital admission) are grouped into chronological episodes
beginning with a "case". The process permits several options such as
episode lengths and recurrence periods which are used to build custom
preferences for case assignment (definition). The record linkage and
episode grouping processes assign unique group IDs to matching records or
those grouped into episodes. This then allows for record deduplication or
sub-analysis within these groups.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX