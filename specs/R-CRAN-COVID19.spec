%global packname  COVID19
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to COVID-19 Data Hub

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-wbstats 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-wbstats 

%description
Download COVID-19 data across governmental sources at national, regional,
and city level, as described in Guidotti and Ardia (2020)
<doi:10.21105/joss.02376>. Includes policy measures by 'Oxford COVID-19
Government Response Tracker'
<https://www.bsg.ox.ac.uk/research/research-projects/coronavirus-government-response-tracker>.
Provides a seamless integration with 'World Bank Open Data'
<https://data.worldbank.org/>, 'Google Mobility Reports'
<https://www.google.com/covid19/mobility/>, 'Apple Mobility Reports'
<https://covid19.apple.com/mobility>.

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
