%global packname  checkpoint
%global packver   0.4.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.9
Release:          3%{?dist}
Summary:          Install Packages from Snapshots on the Checkpoint Server forReproducibility

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-utils 
Requires:         R-utils 

%description
The goal of checkpoint is to solve the problem of package reproducibility
in R. Specifically, checkpoint allows you to install packages as they
existed on CRAN on a specific snapshot date as if you had a CRAN time
machine. To achieve reproducibility, the checkpoint() function installs
the packages required or called by your project and scripts to a local
library exactly as they existed at the specified point in time. Only those
packages are available to your project, thereby avoiding any package
updates that came later and may have altered your results. In this way,
anyone using checkpoint's checkpoint() can ensure the reproducibility of
your scripts or projects at any time. To create the snapshot archives,
once a day (at midnight UTC) Microsoft refreshes the Austria CRAN mirror
on the "Microsoft R Archived Network" server
(<https://mran.microsoft.com/>). Immediately after completion of the rsync
mirror process, the process takes a snapshot, thus creating the archive.
Snapshot archives exist starting from 2014-09-17.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/img
%{rlibdir}/%{packname}/INDEX
