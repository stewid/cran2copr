%global packname  see
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}
Summary:          Visualisation Toolbox for 'easystats' and Extra Geoms, Themesand Color Palettes for 'ggplot2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-effectsize 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-insight 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-parameters 
BuildRequires:    R-CRAN-rlang 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-effectsize 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-insight 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-parameters 
Requires:         R-CRAN-rlang 

%description
Provides plotting utilities supporting easystats-packages
(<https://github.com/easystats/easystats>) and some extra themes, geoms,
and scales for 'ggplot2'. Color scales are based on
<https://www.materialui.co/colors>.

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
