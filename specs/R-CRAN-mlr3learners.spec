%global packname  mlr3learners
%global packver   0.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Recommended Learners for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr3 >= 0.5.0
BuildRequires:    R-CRAN-mlr3misc >= 0.5.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-mlr3 >= 0.5.0
Requires:         R-CRAN-mlr3misc >= 0.5.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-R6 

%description
Recommended Learners for 'mlr3'. Extends 'mlr3' and 'mlr3proba' with
interfaces to essential machine learning packages on CRAN.  This includes,
but is not limited to: (penalized) linear and logistic regression, linear
and quadratic discriminant analysis, k-nearest neighbors, naive Bayes,
support vector machines, and gradient boosting.

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
