%global packname  dae
%global packver   3.1-27
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.27
Release:          1%{?dist}
Summary:          Functions Useful in the Design and ANOVA of Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-stats 

%description
The content falls into the following groupings: (i) Data, (ii) Factor
manipulation functions, (iii) Design functions, (iv) ANOVA functions, (v)
Matrix functions, (vi) Projector and canonical efficiency functions, and
(vii) Miscellaneous functions. There is a vignette describing how to use
the design functions for randomizing and assessing designs available as a
vignette called 'DesignNotes'. The ANOVA functions facilitate the
extraction of information when the 'Error' function has been used in the
call to 'aov'. The package 'dae' can also be installed from
<http://chris.brien.name/rpackages/>.

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
