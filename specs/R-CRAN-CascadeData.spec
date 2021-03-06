%global packname  CascadeData
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          3%{?dist}
Summary:          Experimental Data of Cascade Experiments in Genomics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
These experimental expression data (5 leukemic 'CLL' B-lymphocyte of
aggressive form from 'GSE39411', <doi:10.1073/pnas.1211130110>), after
B-cell receptor stimulation, are used as examples by packages such as the
'Cascade' one, a modeling tool allowing gene selection, reverse
engineering, and prediction in cascade networks. Jung, N., Bertrand, F.,
Bahram, S., Vallat, L., and Maumy-Bertrand, M. (2014)
<doi:10.1093/bioinformatics/btt705>.

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
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NEWS.md
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
