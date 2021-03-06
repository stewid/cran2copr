%global packname  meta
%global packver   4.13-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.13.0
Release:          2%{?dist}
Summary:          General Package for Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-metafor >= 2.1.0
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-CompQuadForm 
Requires:         R-CRAN-metafor >= 2.1.0
Requires:         R-grid 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-CompQuadForm 

%description
User-friendly general package providing standard methods for meta-analysis
and supporting Schwarzer, Carpenter, and Rücker
<DOI:10.1007/978-3-319-21416-0>, "Meta-Analysis with R" (2015): - fixed
effect and random effects meta-analysis; - several plots (forest, funnel,
Galbraith / radial, L'Abbe, Baujat, bubble); - statistical tests and
trim-and-fill method to evaluate bias in meta-analysis; - import data from
'RevMan 5'; - prediction interval, Hartung-Knapp method for random effects
model; - cumulative meta-analysis and leave-one-out meta-analysis; -
meta-regression; - generalised linear mixed models; - produce forest plot
summarising several (subgroup) meta-analyses.

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
