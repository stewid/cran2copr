%global packname  lingtypology
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}
Summary:          Linguistic Typology and Mapping

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-leaflet.minicharts 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-leaflet.minicharts 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-stringdist 
Requires:         R-grDevices 

%description
Provides R with the Glottolog database <http://glottolog.org> and some
more abilities for purposes of linguistic mapping. The Glottolog database
contains the catalogue of languages of the world. This package helps
researchers to make a linguistic maps, using philosophy of the
Cross-Linguistic Linked Data project <http://clld.org/>, which allows for
while at the same time facilitating uniform access to the data across
publications. A tutorial for this package is available on GitHub pages
<https://docs.ropensci.org/lingtypology/> and package vignette. Maps
created by this package can be used both for the investigation and
linguistic teaching. In addition, package provides an ability to download
data from typological databases such as WALS, AUTOTYP and some others and
to create your own database website.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
