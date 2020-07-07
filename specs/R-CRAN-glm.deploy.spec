%global packname  glm.deploy
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}
Summary:          'C' and 'Java' Source Code Generator for Fitted Glm Objects

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-stats 

%description
Provides two functions that generate source code implementing the predict
function of fitted glm objects. In this version, code can be generated for
either 'C' or 'Java'. The idea is to provide a tool for the easy and fast
deployment of glm predictive models into production. The source code
generated by this package implements two function/methods. One of such
functions implements the equivalent to predict(type="response"), while the
second implements predict(type="link"). Source code is written to disk as
a .c or .java file in the specified path. In the case of c, an .h file is
also generated.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
