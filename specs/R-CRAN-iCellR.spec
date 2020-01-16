%global packname  iCellR
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Analyzing High-Throughput Single Cell Sequencing Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-NbClust 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-CRAN-pheatmap 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-methods 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-Matrix 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-NbClust 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-umap 
Requires:         R-CRAN-pheatmap 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-ggdendro 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-methods 

%description
A toolkit that allows scientists to work with data from single cell
sequencing technologies such as scRNA-seq, scVDJ-seq and CITE-Seq. Single
(i) Cell R package ('iCellR') provides unprecedented flexibility at every
step of the analysis pipeline, including normalization, clustering,
dimensionality reduction, imputation, visualization, and so on. Users can
design both unsupervised and supervised models to best suit their
research. In addition, the toolkit provides 2D and 3D interactive
visualizations, differential expression analysis, filters based on cells,
genes and clusters, data merging, normalizing for dropouts, data
imputation methods, correcting for batch differences, pathway analysis,
tools to find marker genes for clusters and conditions, predict cell types
and pseudotime analysis.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX