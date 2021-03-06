%global packname  fabletools
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          2%{?dist}
Summary:          Core Tools for Packages in the 'fable' Framework

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 1.4.1
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tsibble >= 0.9.0
BuildRequires:    R-CRAN-rlang >= 0.4.5
BuildRequires:    R-CRAN-vctrs >= 0.2.2
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-distributional 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tibble >= 1.4.1
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tsibble >= 0.9.0
Requires:         R-CRAN-rlang >= 0.4.5
Requires:         R-CRAN-vctrs >= 0.2.2
Requires:         R-CRAN-tidyselect 
Requires:         R-stats 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-R6 
Requires:         R-utils 
Requires:         R-CRAN-distributional 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-lifecycle 

%description
Provides tools, helpers and data structures for developing models and time
series functions for 'fable' and extension packages. These tools support a
consistent and tidy interface for time series modelling and analysis.

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
