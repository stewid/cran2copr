%global packname  IRkernel
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Native R Kernel for the 'Jupyter Notebook'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    python3dist(jupyter-kernel-test)
BuildRequires:    python3dist(ndjson-testrunner)
Requires:         python-jupyter-filesystem
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 0.9.6
BuildRequires:    R-CRAN-repr >= 0.4.99
BuildRequires:    R-CRAN-IRdisplay >= 0.3.0.9999
BuildRequires:    R-CRAN-pbdZMQ >= 0.2.1
BuildRequires:    R-CRAN-evaluate >= 0.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-jsonlite >= 0.9.6
Requires:         R-CRAN-repr >= 0.4.99
Requires:         R-CRAN-IRdisplay >= 0.3.0.9999
Requires:         R-CRAN-pbdZMQ >= 0.2.1
Requires:         R-CRAN-evaluate >= 0.10
Requires:         R-methods 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-digest 

%description
The R kernel for the 'Jupyter' environment executes R code which the
front-end ('Jupyter Notebook' or other front-ends) submits to the kernel
via the network.

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
