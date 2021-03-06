%global packname  incidence
%global packver   1.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.2
Release:          1%{?dist}
Summary:          Compute, Handle, Plot and Model Incidence of Dated Events

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-CRAN-aweek >= 0.2.0
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-CRAN-aweek >= 0.2.0

%description
Provides functions and classes to compute, handle and visualise incidence
from dated events for a defined time interval. Dates can be provided in
various standard formats. The class 'incidence' is used to store computed
incidence and can be easily manipulated, subsetted, and plotted. In
addition, log-linear models can be fitted to 'incidence' objects using
'fit'. This package is part of the RECON
(<http://www.repidemicsconsortium.org/>) toolkit for outbreak analysis.

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
