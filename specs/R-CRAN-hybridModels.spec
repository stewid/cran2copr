%global packname  hybridModels
%global packver   0.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Stochastic Hybrid Models in Dynamic Networks

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-GillespieSSA 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-grid 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-GillespieSSA 
Requires:         R-parallel 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-grid 

%description
Simulates stochastic hybrid models for transmission of infectious diseases
in dynamic networks. It is a metapopulation model in which each node in
the network is a sub-population and disease spreads within nodes and among
them, combining two approaches: stochastic simulation algorithm or its
approximations (Gillespie DT (2007)
<doi:10.1146/annurev.physchem.58.032806.104637>) and individual-based
approach, respectively. Movement among nodes are data based and can be
irregular. Equations that models spread within nodes are customizable and
there are two link types among nodes: migration and influence (commuting).

%prep
%setup -q -c -n %{packname}


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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX