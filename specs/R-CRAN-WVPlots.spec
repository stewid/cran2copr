%global packname  WVPlots
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Common Plots for Analysis

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-wrapr >= 1.9.0
BuildRequires:    R-CRAN-rquery >= 1.3.8
BuildRequires:    R-CRAN-rqdatatable >= 1.2.2
BuildRequires:    R-CRAN-cdata >= 1.1.2
BuildRequires:    R-CRAN-sigr >= 1.0.6
BuildRequires:    R-utils 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-graphics 
BuildRequires:    R-mgcv 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-wrapr >= 1.9.0
Requires:         R-CRAN-rquery >= 1.3.8
Requires:         R-CRAN-rqdatatable >= 1.2.2
Requires:         R-CRAN-cdata >= 1.1.2
Requires:         R-CRAN-sigr >= 1.0.6
Requires:         R-utils 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-graphics 
Requires:         R-mgcv 
Requires:         R-stats 

%description
Select data analysis plots, under a standardized calling interface
implemented on top of 'ggplot2' and 'plotly'. Plots of interest include:
'ROC', gain curve, scatter plot with marginal distributions, conditioned
scatter plot with marginal densities, box and stem with matching
theoretical distribution, and density with matching theoretical
distribution.

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/unit_tests
%{rlibdir}/%{packname}/INDEX