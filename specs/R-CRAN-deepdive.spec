%global packname  deepdive
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Deep Learning for General Purpose

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-rpart 
BuildRequires:    R-CRAN-treeClust 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-plyr 
Requires:         R-rpart 
Requires:         R-CRAN-treeClust 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 

%description
Aims to provide simple intuitive functions to create quick prototypes of
artificial neural network or deep learning models. In addition novel
ensemble models like 'deeptree' and 'deepforest' has been included which
combines decision trees and neural network.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
