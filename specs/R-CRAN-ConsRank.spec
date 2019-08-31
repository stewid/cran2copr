%global packname  ConsRank
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Compute the Median Ranking(s) According to the Kemeny'sAxiomatic Approach

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-gtools 

%description
Compute the median ranking according to the Kemeny's axiomatic approach.
Rankings can or cannot contain ties, rankings can be both complete or
incomplete. The package contains both branch-and-bound algorithms and
heuristic solutions recently proposed. The package also provide some
useful utilities for deal with preference rankings. Essential references:
Emond, E.J., and Mason, D.W. (2002) <doi:10.1002/mcda.313>; D'Ambrosio,
A., Amodio, S., and Iorio, C. (2015) <doi:10.1285/i20705948v8n2p198>;
Amodio, S., D'Ambrosio, A., and Siciliano R. (2016)
<doi:10.1016/j.ejor.2015.08.048>; D'Ambrosio, A., Mazzeo, G., Iorio, C.,
and Siciliano, R. (2017) <doi:10.1016/j.cor.2017.01.017>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX