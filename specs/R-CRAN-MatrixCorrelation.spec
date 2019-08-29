%global packname  MatrixCorrelation
%global packver   0.9.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          Matrix Correlation Coefficients

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-RSpectra 

%description
Computation and visualization of matrix correlation coefficients. The main
method is the Similarity of Matrices Index, while various related measures
like r1, r2, r3, r4, Yanai's GCD, RV, RV2 and adjusted RV are included for
comparison.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
