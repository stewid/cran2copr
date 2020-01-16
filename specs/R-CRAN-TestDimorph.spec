%global packname  TestDimorph
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Analysis Of The Interpopulation Difference In Degree of SexualDimorphism Using Summary Statistics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-rowr 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-klaR 
BuildRequires:    R-CRAN-mda 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-rowr 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-rlang 
Requires:         R-MASS 
Requires:         R-CRAN-klaR 
Requires:         R-CRAN-mda 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-stringr 

%description
Provides two approaches of comparison; the univariate and the multivariate
analysis in two or more populations. Since the main obstacle of performing
systematic comparisons in anthropological studies is the absence of raw
data, the current package offer a solution for this problem by allowing
the use of published summary statistics of metric data (mean, standard
deviation and sex specific sample size) as illustrated by the works of
Greene, D. L. (1989) <doi:10.1002/ajpa.1330790113> and Konigsberg, L. W.
(1991) <doi:10.1002/ajpa.1330840110>.

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
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX