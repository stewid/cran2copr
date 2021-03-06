%global packname  trade
%global packver   0.5.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.5
Release:          2%{?dist}
Summary:          Tools for Trade Practitioners

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-antitrust >= 0.99.11
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-antitrust >= 0.99.11
Requires:         R-methods 
Requires:         R-stats 

%description
A collection of tools for trade practitioners, including the ability to
calibrate different consumer demand systems and simulate the effects of
tariffs and quotas under different competitive regimes. These tools are
derived from Anderson et al. (2001) <doi:10.1016/S0047-2727(00)00085-2>
and Froeb et al. (2003) <doi:10.1016/S0304-4076(02)00166-5>.

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
