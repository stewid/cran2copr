%global packname  dittodb
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          A Test Environment for Database Requests

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-utils 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-glue 
Requires:         R-methods 
Requires:         R-CRAN-testthat 
Requires:         R-utils 

%description
Testing and documenting code that communicates with remote databases can
be painful. Although the interaction with R is usually relatively simple
(e.g. data(frames) passed to and from a database), because they rely on a
separate service and the data there, testing them can be difficult to set
up, unsustainable in a continuous integration environment, or impossible
without replicating an entire production cluster. This package addresses
that by allowing you to make recordings from your database interactions
and then play them back while testing (or in other contexts) all without
needing to spin up or have access to the database your code would
typically connect to.

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
