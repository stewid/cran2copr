%global packname  cutpointr
%global packver   0.7.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.6
Release:          1%{?dist}
Summary:          Determine and Evaluate Optimal Cutpoints in BinaryClassification Tasks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-gridExtra >= 2.2.1
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-CRAN-tibble >= 2.1.1
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-tidyr >= 0.6.0
BuildRequires:    R-CRAN-dplyr >= 0.5.0
BuildRequires:    R-CRAN-purrr >= 0.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-CRAN-rlang >= 0.1.2
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-gridExtra >= 2.2.1
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-CRAN-tibble >= 2.1.1
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-tidyr >= 0.6.0
Requires:         R-CRAN-dplyr >= 0.5.0
Requires:         R-CRAN-purrr >= 0.2.2
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-CRAN-rlang >= 0.1.2
Requires:         R-stats 
Requires:         R-utils 

%description
Estimate cutpoints that optimize a specified metric in binary
classification tasks and validate performance using bootstrapping. Some
methods for more robust cutpoint estimation and various plotting functions
are included.

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
%{rlibdir}/%{packname}/libs