%global packname  dsm
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          3%{?dist}
Summary:          Density Surface Modelling of Distance Sampling Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mrds >= 2.1.16
BuildRequires:    R-mgcv >= 1.8.23
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-mrds >= 2.1.16
Requires:         R-mgcv >= 1.8.23
Requires:         R-CRAN-numDeriv 
Requires:         R-nlme 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-statmod 

%description
Density surface modelling of line transect data. A Generalized Additive
Model-based approach is used to calculate spatially-explicit estimates of
animal abundance from distance sampling (also presence/absence and strip
transect) data. Several utility functions are provided for model checking,
plotting and variance estimation.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
