%global packname  chinese.misc
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          3%{?dist}
Summary:          Miscellaneous Tools for Chinese Text Mining and More

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tm >= 0.7
BuildRequires:    R-CRAN-slam >= 0.1.37
BuildRequires:    R-CRAN-jiebaR 
BuildRequires:    R-CRAN-NLP 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-purrr 
Requires:         R-CRAN-tm >= 0.7
Requires:         R-CRAN-slam >= 0.1.37
Requires:         R-CRAN-jiebaR 
Requires:         R-CRAN-NLP 
Requires:         R-CRAN-stringi 
Requires:         R-Matrix 
Requires:         R-CRAN-purrr 

%description
Efforts are made to make Chinese text mining easier, faster, and robust to
errors. Document term matrix can be generated by only one line of code;
detecting encoding, segmenting and removing stop words are done
automatically. Some convenient tools are also supplied.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
