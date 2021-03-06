%global packname  fable
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Forecasting Models for Tidy Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tsibble >= 0.9.0
BuildRequires:    R-CRAN-rlang >= 0.4.6
BuildRequires:    R-CRAN-fabletools >= 0.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-distributional 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tsibble >= 0.9.0
Requires:         R-CRAN-rlang >= 0.4.6
Requires:         R-CRAN-fabletools >= 0.2.0
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-distributional 

%description
Provides a collection of commonly used univariate and multivariate time
series forecasting models including automatically selected exponential
smoothing (ETS) and autoregressive integrated moving average (ARIMA)
models. These models work within the 'fable' framework provided by the
'fabletools' package, which provides the tools to evaluate, visualise, and
combine models in a workflow consistent with the tidyverse.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
