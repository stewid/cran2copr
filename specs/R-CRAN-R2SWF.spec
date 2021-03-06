%global packname  R2SWF
%global packver   0.9-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}
Summary:          Convert R Graphics to Flash Animations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    zlib-devel
BuildRequires:    libpng-devel
BuildRequires:    freetype-devel
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
Requires:         R-CRAN-sysfonts 
Requires:         R-grDevices 
Requires:         R-utils 

%description
Using the 'Ming' library <http://www.libming.org/> to create Flash
animations. Users can either use the 'SWF' device swf() to generate 'SWF'
file directly through plotting functions like plot() and lines(), or
convert images of other formats ('SVG', 'PNG', 'JPEG') into 'SWF'.

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
