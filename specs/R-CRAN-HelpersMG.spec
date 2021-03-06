%global packname  HelpersMG
%global packver   4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Environmental Analyses, Ecotoxicology and Various RFunctions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-coda 

%description
Contains miscellaneous functions useful for managing 'NetCDF' files (see
<http://en.wikipedia.org/wiki/NetCDF>), get tide levels on any point of
the globe, get moon phase and time for sun rise and fall, analyse and
reconstruct periodic time series of temperature with irregular sinusoidal
pattern, show scales and wind rose in plot with change of color of text,
Metropolis-Hastings algorithm for Bayesian MCMC analysis, plot graphs or
boxplot with error bars, search files in disk by there names or their
content, read the contents of all files from a folder at one time.

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
