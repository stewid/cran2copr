%global packname  fsbrain
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          2%{?dist}
Summary:          Managing and Visualizing Brain Surface Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-freesurferformats >= 0.1.11
BuildRequires:    R-CRAN-pkgfilecache >= 0.1.1
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-squash 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-freesurferformats >= 0.1.11
Requires:         R-CRAN-pkgfilecache >= 0.1.1
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-squash 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-data.table 

%description
Provides high-level access to 'FreeSurfer' <http://freesurfer.net/>
neuroimaging data on the level of subjects and groups. Load morphometry
data, surfaces and brain parcellations based on atlases. Mask data using
labels, load data for specific atlas regions only, and visualize data and
results directly in 'R'.

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

%files
%{rlibdir}/%{packname}
