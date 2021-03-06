%global packname  MetaLandSim
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          3%{?dist}
Summary:          Landscape and Range Expansion Simulation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-fgui 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-googleVis 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-rgrass7 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-zipfR 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-knitr 
Requires:         R-tcltk 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-fgui 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-googleVis 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-rgrass7 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-spatstat 
Requires:         R-stats 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-zipfR 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-knitr 

%description
Tools to generate random landscape graphs, evaluate species occurrence in
dynamic landscapes, simulate future landscape occupation and evaluate
range expansion when new empty patches are available (e.g. as a result of
climate change).

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/logo
%{rlibdir}/%{packname}/INDEX
