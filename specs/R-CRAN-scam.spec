%global packname  scam
%global packver   1.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          3%{?dist}
Summary:          Shape Constrained Additive Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildRequires:    R-mgcv >= 1.8.2
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-Matrix 
BuildRequires:    R-splines 
Requires:         R-mgcv >= 1.8.2
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-Matrix 
Requires:         R-splines 

%description
Routines for generalized additive modelling under shape constraints on the
component functions of the linear predictor (Pya and Wood, 2015)
<doi:10.1007/s11222-013-9448-7>. Models can contain multiple shape
constrained (univariate and/or bivariate) and unconstrained terms. The
routines of gam() in package 'mgcv' are used for setting up the model
matrix, printing and plotting the results.  Penalized likelihood
maximization based on Newton-Raphson method is used to fit a model with
multiple smoothing parameter selection by GCV or UBRE/AIC.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
