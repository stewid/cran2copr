%global packname  natmanager
%global packver   0.4.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.6
Release:          2%{?dist}
Summary:          Install the 'Natverse' Packages from Scratch

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-gh 
Requires:         R-utils 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-withr 

%description
Provides streamlined installation for packages from the 'natverse', a
suite of R packages for computational neuroanatomy built on top of the
'nat' 'NeuroAnatomy Toolbox' package. Installation of the complete
'natverse' suite requires a 'GitHub' user account and personal access
token 'GITHUB_PAT'. 'natmanager' will help the end user set this up if
necessary.

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
