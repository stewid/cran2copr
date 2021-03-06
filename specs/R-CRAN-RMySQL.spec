%global packname  RMySQL
%global packver   0.10.20
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10.20
Release:          3%{?dist}
Summary:          Database Interface and 'MySQL' Driver for R

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    mariadb-devel
BuildRequires:    R-devel >= 2.8.0
Requires:         R-core >= 2.8.0
BuildRequires:    R-CRAN-DBI >= 0.4
BuildRequires:    R-methods 
Requires:         R-CRAN-DBI >= 0.4
Requires:         R-methods 

%description
Legacy 'DBI' interface to 'MySQL' / 'MariaDB' based on old code ported
from S-PLUS. A modern 'MySQL' client based on 'Rcpp' is available from the
'RMariaDB' package.

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
%{rlibdir}/%{packname}/libs
