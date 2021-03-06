%global packname  beastier
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}
Summary:          Call 'BEAST2'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-beautier >= 2.3.5
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-assertive 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-beautier >= 2.3.5
Requires:         R-CRAN-ape 
Requires:         R-CRAN-assertive 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xml2 

%description
'BEAST2' (<https://www.beast2.org>) is a widely used Bayesian phylogenetic
tool, that uses DNA/RNA/protein data and many model priors to create a
posterior of jointly estimated phylogenies and parameters. 'BEAST2' is a
command-line tool. This package provides a way to call 'BEAST2' from an
'R' function call.

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
