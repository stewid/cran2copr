%global packname  mlr3verse
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Easily Install and Load the 'mlr3' Package Family

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mlr3 
BuildRequires:    R-CRAN-mlr3filters 
BuildRequires:    R-CRAN-mlr3learners 
BuildRequires:    R-CRAN-mlr3pipelines 
BuildRequires:    R-CRAN-mlr3tuning 
BuildRequires:    R-CRAN-mlr3viz 
BuildRequires:    R-CRAN-paradox 
BuildRequires:    R-CRAN-mlr3data 
BuildRequires:    R-CRAN-mlr3misc 
Requires:         R-CRAN-mlr3 
Requires:         R-CRAN-mlr3filters 
Requires:         R-CRAN-mlr3learners 
Requires:         R-CRAN-mlr3pipelines 
Requires:         R-CRAN-mlr3tuning 
Requires:         R-CRAN-mlr3viz 
Requires:         R-CRAN-paradox 
Requires:         R-CRAN-mlr3data 
Requires:         R-CRAN-mlr3misc 

%description
The 'mlr3' package family is a set of packages for machine-learning
purposes built in a modular fashion. This wrapper package is aimed to
simplify the installation and loading of the core 'mlr3' packages. Get
more information about the 'mlr3' project at
<https://mlr3book.mlr-org.com/>.

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
