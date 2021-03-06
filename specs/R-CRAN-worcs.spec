%global packname  worcs
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Workflow for Open Reproducible Code in Science

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-prereg 
BuildRequires:    R-CRAN-gert 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-rticles 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-prereg 
Requires:         R-CRAN-gert 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-rticles 

%description
Create reproducible and transparent research projects in 'R', with a
minimal amount of code. This package is based on the Workflow for Open
Reproducible Code in Science (WORCS), a step-by-step procedure based on
best practices for Open Science. It includes an 'RStudio' project
template, several convenience functions, and all dependencies required to
make your project reproducible and transparent. WORCS is explained in the
tutorial paper by Van Lissa, Brandmaier, Brinkman, Lamprecht, Struiksma, &
Vreede (2020). <doi:10.17605/OSF.IO/ZCVBS>.

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
