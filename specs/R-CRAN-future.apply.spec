%global packname  future.apply
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          2%{?dist}
Summary:          Apply Function to Elements in Parallel using Futures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-future >= 1.17.0
BuildRequires:    R-CRAN-globals >= 0.12.5
BuildRequires:    R-parallel 
BuildRequires:    R-utils 
Requires:         R-CRAN-future >= 1.17.0
Requires:         R-CRAN-globals >= 0.12.5
Requires:         R-parallel 
Requires:         R-utils 

%description
Implementations of apply(), by(), eapply(), lapply(), Map(), .mapply(),
mapply(), replicate(), sapply(), tapply(), and vapply() that can be
resolved using any future-supported backend, e.g. parallel on the local
machine or distributed on a compute cluster.  These future_*apply()
functions come with the same pros and cons as the corresponding base-R
*apply() functions but with the additional feature of being able to be
processed via the future framework.

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
