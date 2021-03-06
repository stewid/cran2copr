%global packname  pivottabler
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          2%{?dist}
Summary:          Create Pivot Tables

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 >= 2.2.0
BuildRequires:    R-CRAN-data.table >= 1.10.0
BuildRequires:    R-CRAN-htmlwidgets >= 0.8
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-htmltools >= 0.3.5
Requires:         R-CRAN-R6 >= 2.2.0
Requires:         R-CRAN-data.table >= 1.10.0
Requires:         R-CRAN-htmlwidgets >= 0.8
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-htmltools >= 0.3.5

%description
Create regular pivot tables with just a few lines of R. More complex pivot
tables can also be created, e.g. pivot tables with irregular layouts,
multiple calculations and/or derived calculations based on multiple data
frames.  Pivot tables are constructed using R only and can be written to a
range of output formats (plain text, 'HTML', 'Latex' and 'Excel'),
including with styling/formatting.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/htmlwidgets
%{rlibdir}/%{packname}/INDEX
