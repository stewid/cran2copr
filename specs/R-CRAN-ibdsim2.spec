%global packname  ibdsim2
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Simulation of Chromosomal Regions Shared by Family Members

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ribd >= 1.1.0
BuildRequires:    R-CRAN-pedtools >= 0.9.4
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-ribd >= 1.1.0
Requires:         R-CRAN-pedtools >= 0.9.4
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glue 

%description
Simulation of segments shared identical-by-descent (IBD) by pedigree
members. Using sex specific recombination rates along the human genome
(Halldorsson et al. (2019) <doi:10.1126/science.aau1043>), phased
chromosomes are simulated for all pedigree members. Additional features
include calculation of realised IBD coefficients and plots of IBD segment
distributions.

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
