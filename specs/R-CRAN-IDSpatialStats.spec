%global packname  IDSpatialStats
%global packver   0.3.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.10
Release:          3%{?dist}
Summary:          Estimate Global Clustering in Infectious Disease

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-spatstat 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-spatstat 

%description
Implements various novel and standard clustering statistics and other
analyses useful for understanding the spread of infectious disease.

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
%doc %{rlibdir}/%{packname}/tests
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
