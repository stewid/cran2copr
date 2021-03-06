%global packname  Require
%global packver   0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Installing and Loading R Packages for Reproducible Workflows

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.table >= 1.10.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-utils 
Requires:         R-CRAN-data.table >= 1.10.4
Requires:         R-methods 
Requires:         R-CRAN-remotes 
Requires:         R-utils 

%description
A single key function, 'Require' that wraps 'install.packages',
'remotes::install_github', 'versions::install.versions', and
'base::require' that allows for reproducible workflows. As with other
functions in a reproducible workflow, this package emphasizes functions
that return the same result whether it is the first or subsequent times
running the function.

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
