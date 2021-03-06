%global packname  gaiah
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          3%{?dist}
Summary:          Genetic and Isotopic Assignment Accounting for HabitatSuitability

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-geosphere 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sp 

%description
Tools for using genetic markers, stable isotope data, and habitat
suitability data to calculate posterior probabilities of breeding origin
of migrating birds.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
