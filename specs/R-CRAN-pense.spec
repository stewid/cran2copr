%global packname  pense
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}
Summary:          Penalized Elastic Net S/MM-Estimator of Regression

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-robustbase 
Requires:         R-parallel 
Requires:         R-methods 

%description
Robust penalized elastic net S and MM estimator for linear regression. The
method is described in detail in Cohen Freue, G. V., Kepplinger, D.,
Salibian-Barrera, M., and Smucler, E. (2017)
<https://gcohenfr.github.io/pdfs/PENSE_manuscript.pdf>.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs