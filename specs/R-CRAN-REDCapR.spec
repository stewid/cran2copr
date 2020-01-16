%global packname  REDCapR
%global packver   0.10.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.2
Release:          1%{?dist}
Summary:          Interaction Between R and REDCap

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tibble >= 1.4.0
BuildRequires:    R-CRAN-readr >= 1.3.1
BuildRequires:    R-CRAN-httr >= 1.3.0
BuildRequires:    R-CRAN-tidyr >= 0.7.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-tibble >= 1.4.0
Requires:         R-CRAN-readr >= 1.3.1
Requires:         R-CRAN-httr >= 1.3.0
Requires:         R-CRAN-tidyr >= 0.7.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 

%description
Encapsulates functions to streamline calls from R to the REDCap API.
REDCap (Research Electronic Data CAPture) is a web application for
building and managing online surveys and databases developed at Vanderbilt
University.  The Application Programming Interface (API) offers an avenue
to access and modify data programmatically, improving the capacity for
literate and reproducible programming.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/misc
%{rlibdir}/%{packname}/test-data
%{rlibdir}/%{packname}/INDEX