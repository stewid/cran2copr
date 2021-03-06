%global packname  mlr3fselect
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Feature Selection for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate >= 2.0.0
BuildRequires:    R-CRAN-paradox >= 0.3.0
BuildRequires:    R-CRAN-bbotk >= 0.2.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lgr 
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-mlr3misc 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-checkmate >= 2.0.0
Requires:         R-CRAN-paradox >= 0.3.0
Requires:         R-CRAN-bbotk >= 0.2.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lgr 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-mlr3misc 
Requires:         R-CRAN-R6 

%description
Implements methods for feature selection with 'mlr3', e.g.  random search
and sequential selection. Various termination criteria can be set and
combined. The class 'AutoFSelect' provides a convenient way to perform
nested resampling in combination with 'mlr3'.

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
