%global packname  GDINA
%global packver   2.8.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.8.0
Release:          3%{?dist}
Summary:          The Generalized DINA Model Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.1
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rsolnp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinydashboard 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.1
Requires:         R-CRAN-alabama 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-MASS 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rsolnp 
Requires:         R-stats 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinydashboard 
Requires:         R-utils 

%description
A set of psychometric tools for cognitive diagnosis modeling based on the
generalized deterministic inputs, noisy and gate (G-DINA) model by de la
Torre (2011) <DOI:10.1007/s11336-011-9207-7> and its extensions, including
the sequential G-DINA model by Ma and de la Torre (2016)
<DOI:10.1111/bmsp.12070> for polytomous responses, and the polytomous
G-DINA model by Chen and de la Torre <DOI:10.1177/0146621613479818> for
polytomous attributes. Joint attribute distribution can be independent,
saturated, higher-order, loglinear smoothed or structured. Q-matrix
validation, item and model fit statistics, model comparison at test and
item level and differential item functioning can also be conducted. A
graphical user interface is also provided. For tutorials, please check Ma
and de la Torre (2020) <DOI:10.18637/jss.v093.i14>, Ma and de la Torre
(2019) <DOI:10.1111/emip.12262>, Ma (2019)
<DOI:10.1007/978-3-030-05584-4_29> and de la Torre and Akbay (2019)
<DOI:10.14689/ejer.2019.80.9>.

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
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
