%global packname  modelStudio
%global packver   0.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Interactive Studio with Explanations for ML Predictive Models

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-iBreakDown >= 0.9.9
BuildRequires:    R-CRAN-ingredients >= 0.3.9
BuildRequires:    R-CRAN-r2d3 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-iBreakDown >= 0.9.9
Requires:         R-CRAN-ingredients >= 0.3.9
Requires:         R-CRAN-r2d3 
Requires:         R-CRAN-jsonlite 

%description
Automate explanation of machine learning predictive models. This package
generates advanced interactive and animated model explanations in the form
of serverless HTML site. It combines 'R' with 'D3.js' to produce plots and
descriptions for local and global explanations. The whole is greater than
the sum of its parts, so it also supports EDA (Exploratory Data Analysis)
on top of that. 'modelStudio' is a fast and condensed way to get all the
answers without much effort. Break down your model and look into its
ingredients with only a few lines of code.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/d3js
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX