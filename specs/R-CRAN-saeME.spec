%global packname  saeME
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Small Area Estimation with Measurement Error

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
Requires:         R-CRAN-expm 
Requires:         R-MASS 
Requires:         R-stats 
Requires:         R-CRAN-dplyr 

%description
A set of functions and datasets implementation of small area estimation
when auxiliary variable is measured with error. These functions provide a
empirical best linear unbiased prediction (EBLUP) estimator and mean
squared error (MSE) estimator of the EBLUP. These models were developed by
Ybarra and Lohr (2008) <doi:10.1093/biomet/asn048>.

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
