%global packname  updog
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}
Summary:          Flexible Genotyping for Polyploids

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggthemes 
BuildRequires:    R-CRAN-reshape2 
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggthemes 
Requires:         R-CRAN-reshape2 

%description
Implements empirical Bayes approaches to genotype polyploids from next
generation sequencing data while accounting for allele bias,
overdispersion, and sequencing error. The main functions are flexdog() and
multidog(), which allow the specification of many different genotype
distributions. Also provided are functions to simulate genotypes, rgeno(),
and read-counts, rflexdog(), as well as functions to calculate oracle
genotyping error rates, oracle_mis(), and correlation with the true
genotypes, oracle_cor(). These latter two functions are useful for read
depth calculations. Run browseVignettes(package = "updog") in R for
example usage. See Gerard et al. (2018) <doi:10.1534/genetics.118.301468>
and Gerard and Ferrao (2020) <doi:10.1093/bioinformatics/btz852> for
details on the implemented methods.

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
