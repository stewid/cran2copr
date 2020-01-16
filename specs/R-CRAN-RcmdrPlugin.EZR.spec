%global packname  RcmdrPlugin.EZR
%global packver   1.40
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.40
Release:          1%{?dist}
Summary:          R Commander Plug-in for the EZR (Easy R) Package

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rcmdr >= 2.4.0
BuildRequires:    R-CRAN-readstata13 
Requires:         R-CRAN-Rcmdr >= 2.4.0
Requires:         R-CRAN-readstata13 

%description
EZR (Easy R) adds a variety of statistical functions, including survival
analyses, ROC analyses, metaanalyses, sample size calculation, and so on,
to the R commander. EZR enables point-and-click easy access to statistical
functions, especially for medical statistics. EZR is platform-independent
and runs on Windows, Mac OS X, and UNIX. Its complete manual is available
only in Japanese (Chugai Igakusha, ISBN: 978-4-498-10901-8 or Nankodo,
ISBN: 978-4-524-26158-1), but an report that introduced the investigation
of EZR was published in Bone Marrow Transplantation (Nature Publishing
Group) as an Open article. This report can be used as a simple manual. It
can be freely downloaded from the journal website as shown below. This
report has been cited in more than 2,000 scientific articles.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/etc
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX