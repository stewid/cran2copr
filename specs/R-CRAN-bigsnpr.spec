%global packname  bigsnpr
%global packver   1.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.4
Release:          2%{?dist}
Summary:          Analysis of Massive SNP Arrays

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildRequires:    R-CRAN-bigstatsr >= 1.2.2
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.600
BuildRequires:    R-CRAN-bigutilsr >= 0.3
BuildRequires:    R-CRAN-bigsparser >= 0.2.3
BuildRequires:    R-CRAN-bigassertr >= 0.1.3
BuildRequires:    R-CRAN-bigparallelr 
BuildRequires:    R-CRAN-bigreadr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rmio 
Requires:         R-CRAN-bigstatsr >= 1.2.2
Requires:         R-CRAN-bigutilsr >= 0.3
Requires:         R-CRAN-bigsparser >= 0.2.3
Requires:         R-CRAN-bigassertr >= 0.1.3
Requires:         R-CRAN-bigparallelr 
Requires:         R-CRAN-bigreadr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Easy-to-use, efficient, flexible and scalable tools for analyzing massive
SNP arrays <doi:10.1093/bioinformatics/bty185>.

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
