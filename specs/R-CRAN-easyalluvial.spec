%global packname  easyalluvial
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          3%{?dist}
Summary:          Generate Alluvial Plots with a Single Line of Code

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-ggalluvial >= 0.9.1
BuildRequires:    R-CRAN-recipes >= 0.1.5
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-ggridges 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-ggplot2 >= 3.2.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-ggalluvial >= 0.9.1
Requires:         R-CRAN-recipes >= 0.1.5
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-ggridges 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-e1071 

%description
Alluvial plots are similar to sankey diagrams and visualise categorical
data over multiple dimensions as flows. (Rosvall M, Bergstrom CT (2010)
Mapping Change in Large Networks. PLoS ONE 5(1): e8694.
<doi:10.1371/journal.pone.0008694> Their graphical grammar however is a
bit more complex then that of a regular x/y plots. The 'ggalluvial'
package made a great job of translating that grammar into 'ggplot2' syntax
and gives you many options to tweak the appearance of an alluvial plot,
however there still remains a multi-layered complexity that makes it
difficult to use 'ggalluvial' for explorative data analysis.
'easyalluvial' provides a simple interface to this package that allows you
to produce a decent alluvial plot from any dataframe in either long or
wide format from a single line of code while also handling continuous
data. It is meant to allow a quick visualisation of entire dataframes with
a focus on different colouring options that can make alluvial plots a
great tool for data exploration.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/logo
%{rlibdir}/%{packname}/INDEX
