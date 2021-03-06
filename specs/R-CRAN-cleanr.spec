%global packname  cleanr
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          3%{?dist}
Summary:          Helps You to Code Cleaner

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-pkgload 
BuildRequires:    R-CRAN-rprojroot 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-pkgload 
Requires:         R-CRAN-rprojroot 

%description
Check your R code for some of the most common layout flaws.  Many tried to
teach us how to write code less dreadful, be it implicitly as B. W.
Kernighan and D. M. Ritchie (1988) <ISBN:0-13-110362-8> in 'The C
Programming Language' did, be it explicitly as R.C. Martin (2008)
<ISBN:0-13-235088-2> in 'Clean Code: A Handbook of Agile Software
Craftsmanship' did.  So we should check our code for files too long or
wide, functions with too many lines, too wide lines, too many arguments or
too many levels of nesting. Note: This is not a static code analyzer like
pylint or the like. Checkout <https://cran.r-project.org/package=lintr>
instead.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/runit_tests
%doc %{rlibdir}/%{packname}/source
%{rlibdir}/%{packname}/INDEX
