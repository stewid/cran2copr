%global packname  enveomics.R
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}
Summary:          Various Utilities for Microbial Genomics and Metagenomics

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.9
Requires:         R-core >= 2.9
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-CRAN-investr 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-sn 
Requires:         R-CRAN-investr 

%description
A collection of functions for microbial ecology and other applications of
genomics and metagenomics. Companion package for the Enveomics Collection
(Rodriguez-R, L.M. and Konstantinidis, K.T., 2016
<DOI:10.7287/peerj.preprints.1900v1>).

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
