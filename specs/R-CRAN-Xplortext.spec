%global packname  Xplortext
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Statistical Analysis of Textual Data

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-FactoMineR >= 1.36
BuildRequires:    R-CRAN-tm >= 0.7.3
BuildRequires:    R-CRAN-ggdendro 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-flexclust 
BuildRequires:    R-CRAN-flashClust 
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-FactoMineR >= 1.36
Requires:         R-CRAN-tm >= 0.7.3
Requires:         R-CRAN-ggdendro 
Requires:         R-graphics 
Requires:         R-CRAN-gridExtra 
Requires:         R-MASS 
Requires:         R-methods 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-slam 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-flexclust 
Requires:         R-CRAN-flashClust 

%description
Provides a set of functions devoted to multivariate exploratory statistics
on textual data. Classical methods such as correspondence analysis and
agglomerative hierarchical clustering are available. Chronologically
constrained agglomerative hierarchical clustering enriched with
labelled-by-words trees is offered. Given a division of the corpus into
parts, their characteristic words and documents are identified. Further,
accessing to 'FactoMineR' functions is very easy. Two of them are relevant
in textual domain. MFA() addresses multiple lexical table allowing
applications such as dealing with multilingual corpora as well as
simultaneously analyzing both open-ended and closed questions in surveys.
See <http://www.xplortext.org> for examples.

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
%doc %{rlibdir}/%{packname}/Xplortext.pdf
%{rlibdir}/%{packname}/INDEX