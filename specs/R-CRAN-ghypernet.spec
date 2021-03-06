%global packname  ghypernet
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          3%{?dist}
Summary:          Fit and Simulate Generalised Hypergeometric Ensembles of Graphs

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rootSolve 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rootSolve 

%description
Provides functions for model fitting and selection of generalised
hypergeometric ensembles of random graphs (gHypEG). To learn how to use
it, check the vignettes for a quick tutorial. Please reference its use as
Casiraghi, G., Nanumyan, V. (2019) <doi:10.5281/zenodo.2555300> together
with those relevant references from the one listed below. The package is
based on the research developed at the Chair of Systems Design, ETH
Zurich. Casiraghi, G., Nanumyan, V., Scholtes, I., Schweitzer, F. (2016)
<arXiv:1607.02441>. Casiraghi, G., Nanumyan, V., Scholtes, I., Schweitzer,
F. (2017) <doi:10.1007/978-3-319-67256-4_11>. Casiraghi, G., (2017)
<arxiv:1702.02048> Casiraghi, G., Nanumyan, V. (2018) <arXiv:1810.06495>.
Brandenberger, L., Casiraghi, G., Nanumyan, V., Schweitzer, F. (2019)
<doi:10.1145/3341161.3342926> Casiraghi, G. (2019)
<doi:10.1007/s41109-019-0241-1>.

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
%{rlibdir}/%{packname}/INDEX
