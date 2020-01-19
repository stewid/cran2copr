%global packname  mixl
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Simulated Maximum Likelihood Estimation of Mixed Logit Modelsfor Large Datasets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.19
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-randtoolbox 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-Rcpp >= 0.12.19
Requires:         R-stats 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-randtoolbox 
Requires:         R-CRAN-sandwich 

%description
Specification and estimation of multinomial logit models. Large datasets
and complex models are supported, with an intuitive syntax. Multinomial
Logit Models, Mixed models, random coefficients and Hybrid Choice are all
supported. For more information, see Molloy et al. (2019)
<doi:10.3929/ethz-b-000334289>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX