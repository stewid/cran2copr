%global packname  statsExpressions
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          2%{?dist}
Summary:          Expressions with Statistical Details

License:          GPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ipmisc >= 3.0.1
BuildRequires:    R-CRAN-WRS2 >= 1.1.0
BuildRequires:    R-CRAN-correlation >= 0.3.0
BuildRequires:    R-CRAN-broomExtra 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-effectsize 
BuildRequires:    R-CRAN-ez 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-metaplus 
BuildRequires:    R-CRAN-rcompanion 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyBF 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ipmisc >= 3.0.1
Requires:         R-CRAN-WRS2 >= 1.1.0
Requires:         R-CRAN-correlation >= 0.3.0
Requires:         R-CRAN-broomExtra 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-effectsize 
Requires:         R-CRAN-ez 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-metaplus 
Requires:         R-CRAN-rcompanion 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tidyBF 
Requires:         R-CRAN-tidyr 

%description
Statistical processing backend for 'ggstatsplot', this package creates
expressions with details from statistical tests. Currently, it supports
only the most common types of statistical tests: parametric,
nonparametric, robust, and Bayesian versions of t-test/ANOVA, correlation
analyses, contingency table analysis, and meta-analysis.

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
