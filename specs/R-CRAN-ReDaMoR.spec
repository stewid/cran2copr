%global packname  ReDaMoR
%global packver   0.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          3%{?dist}
Summary:          Relational Data Modeler

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-visNetwork 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-colourpicker 
BuildRequires:    R-CRAN-rintrojs 
BuildRequires:    R-CRAN-markdown 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-visNetwork 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-colourpicker 
Requires:         R-CRAN-rintrojs 
Requires:         R-CRAN-markdown 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-igraph 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 

%description
The aim of this package is to manipulate relational data models in R. It
provides functions to create, modify and export data models in json
format. It also allows importing models created with 'MySQL Workbench'
(<https://www.mysql.com/products/workbench/>). These functions are
accessible through a graphical user interface made with 'shiny'.
Constraints such as types, keys, uniqueness and mandatory fields are
automatically checked and corrected when editing a model. Finally, real
data can be confronted to a model to check their compatibility.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/Documentation
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/www
%{rlibdir}/%{packname}/INDEX
