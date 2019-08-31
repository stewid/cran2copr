%global packname  CAvariants
%global packver   4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0
Release:          1%{?dist}
Summary:          Correspondence Analysis Variants

License:          GPL (> 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel > 3.0.1
Requires:         R-core > 3.0.1
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-rgl 
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-rgl 

%description
Provides six variants of two-way correspondence analysis (ca): simple ca,
singly ordered ca, doubly ordered ca, non symmetrical ca, singly ordered
non symmetrical ca, and doubly ordered non symmetrical ca.

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