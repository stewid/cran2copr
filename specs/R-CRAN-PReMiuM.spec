%global packname  PReMiuM
%global packver   3.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.3
Release:          3%{?dist}
Summary:          Dirichlet Process Bayesian Clustering, Profile Regression

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    make
BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-gamlss.dist >= 4.3.1
BuildRequires:    R-CRAN-plotrix >= 3.6.6
BuildRequires:    R-CRAN-ggplot2 >= 2.2
BuildRequires:    R-CRAN-BH >= 1.65.0.1
BuildRequires:    R-CRAN-rgdal >= 1.3.3
BuildRequires:    R-CRAN-data.table >= 1.10.4.3
BuildRequires:    R-CRAN-ald >= 1.1
BuildRequires:    R-CRAN-spdep >= 0.7.7
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.13
BuildRequires:    R-cluster 
Requires:         R-CRAN-gamlss.dist >= 4.3.1
Requires:         R-CRAN-plotrix >= 3.6.6
Requires:         R-CRAN-ggplot2 >= 2.2
Requires:         R-CRAN-rgdal >= 1.3.3
Requires:         R-CRAN-data.table >= 1.10.4.3
Requires:         R-CRAN-ald >= 1.1
Requires:         R-CRAN-spdep >= 0.7.7
Requires:         R-CRAN-Rcpp >= 0.12.13
Requires:         R-cluster 

%description
Bayesian clustering using a Dirichlet process mixture model. This model is
an alternative to regression models, non-parametrically linking a response
vector to covariate data through cluster membership. The package allows
Bernoulli, Binomial, Poisson, Normal, survival and categorical response,
as well as Normal and discrete covariates. It also allows for fixed
effects in the response model, where a spatial CAR (conditional
autoregressive) term can be also included. Additionally, predictions may
be made for the response, and missing values for the covariates are
handled. Several samplers and label switching moves are implemented along
with diagnostic tools to assess convergence. A number of R functions for
post-processing of the output are also provided. In addition to fitting
mixtures, it may additionally be of interest to determine which covariates
actively drive the mixture components. This is implemented in the package
as variable selection. The main reference for the package is Liverani,
Hastie, Azizi, Papathomas and Richardson (2015)
<doi:10.18637/jss.v064.i07>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/shapes
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
