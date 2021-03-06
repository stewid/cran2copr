%global packname  chillR
%global packver   0.70.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.70.24
Release:          3%{?dist}
Summary:          Statistical Methods for Phenology Analysis in Temperate FruitTrees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Kendall 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RMAWGEN 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-R.utils 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-pls 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Kendall 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-httr 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-RMAWGEN 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-R.utils 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 

%description
The phenology of plants (i.e. the timing of their annual life phases)
depends on climatic cues. For temperate trees and many other plants,
spring phases, such as leaf emergence and flowering, have been found to
result from the effects of both cool (chilling) conditions and heat. Fruit
tree scientists (pomologists) have developed some metrics to quantify
chilling and heat (e.g. see Luedeling (2012)
<doi.org/10.1016/j.scienta.2012.07.011>). 'chillR' contains functions for
processing temperature records into chilling (Chilling Hours, Utah Chill
Units and Chill Portions) and heat units (Growing Degree Hours). Regarding
chilling metrics, Chill Portions are often considered the most promising,
but they are difficult to calculate. This package makes it easy. 'chillR'
also contains procedures for conducting a PLS analysis relating
phenological dates (e.g. bloom dates) to either mean temperatures or mean
chill and heat accumulation rates, based on long-term weather and
phenology records (Luedeling and Gassner (2012)
<doi.org/10.1016/j.agrformet.2011.10.020>). As of version 0.65, it also
includes functions for generating weather scenarios with a weather
generator, for conducting climate change analyses for temperature-based
climatic metrics and for plotting results from such analyses. Since
version 0.70, 'chillR' contains a function for interpolating hourly
temperature records.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
