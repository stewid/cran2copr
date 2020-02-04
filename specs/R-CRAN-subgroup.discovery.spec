%global packname  subgroup.discovery
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Subgroup Discovery and Bump Hunting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-RcppParallel >= 4.4.4
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-RcppParallel >= 4.4.4
Requires:         R-CRAN-Rcpp >= 1.0.3

%description
Developed to assist in discovering interesting subgroups in
high-dimensional data. The PRIM implementation is based on the 1998 paper
"Bump hunting in high-dimensional data" by Jerome H. Friedman and Nicholas
I. Fisher <doi:10.1023/A:1008894516817>. PRIM involves finding a set of
"rules" which combined imply unusually large values of some other target
variable. Specifically one tries to find a set of sub regions in which the
target variable is substantially larger than overall mean. The objective
of bump hunting in general is to find regions in the input
(attribute/feature) space with relatively high values for the target
variable. The regions are described by simple rules of the type if:
condition-1 and ... and condition-n then: estimated target value. Given
the data (or a subset of the data), the goal is to produce a box B within
which the target mean is as large as possible.

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
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
