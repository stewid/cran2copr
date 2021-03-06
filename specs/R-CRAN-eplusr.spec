%global packname  eplusr
%global packver   0.13.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.13.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Toolkit for Using Whole Building Simulation Program'EnergyPlus'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-processx >= 3.2.0
BuildRequires:    R-CRAN-callr >= 2.0.4
BuildRequires:    R-CRAN-progress >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-cli >= 1.1.0
BuildRequires:    R-CRAN-rgl >= 0.100.26
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-decido 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-units 
Requires:         R-CRAN-processx >= 3.2.0
Requires:         R-CRAN-callr >= 2.0.4
Requires:         R-CRAN-progress >= 1.2.0
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-cli >= 1.1.0
Requires:         R-CRAN-rgl >= 0.100.26
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-decido 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-units 

%description
A rich toolkit of using the whole building simulation program
'EnergyPlus'(<https://energyplus.net>), which enables programmatic
navigation, modification of 'EnergyPlus' models and makes it less painful
to do parametric simulations and analysis.

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
