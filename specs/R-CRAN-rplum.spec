%global packname  rplum
%global packver   0.1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5.1
Release:          1%{?dist}
Summary:          Bayesian Age-Depth Modelling of Cores Dated by Pb-210

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-coda >= 0.19.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.12
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-coda >= 0.19.1
Requires:         R-CRAN-Rcpp >= 0.12.12
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
An approach to age-depth modelling that uses Bayesian statistics to
reconstruct accumulation histories for 210Pb-dated deposits using prior
information. It can combine 210Pb, radiocarbon, and other dates in the
chronologies. See Aquino et al. (2018) <doi:10.1007/s13253-018-0328-7>.
Note that parts of the code underlying 'rplum' are derived from the
'rbacon' package by the same authors. Subsequent versions of 'rplum' and
'rbacon' are planned to reduce duplication, with 'rplum' importing
'rbacon' instead.

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
