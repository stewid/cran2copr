%global packname  ingredients
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}
Summary:          Effects and Importances of Model Ingredients

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-DALEX 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-scales 
Requires:         R-CRAN-DALEX 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-scales 

%description
Collection of tools for assessment of feature importance and feature
effects. Key functions are: feature_importance() for assessment of global
level feature importance, ceteris_paribus() for calculation of the what-if
plots, partial_dependency() for partial dependency plots,
conditional_dependency() for conditional dependency plots,
accumulated_dependency() for accumulated local effects plots,
aggregate_profiles() and cluster_profiles() for aggregation of ceteris
paribus profiles, generic print() and plot() for better usability of
selected explainers, generic plotD3() for interactive, D3 based
explanations, and generic describe() for explanations in natural language.
The package 'ingredients' is a part of the 'DrWhy.AI' universe (Biecek
2018) <arXiv:1806.08915>.

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
%doc %{rlibdir}/%{packname}/d3js
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX