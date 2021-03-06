%global packname  Cyclops
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          3%{?dist}
Summary:          Cyclic Coordinate Descent for Logistic, Poisson and SurvivalAnalysis

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-BH >= 1.51.0
BuildRequires:    R-CRAN-RcppEigen >= 0.3.2
BuildRequires:    R-CRAN-Andromeda >= 0.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-methods 
BuildRequires:    R-survival 
Requires:         R-CRAN-Andromeda >= 0.3.1
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-rlang 
Requires:         R-Matrix 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dbplyr 
Requires:         R-methods 
Requires:         R-survival 

%description
This model fitting tool incorporates cyclic coordinate descent and
majorization-minimization approaches to fit a variety of regression models
found in large-scale observational healthcare data.  Implementations focus
on computational optimization and fine-scale parallelization to yield
efficient inference in massive datasets.  Please see: Suchard, Simpson,
Zorych, Ryan and Madigan (2013) <doi:10.1145/2414416.2414791>.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
