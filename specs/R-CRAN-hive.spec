%global packname  hive
%global packver   0.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Hadoop InteractiVE

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         hadoop-client >= 2.6.0
BuildRequires:    R-devel >= 2.9.0
Requires:         R-core >= 2.9.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rJava >= 0.9.3
BuildRequires:    R-methods 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-rJava >= 0.9.3
Requires:         R-methods 
Requires:         R-tools 
Requires:         R-CRAN-XML 

%description
Hadoop InteractiVE facilitates distributed computing via the MapReduce
paradigm through R and Hadoop. An easy to use interface to Hadoop, the
Hadoop Distributed File System (HDFS), and Hadoop Streaming is provided.

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/defaults
%{rlibdir}/%{packname}/INDEX