%global packname  workflows
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Modeling Workflows

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 2.0.0
BuildRequires:    R-CRAN-rlang >= 0.4.1
BuildRequires:    R-CRAN-ellipsis >= 0.2.0
BuildRequires:    R-CRAN-hardhat >= 0.1.4
BuildRequires:    R-CRAN-parsnip >= 0.1.3
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-glue 
Requires:         R-CRAN-cli >= 2.0.0
Requires:         R-CRAN-rlang >= 0.4.1
Requires:         R-CRAN-ellipsis >= 0.2.0
Requires:         R-CRAN-hardhat >= 0.1.4
Requires:         R-CRAN-parsnip >= 0.1.3
Requires:         R-CRAN-generics 
Requires:         R-CRAN-glue 

%description
Managing both a 'parsnip' model and a preprocessor, such as a model
formula or recipe from 'recipes', can often be challenging. The goal of
'workflows' is to streamline this process by bundling the model alongside
the preprocessor, all within the same object.

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
