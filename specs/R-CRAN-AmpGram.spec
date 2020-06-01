%global packname  AmpGram
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Prediction of Antimicrobial Peptides

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-biogram 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-stringi 
Requires:         R-CRAN-biogram 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-stringi 

%description
Predicts antimicrobial peptides using random forests trained on the n-gram
encoded peptides. The implemented algorithm can be accessed from both the
command line and shiny-based GUI. The AmpGram model is too large for CRAN
and it has to be downloaded separately from the repository:
<https://github.com/michbur/AmpGramModel>.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/AmpGram
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
