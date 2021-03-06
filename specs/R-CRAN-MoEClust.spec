%global packname  MoEClust
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          2%{?dist}
Summary:          Gaussian Parsimonious Clustering Models with Covariates and aNoise Component

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mclust >= 5.1
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-mvnfast 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-vcd 
Requires:         R-CRAN-mclust >= 5.1
Requires:         R-lattice 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-mvnfast 
Requires:         R-nnet 
Requires:         R-CRAN-vcd 

%description
Clustering via parsimonious Gaussian Mixtures of Experts using the
MoEClust models introduced by Murphy and Murphy (2019)
<doi:10.1007/s11634-019-00373-8>. This package fits finite Gaussian
mixture models with a formula interface for supplying gating and/or expert
network covariates using a range of parsimonious covariance
parameterisations from the GPCM family via the EM/CEM algorithm.
Visualisation of the results of such models using generalised pairs plots
and the inclusion of an additional noise component is also facilitated. A
greedy forward stepwise search algorithm is provided for identifying the
optimal model in terms of the number of components, the GPCM covariance
parameterisation, and the subsets of gating/expert network covariates.

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

%files
%{rlibdir}/%{packname}
