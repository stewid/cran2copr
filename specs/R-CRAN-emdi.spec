%global packname  emdi
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Estimating and Mapping Disaggregated Indicators

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-MuMIn 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-parallelMap 
BuildRequires:    R-CRAN-HLMdiag 
BuildRequires:    R-parallel 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-readODS 
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-CRAN-saeRobust 
BuildRequires:    R-CRAN-spdep 
Requires:         R-nlme 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-MuMIn 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-reshape2 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-parallelMap 
Requires:         R-CRAN-HLMdiag 
Requires:         R-parallel 
Requires:         R-boot 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-maptools 
Requires:         R-MASS 
Requires:         R-CRAN-readODS 
Requires:         R-CRAN-formula.tools 
Requires:         R-CRAN-saeRobust 
Requires:         R-CRAN-spdep 

%description
Functions that support estimating, assessing and mapping regional
disaggregated indicators. So far, estimation methods comprise direct
estimation, the model-based unit-level approach Empirical Best Prediction
(see "Small area estimation of poverty indicators" by Molina and Rao
(2010) <doi:10.1002/cjs.10051>), the area-level model (see "Estimates of
income for small places: An application of James-Stein procedures to
Census Data" by (Fay and Herriot 1979)
<doi:10.1080/01621459.1979.10482505>) and various extensions of it
(adjusted variance estimation methods, log and arcsin transformation,
spatial, robust and measurement error models), as well as their precision
estimates. The assessment of the used model is supported by a summary and
diagnostic plots. For a suitable presentation of estimates, map plots can
be easily created. Furthermore, results can easily be exported to excel.
For a detailed description of the package and the methods used see "The
{R} Package {emdi} for Estimating and Mapping Regionally Disaggregated
Indicators" by Kreutzmann et al. (2019) <doi:10.18637/jss.v091.i07>.

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
