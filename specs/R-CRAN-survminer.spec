%global packname  survminer
%global packver   0.4.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.8
Release:          1%{?dist}
Summary:          Drawing Survival Curves using 'ggplot2'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gridExtra >= 2.0
BuildRequires:    R-CRAN-ggpubr >= 0.1.6
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-maxstat 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-survival 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-survMisc 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-gridExtra >= 2.0
Requires:         R-CRAN-ggpubr >= 0.1.6
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-maxstat 
Requires:         R-methods 
Requires:         R-CRAN-scales 
Requires:         R-survival 
Requires:         R-stats 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-survMisc 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rlang 

%description
Contains the function 'ggsurvplot()' for drawing easily beautiful and
'ready-to-publish' survival curves with the 'number at risk' table and
'censoring count plot'. Other functions are also available to plot
adjusted curves for `Cox` model and to visually examine 'Cox' model
assumptions.

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
