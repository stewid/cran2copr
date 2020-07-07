%global packname  HSAUR2
%global packver   1.1-17
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.17
Release:          3%{?dist}
Summary:          A Handbook of Statistical Analyses Using R (2nd Edition)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.2.0
Requires:         R-core >= 2.2.0
BuildArch:        noarch
BuildRequires:    R-tools 
Requires:         R-tools 

%description
Functions, data sets, analyses and examples from the second edition of the
book ''A Handbook of Statistical Analyses Using R'' (Brian S. Everitt and
Torsten Hothorn, Chapman & Hall/CRC, 2008). The first chapter of the book,
which is entitled ''An Introduction to R'', is completely included in this
package, for all other chapters, a vignette containing all data analyses
is available. In addition, the package contains Sweave code for producing
slides for selected chapters (see HSAUR2/inst/slides).

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
%doc %{rlibdir}/%{packname}/cache
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/LaTeXBibTeX
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/rawdata
%doc %{rlibdir}/%{packname}/slides
%{rlibdir}/%{packname}/INDEX
