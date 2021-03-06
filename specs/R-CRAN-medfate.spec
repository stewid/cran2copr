%global packname  medfate
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Mediterranean Forest Simulation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-meteoland >= 0.8.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spdep 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
Requires:         R-CRAN-meteoland >= 0.8.1
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spdep 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 

%description
Functions to simulate Mediterranean forest functioning and dynamics using
cohort-based description of vegetation [De Caceres et al. (2015)
<doi:10.1016/j.agrformet.2015.06.012>].

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
