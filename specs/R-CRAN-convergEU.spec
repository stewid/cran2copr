%global packname  convergEU
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Monitoring Convergence of EU Countries

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-eurostat 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-formattable 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-eurostat 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-formattable 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 

%description
Indicators and measures by country and time describe what happens at
economic and social levels. This package provides functions to calculate
several measures of convergence after imputing missing values. The
automated downloading of Eurostat data, followed by the production of
country fiches and indicator fiches, makes possible to produce automated
reports.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/EUstat_download
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/vign
%{rlibdir}/%{packname}/INDEX