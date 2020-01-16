%global packname  textrecipes
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Extra 'Recipes' for Text Processing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-textfeatures >= 0.3.3
BuildRequires:    R-CRAN-recipes >= 0.1.4
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-SnowballC 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-text2vec 
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-textfeatures >= 0.3.3
Requires:         R-CRAN-recipes >= 0.1.4
Requires:         R-CRAN-generics 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-SnowballC 
Requires:         R-CRAN-stopwords 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-text2vec 
Requires:         R-CRAN-lifecycle 

%description
Converting text to numerical features requires specifically created
procedures, which are implemented as steps according to the 'recipes'
package. These steps allows for tokenization, filtering, counting (tf and
tfidf) and feature hashing.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX