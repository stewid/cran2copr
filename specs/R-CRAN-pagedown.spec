%global packname  pagedown
%global packver   0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.10
Release:          3%{?dist}
Summary:          Paginate the HTML Output of R Markdown with CSS for Print

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc >= 2.0
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rmarkdown >= 1.16
BuildRequires:    R-CRAN-later >= 1.0.0
BuildRequires:    R-CRAN-bookdown >= 0.8
BuildRequires:    R-CRAN-servr >= 0.13
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-processx 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-websocket 
Requires:         R-CRAN-rmarkdown >= 1.16
Requires:         R-CRAN-later >= 1.0.0
Requires:         R-CRAN-bookdown >= 0.8
Requires:         R-CRAN-servr >= 0.13
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-processx 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-websocket 

%description
Use the paged media properties in CSS and the JavaScript library
'paged.js' to split the content of an HTML document into discrete pages.
Each page can have its page size, page numbers, margin boxes, and running
headers, etc. Applications of this package include books, letters,
reports, papers, business cards, resumes, and posters.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/resources
%doc %{rlibdir}/%{packname}/rmarkdown
%{rlibdir}/%{packname}/INDEX
