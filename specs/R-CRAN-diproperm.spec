%global packname  diproperm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conduct Direction-Projection-Permutation Tests and Display Plots

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lemon 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-DWDLargeR 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-CRAN-sampling 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lemon 
Requires:         R-CRAN-gridExtra 
Requires:         R-parallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-DWDLargeR 
Requires:         R-Matrix 
Requires:         R-CRAN-SparseM 
Requires:         R-CRAN-sampling 

%description
Conducts a direction-projection-permutation test and displays several key
plots to facilitate the visual assessment of the test. See Wei et. al
(2016) <doi:10.1080/10618600.2015.1027773> and Lam et. al (2018)
<doi:10.1080/10618600.2017.1366915> for more details.

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
