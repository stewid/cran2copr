%global packname  rnpn
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Interface to the National 'Phenology' Network 'API'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-httr >= 1.1.0
BuildRequires:    R-CRAN-jsonlite >= 0.9.19
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-httr >= 1.1.0
Requires:         R-CRAN-jsonlite >= 0.9.19
Requires:         R-stats 
Requires:         R-CRAN-plyr 

%description
Programmatic interface to the Web Service methods provided by the National
'Phenology' Network (<https://usanpn.org/>), which includes data on
various life history events that occur at specific times.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ignore
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
