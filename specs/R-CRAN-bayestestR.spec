%global packname  bayestestR
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}
Summary:          Understand and Describe Bayesian Models and PosteriorDistributions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-insight >= 0.8.4
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-insight >= 0.8.4
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides utilities to describe posterior distributions and Bayesian
models. It includes point-estimates such as Maximum A Posteriori (MAP),
measures of dispersion (Highest Density Interval - HDI; Kruschke, 2015
<doi:10.1016/C2012-0-00477-2>) and indices used for null-hypothesis
testing (such as ROPE percentage, pd and Bayes factors).

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
