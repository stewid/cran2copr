%global packname  latticeExtra
%global packver   0.6-28
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.28
Release:          1%{?dist}
Summary:          Extra Graphical Utilities Based on Lattice

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz

BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grid 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-lattice 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grid 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Building on the infrastructure provided by the lattice package, this
package provides several new high-level functions and methods, as well as
additional utilities such as panel and axis annotation functions.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/old.svnlog
%doc %{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/INDEX
