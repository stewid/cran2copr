%global packname  GCalignR
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}
Summary:          Simple Peak Alignment for Gas-Chromatography Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-stringr 
Requires:         R-utils 
Requires:         R-CRAN-pbapply 

%description
Aligns peak based on peak retention times and matches homologous peaks
across samples. The underlying alignment procedure comprises three
sequential steps. (1) Full alignment of samples by linear transformation
of retention times to maximise similarity among homologous peaks (2)
Partial alignment of peaks within a user-defined retention time window to
cluster homologous peaks (3) Merging rows that are likely representing
homologous substances (i.e. no sample shows peaks in both rows and the
rows have similar retention time means). The algorithm is described in
detail in Ottensmann et al., 2018 <doi:10.1371/journal.pone.0198311>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
