%global packname  Rdpack
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Update and Manipulate Rd Documentation Objects

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bibtex >= 0.4.0
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-gbRd 
Requires:         R-CRAN-bibtex >= 0.4.0
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-gbRd 

%description
Functions for manipulation of R documentation objects, including functions
reprompt() and ereprompt() for updating 'Rd' documentation for functions,
methods and classes; 'Rd' macros for citations and import of references
from 'bibtex' files for use in 'Rd' files and 'roxygen2' comments; 'Rd'
macros for evaluating and inserting snippets of 'R' code and the results
of its evaluation or creating graphics on the fly; and many functions for
manipulation of references and Rd files.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
