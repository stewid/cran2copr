%global packname  graph4lg
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Build Graphs for Landscape Genetics Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-CRAN-ade4 
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pegas 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-doBy 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Imap 
BuildRequires:    R-CRAN-diveRsity 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ecodist 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-adegenet 
Requires:         R-CRAN-ade4 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-vegan 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-pegas 
Requires:         R-CRAN-Rdpack 
Requires:         R-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-doBy 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Imap 
Requires:         R-CRAN-diveRsity 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ecodist 

%description
Build graphs for landscape genetics analysis. This set of functions can be
used to import and convert spatial and genetic data initially in different
formats, import landscape graphs created with 'GRAPHAB' software (Foltete
et al., 2012) <doi:10.1016/j.envsoft.2012.07.002>, make diagnosis plots of
isolation by distance relationships in order to choose how to build
genetic graphs, create graphs with a large range of pruning methods,
weight their links with several genetic distances, plot and analyse
graphs, compare them with other graphs. It uses functions from other
packages such as 'adegenet' (Jombart, 2008)
<doi:10.1093/bioinformatics/btn129> and 'igraph' (Csardi et Nepusz, 2006)
<https://bit.ly/2028mcO>. It also implements methods commonly used in
landscape genetics to create graphs, described by Dyer et Nason (2004)
<doi:10.1111/j.1365-294X.2004.02177.x> and Greenbaum et Fefferman (2017)
<doi:10.1111/mec.14059>, and to analyse distance data (van Strien et al.,
2015) <doi:10.1038/hdy.2014.62>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX