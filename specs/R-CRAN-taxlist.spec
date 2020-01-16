%global packname  taxlist
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Handling Taxonomic Lists

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-foreign 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-taxize 
BuildRequires:    R-CRAN-stringdist 
BuildRequires:    R-CRAN-vegdata 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-foreign 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-taxize 
Requires:         R-CRAN-stringdist 
Requires:         R-CRAN-vegdata 

%description
Handling taxonomic lists through objects of class 'taxlist'. This package
provides functions to import species lists from 'Turboveg'
(<https://www.synbiosys.alterra.nl/turboveg>) and the possibility to
create backups from resulting R-objects. Also quick displays are
implemented as summary-methods.

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/cyperus
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/tv_data
%{rlibdir}/%{packname}/INDEX