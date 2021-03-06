%global packname  RSiteCatalyst
%global packver   1.4.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.16
Release:          3%{?dist}
Summary:          R Client for Adobe Analytics API V1.4

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr >= 1.8
BuildRequires:    R-CRAN-jsonlite >= 1.0
BuildRequires:    R-CRAN-httr >= 1.0
BuildRequires:    R-CRAN-stringr >= 1.0
BuildRequires:    R-CRAN-digest >= 0.6
BuildRequires:    R-CRAN-base64enc >= 0.1
Requires:         R-CRAN-plyr >= 1.8
Requires:         R-CRAN-jsonlite >= 1.0
Requires:         R-CRAN-httr >= 1.0
Requires:         R-CRAN-stringr >= 1.0
Requires:         R-CRAN-digest >= 0.6
Requires:         R-CRAN-base64enc >= 0.1

%description
Functions for interacting with the Adobe Analytics API V1.4
(<https://api.omniture.com/admin/1.4/rest/>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
