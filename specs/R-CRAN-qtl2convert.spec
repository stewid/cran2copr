%global packname  qtl2convert
%global packver   0.22-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.22.7
Release:          2%{?dist}
Summary:          Convert Data among QTL Mapping Packages

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-qtl >= 1.40.8
BuildRequires:    R-CRAN-qtl2 >= 0.18
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-qtl >= 1.40.8
Requires:         R-CRAN-qtl2 >= 0.18
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-utils 
Requires:         R-stats 

%description
Functions to convert data structures among the 'qtl2', 'qtl', and 'DOQTL'
packages for mapping quantitative trait loci (QTL).

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
