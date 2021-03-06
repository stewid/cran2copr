%global packname  attachment
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Deal with Dependencies

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.3.1
BuildRequires:    R-CRAN-glue >= 1.3.0
BuildRequires:    R-CRAN-knitr >= 1.20
BuildRequires:    R-CRAN-desc >= 1.2.0
BuildRequires:    R-CRAN-rmarkdown >= 1.10
BuildRequires:    R-CRAN-roxygen2 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.3.1
Requires:         R-CRAN-glue >= 1.3.0
Requires:         R-CRAN-knitr >= 1.20
Requires:         R-CRAN-desc >= 1.2.0
Requires:         R-CRAN-rmarkdown >= 1.10
Requires:         R-CRAN-roxygen2 
Requires:         R-stats 
Requires:         R-utils 

%description
Tools to help manage dependencies during package development.  This can
retrieve all dependencies that are used in R files in the "R" directory,
in Rmd files in "vignettes" directory and in 'roxygen2' documentation of
functions. There is a function to update the Description file of your
package and a function to create a file with the R commands to install all
dependencies of your package. All functions to retrieve dependencies of R
scripts and Rmd files can be used independently of a package development.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/dependencies.R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/dummypackage
%{rlibdir}/%{packname}/INDEX
