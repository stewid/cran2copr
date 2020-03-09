%global packname  hal9001
%global packver   0.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          The Scalable Highly Adaptive Lasso

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-origami >= 0.8.1
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-origami >= 0.8.1
Requires:         R-CRAN-Rcpp 
Requires:         R-Matrix 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-glmnet 

%description
A scalable implementation of the highly adaptive lasso algorithm,
including routines for constructing sparse matrices of basis functions of
the observed data, as well as a custom implementation of Lasso regression
tailored to enhance efficiency when the matrix of predictors is composed
exclusively of indicator functions. For ease of use and increased
flexibility, the Lasso fitting routines invoke code from the 'glmnet'
package by default. The highly adaptive lasso was first formulated and
described by MJ van der Laan (2017) <doi:10.1515/ijb-2015-0097>, with
practical demonstrations of its performance given by Benkeser and van der
Laan (2016) <doi:10.1109/DSAA.2016.93>.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs