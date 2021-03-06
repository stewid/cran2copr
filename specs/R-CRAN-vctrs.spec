%global packname  vctrs
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Vector Helpers

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-ellipsis >= 0.2.0
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-ellipsis >= 0.2.0
Requires:         R-CRAN-digest 
Requires:         R-CRAN-glue 

%description
Defines new notions of prototype and size that are used to provide tools
for consistent and well-founded type-coercion and size-recycling, and are
in turn connected to ideas of type- and size-stability useful for
analysing function interfaces.

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
