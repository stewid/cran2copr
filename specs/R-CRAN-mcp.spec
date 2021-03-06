%global packname  mcp
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Regression with Multiple Change Points

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.9
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-loo >= 2.1.0
BuildRequires:    R-CRAN-tidybayes >= 2.0.3
BuildRequires:    R-CRAN-bayesplot >= 1.7.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.4.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-patchwork >= 1.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.1
BuildRequires:    R-CRAN-tidyselect >= 0.2.5
BuildRequires:    R-CRAN-coda >= 0.19.3
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-stats 
Requires:         R-CRAN-rjags >= 4.9
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-loo >= 2.1.0
Requires:         R-CRAN-tidybayes >= 2.0.3
Requires:         R-CRAN-bayesplot >= 1.7.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.4.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-patchwork >= 1.0.0
Requires:         R-CRAN-rlang >= 0.4.1
Requires:         R-CRAN-tidyselect >= 0.2.5
Requires:         R-CRAN-coda >= 0.19.3
Requires:         R-parallel 
Requires:         R-CRAN-future 
Requires:         R-CRAN-future.apply 
Requires:         R-stats 

%description
Flexible and informed regression with Multiple Change Points (MCP). 'mcp'
can infer change points in means, variances, autocorrelation structure,
and any combination of these, as well as the parameters of the segments in
between. All parameters are estimated with uncertainty and prediction
intervals are supported - also near the change points. 'mcp' supports
hypothesis testing via Savage-Dickey density ratio, posterior contrasts,
and cross-validation. 'mcp' is described in Lindeløv (submitted)
<doi:10.31219/osf.io/fzqxv> and generalizes the approach described in
Carlin, Gelfand, & Smith (1992) <doi:10.2307/2347570> and Stephens (1994)
<doi:10.2307/2986119>.

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
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
