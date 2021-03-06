%global packname  umx
%global packver   4.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0.0
Release:          2%{?dist}
Summary:          Structural Equation and Twin Modeling in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-OpenMx >= 2.11.5
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-DiagrammeR 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-CRAN-R2HTML 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-OpenMx >= 2.11.5
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-DiagrammeR 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-mvtnorm 
Requires:         R-nlme 
Requires:         R-CRAN-polycor 
Requires:         R-CRAN-R2HTML 
Requires:         R-CRAN-RCurl 
Requires:         R-utils 
Requires:         R-CRAN-xtable 

%description
Quickly create, run, and report structural equation and twin models. See
'?umx' for help, and umx_open_CRAN_page("umx") for NEWS.

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
