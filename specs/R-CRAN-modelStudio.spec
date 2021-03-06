%global packname  modelStudio
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Interactive Studio for Explanatory Model Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-iBreakDown >= 1.1.0
BuildRequires:    R-CRAN-ingredients >= 1.0.0
BuildRequires:    R-CRAN-r2d3 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-digest 
Requires:         R-CRAN-iBreakDown >= 1.1.0
Requires:         R-CRAN-ingredients >= 1.0.0
Requires:         R-CRAN-r2d3 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-digest 

%description
Automate the explanatory analysis of machine learning predictive models.
Generate advanced interactive and animated model explanations in the form
of a serverless HTML site with only one line of code. This tool is model
agnostic, therefore compatible with most of the black box predictive
models and frameworks. The main function computes various (instance and
dataset level) model explanations and produces an interactive,
customisable dashboard. It consists of multiple panels for plots with
their short descriptions. Easily save and share the dashboard with others.
Tools for model exploration unite with tools for Exploratory Data Analysis
to give a broad overview of the model behavior.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
