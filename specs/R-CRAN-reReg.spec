%global packname  reReg
%global packver   1.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Recurrent Event Regression

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-SQUAREM 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-BB 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-SQUAREM 
Requires:         R-survival 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-tibble 

%description
A collection of regression models for recurrent event process and failure
time data. Available methods include these from Xu et al. (2017)
<doi:10.1080/01621459.2016.1173557>, Lin et al. (2000)
<doi:10.1111/1467-9868.00259>, Wang et al. (2001)
<doi:10.1198/016214501753209031>, Ghosh and Lin (2003)
<doi:10.1111/j.0006-341X.2003.00102.x>, and Huang and Wang (2004)
<doi:10.1198/016214504000001033>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs