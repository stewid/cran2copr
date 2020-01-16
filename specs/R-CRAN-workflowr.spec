%global packname  workflowr
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          A Framework for Reproducible and Collaborative Data Science

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc >= 1.12.3
BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 1.7
BuildRequires:    R-CRAN-fs >= 1.2.4
BuildRequires:    R-CRAN-knitr >= 1.18
BuildRequires:    R-CRAN-stringr >= 1.1.0
BuildRequires:    R-CRAN-rstudioapi >= 0.5
BuildRequires:    R-CRAN-callr 
BuildRequires:    R-CRAN-getPass 
BuildRequires:    R-CRAN-git2r 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rprojroot 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-whisker 
BuildRequires:    R-CRAN-yaml 
Requires:         R-CRAN-rmarkdown >= 1.7
Requires:         R-CRAN-fs >= 1.2.4
Requires:         R-CRAN-knitr >= 1.18
Requires:         R-CRAN-stringr >= 1.1.0
Requires:         R-CRAN-rstudioapi >= 0.5
Requires:         R-CRAN-callr 
Requires:         R-CRAN-getPass 
Requires:         R-CRAN-git2r 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-httr 
Requires:         R-methods 
Requires:         R-CRAN-rprojroot 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-whisker 
Requires:         R-CRAN-yaml 

%description
Provides a workflow for your analysis projects by combining literate
programming ('knitr' and 'rmarkdown') and version control ('Git', via
'git2r') to generate a website containing time-stamped, versioned, and
documented results.

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
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX