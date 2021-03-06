%global packname  childsds
%global packver   0.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          3%{?dist}
Summary:          Data and Methods Around Reference Values in Pediatrics

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-boot 
BuildRequires:    R-class 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-purrrlyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-VGAM 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-tidyr 
Requires:         R-boot 
Requires:         R-class 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-purrrlyr 
Requires:         R-utils 
Requires:         R-CRAN-VGAM 

%description
Calculation of standard deviation scores and percentiles adduced from
different growth standards (WHO, UK, Germany, Italy, China, etc).
Therefore, the calculation of SDS-values for different measures like BMI,
weight, height, head circumference, different ratios, etc. are easy to
carry out. Also, references for laboratory values in children and adults
are available, e.g., serum lipids, iron-related blood parameters, IGF,
liver enzymes. In the new version, there are also functions combining the
lms() function from package 'gamlss' with resampling methods for using
with repeated measurements and family dependencies. A searchable list of
items can be found here: <https://github.com/mvogel78/childsds/wiki>.

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
%{rlibdir}/%{packname}/INDEX
