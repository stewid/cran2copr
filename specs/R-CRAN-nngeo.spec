%global packname  nngeo
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}
Summary:          k-Nearest Neighbor Join for Spatial Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-sf >= 0.6
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lwgeom 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-s2 
Requires:         R-CRAN-sf >= 0.6
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-units 
Requires:         R-methods 
Requires:         R-CRAN-lwgeom 
Requires:         R-parallel 
Requires:         R-CRAN-s2 

%description
K-nearest neighbor search for projected and non-projected 'sf' spatial
layers. Nearest neighbor search uses (1) C code from 'GeographicLib' for
lon-lat point layers, (2) function nn2() from package 'RANN' for projected
point layers, or (3) function st_distance() from package 'sf' for line or
polygon layers. The package also includes several other utility functions
for spatial analysis.

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
