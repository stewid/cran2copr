%global packname  bnviewer
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          3%{?dist}
Summary:          Interactive Visualization of Bayesian Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildArch:        noarch
BuildRequires:    R-CRAN-bnlearn >= 4.3
BuildRequires:    R-CRAN-visNetwork >= 2.0.4
BuildRequires:    R-CRAN-igraph >= 1.2.4
BuildRequires:    R-methods 
Requires:         R-CRAN-bnlearn >= 4.3
Requires:         R-CRAN-visNetwork >= 2.0.4
Requires:         R-CRAN-igraph >= 1.2.4
Requires:         R-methods 

%description
Bayesian networks provide an intuitive framework for probabilistic
reasoning and its graphical nature can be interpreted quite clearly. Graph
based methods of machine learning are becoming more popular because they
offer a richer model of knowledge that can be understood by a human in a
graphical format. The 'bnviewer' is an R Package that allows the
interactive visualization of Bayesian Networks. The aim of this package is
to improve the Bayesian Networks visualization over the basic and static
views offered by existing packages.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
