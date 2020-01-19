%global packname  OCNet
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Optimal Channel Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-SSN 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-rgl 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-SSN 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 

%description
Generate and analyze Optimal Channel Networks (OCNs): oriented spanning
trees reproducing all scaling features characteristic of real, natural
river networks. As such, they can be used in a variety of numerical
experiments in the fields of hydrology, ecology and epidemiology. See
Rinaldo et al. (2014) <doi:10.1073/pnas.1322700111> for an overview on the
OCN concept; Furrer and Sain (2010) <doi:10.18637/jss.v036.i10> for the
construct used.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs