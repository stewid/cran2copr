%global packname  waiter
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Loading Screen for 'Shiny'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-rstudioapi 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-rstudioapi 

%description
Full screen and partial loading screens for 'Shiny' with spinners,
progress bars, and notifications.

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
