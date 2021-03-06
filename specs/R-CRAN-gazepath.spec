%global packname  gazepath
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}
Summary:          Parse Eye-Tracking Data into Fixations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-shiny 

%description
Eye-tracking data must be transformed into fixations and saccades before
it can be analyzed. This package provides a non-parametric speed-based
approach to do this on a trial basis. The method is especially useful when
there are large differences in data quality, as the thresholds are
adjusted accordingly. The same pre-processing procedure can be applied to
all participants, while accounting for individual differences in data
quality.

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
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
