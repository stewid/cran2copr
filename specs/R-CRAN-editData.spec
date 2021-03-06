%global packname  editData
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          'RStudio' Addin for Editing a 'data.frame'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rstudioapi >= 0.5
BuildRequires:    R-CRAN-shiny >= 0.13
BuildRequires:    R-CRAN-miniUI >= 0.1.1
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-rstudioapi >= 0.5
Requires:         R-CRAN-shiny >= 0.13
Requires:         R-CRAN-miniUI >= 0.1.1
Requires:         R-CRAN-DT 
Requires:         R-CRAN-tibble 

%description
An 'RStudio' addin for editing a 'data.frame' or a 'tibble'. You can
delete, add or update a 'data.frame' without coding. You can get resultant
data as a 'data.frame'. In the package, modularized 'shiny' app codes are
provided. These modules are intended for reuse across applications.

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
%doc %{rlibdir}/%{packname}/example
%doc %{rlibdir}/%{packname}/multipleData
%doc %{rlibdir}/%{packname}/multipleFiles
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
