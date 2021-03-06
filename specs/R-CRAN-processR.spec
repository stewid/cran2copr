%global packname  processR
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          Implementation of the 'PROCESS' Macro

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.1
BuildRequires:    R-CRAN-predict3d >= 0.1.3.3
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-diagram 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-officer 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rrtable 
BuildRequires:    R-CRAN-semTools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-interactions 
BuildRequires:    R-CRAN-ztable 
BuildRequires:    R-CRAN-rmarkdown 
Requires:         R-CRAN-ggplot2 >= 3.1.1
Requires:         R-CRAN-predict3d >= 0.1.3.3
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-diagram 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-officer 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rrtable 
Requires:         R-CRAN-semTools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-interactions 
Requires:         R-CRAN-ztable 
Requires:         R-CRAN-rmarkdown 

%description
Perform moderation, mediation, moderated mediation and moderated
moderation. Inspired from famous 'PROCESS' macro for 'SPSS' and 'SAS'
created by Andrew Hayes.

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

%files
%{rlibdir}/%{packname}
