%global packname  Rd2roxygen
%global packver   1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9
Release:          1%{?dist}
Summary:          Convert Rd to 'Roxygen' Documentation

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-roxygen2 >= 4.0.0
BuildRequires:    R-CRAN-formatR >= 1.0
Requires:         R-CRAN-roxygen2 >= 4.0.0
Requires:         R-CRAN-formatR >= 1.0

%description
Functions to convert Rd to 'roxygen' documentation. It can parse an Rd
file to a list, create the 'roxygen' documentation and update the original
R script (e.g. the one containing the definition of the function)
accordingly. This package also provides utilities that can help developers
build packages using 'roxygen' more easily. The 'formatR' package can be
used to reformat the R code in the examples sections so that the code will
be more readable.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%{rlibdir}/%{packname}/INDEX