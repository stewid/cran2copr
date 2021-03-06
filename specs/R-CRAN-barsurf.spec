%global packname  barsurf
%global packver   0.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Function Visualization and Smooth Multiband ColorInterpolation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-kubik 
BuildRequires:    R-CRAN-colorspace 
Requires:         R-methods 
Requires:         R-CRAN-kubik 
Requires:         R-CRAN-colorspace 

%description
Combined contour/heatmap plots, 3d bar/surface plots, isosurface plots,
triangular plots and 2d/3d vector fields. Builds on the colorspace package
(Zeileis, A., et al. (2019) <arxiv.org/abs/1903.06490>), by supporting
smooth multiband color interpolation, in sRGB, HSV and HCL color spaces.
The default color functions for heatmaps, use HCL (Zeileis, A., et al.
(2009) <doi:10.1016/j.csda.2008.11.033>) and support near-uniform
perception.

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
