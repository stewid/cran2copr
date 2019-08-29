%global packname  foghorn
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Summarize CRAN Check Results in the Terminal

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.2
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-crayon >= 1.3.2
BuildRequires:    R-CRAN-httr >= 1.2.1
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-clisymbols >= 1.0.0
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-rvest >= 0.3.2
Requires:         R-CRAN-curl >= 2.2
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-crayon >= 1.3.2
Requires:         R-CRAN-httr >= 1.2.1
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-clisymbols >= 1.0.0
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-rvest >= 0.3.2

%description
The CRAN check results in your R terminal.

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
%{rlibdir}/%{packname}/INDEX
