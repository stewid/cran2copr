%global packname  OCNet
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Optimal Channel Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-spam 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-SSN 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-spam 
Requires:         R-CRAN-rgl 
Requires:         R-methods 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-SSN 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sp 

%description
Generate and analyze Optimal Channel Networks (OCNs): oriented spanning
trees reproducing all scaling features characteristic of real, natural
river networks. As such, they can be used in a variety of numerical
experiments in the fields of hydrology, ecology and epidemiology. See
Carraro et al. (2020) <doi:10.1002/ece3.6479> for a presentation of the
package; Rinaldo et al. (2014) <doi:10.1073/pnas.1322700111> for a
theoretical overview on the OCN concept; Furrer and Sain (2010)
<doi:10.18637/jss.v036.i10> for the construct used.

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
