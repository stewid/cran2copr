%global packname  hpiR
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          House Price Indexes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-imputeTS 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-imputeTS 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-zoo 

%description
Compute house price indexes and series using a variety of different
methods and models common through the real estate literature.  Evaluate
index 'goodness' based on accuracy, volatility and revision statistics.
Background on basic model construction for repeat sales models can be
found at: Case and Quigley (1991) <doi:10.2307/2109686> and for hedonic
pricing models at: Bourassa et al (2006) <doi:10.1016/j.jhe.2006.03.001>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX