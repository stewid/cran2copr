%global packname  IsoplotR
%global packver   3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4
Release:          2%{?dist}
Summary:          Statistical Toolbox for Radiometric Geochronology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-grDevices 
Requires:         R-MASS 
Requires:         R-grDevices 

%description
Plots U-Pb data on Wetherill and Tera-Wasserburg concordia diagrams.
Calculates concordia and discordia ages. Performs linear regression of
measurements with correlated errors using 'York', 'Titterington' and
'Ludwig' approaches. Generates Kernel Density Estimates (KDEs) and
Cumulative Age Distributions (CADs). Produces Multidimensional Scaling
(MDS) configurations and Shepard plots of multi-sample detrital datasets
using the Kolmogorov-Smirnov distance as a dissimilarity measure.
Calculates 40Ar/39Ar ages, isochrons, and age spectra. Computes weighted
means accounting for overdispersion. Calculates U-Th-He (single grain and
central) ages, logratio plots and ternary diagrams. Processes fission
track data using the external detector method and LA-ICP-MS, calculates
central ages and plots fission track and other data on radial (a.k.a.
'Galbraith') plots. Constructs total Pb-U, Pb-Pb, Th-Pb, K-Ca, Re-Os,
Sm-Nd, Lu-Hf, Rb-Sr and 230Th-U isochrons as well as 230Th-U evolution
plots.

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
