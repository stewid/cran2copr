%global packname  tidycomm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          Data Modification and Analysis for Communication Research

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MBESS 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MBESS 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Provides convenience functions for common data modification and analysis
tasks in communication research. This includes functions for univariate
and bivariate data analysis, index generation and reliability computation,
and intercoder reliability tests. All functions follow the style and
syntax of the tidyverse, and are construed to perform their computations
on multiple variables at once. Functions for univariate and bivariate data
analysis comprise summary statistics for continuous and categorical
variables, as well as several tests of bivariate association including
effect sizes. Functions for data modification comprise index generation
and automated reliability analysis of index variables. Functions for
intercoder reliability comprise tests of several intercoder reliability
estimates, including simple and mean pairwise percent agreement,
Krippendorff's Alpha (Krippendorff 2004, ISBN: 9780761915454), and various
Kappa coefficients (Brennan & Prediger 1981 <doi:
10.1177/001316448104100307>; Cohen 1960 <doi: 10.1177/001316446002000104>;
Fleiss 1971 <doi: 10.1037/h0031619>).

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
