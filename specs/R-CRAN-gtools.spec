%global packname  gtools
%global packver   3.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.8.2
Release:          3%{?dist}
Summary:          Various R Programming Tools

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions to assist in R programming, including: - assist in developing,
updating, and maintaining R and R packages ('ask', 'checkRVersion',
'getDependencies', 'keywords', 'scat'), - calculate the logit and inverse
logit transformations ('logit', 'inv.logit'), - test if a value is
missing, empty or contains only NA and NULL values ('invalid'), -
manipulate R's .Last function ('addLast'), - define macros ('defmacro'), -
detect odd and even integers ('odd', 'even'), - convert strings containing
non-ASCII characters (like single quotes) to plain ASCII ('ASCIIfy'), -
perform a binary search ('binsearch'), - sort strings containing both
numeric and character components ('mixedsort'), - create a factor variable
from the quantiles of a continuous variable ('quantcut'), - enumerate
permutations and combinations ('combinations', 'permutation'), - calculate
and convert between fold-change and log-ratio ('foldchange',
'logratio2foldchange', 'foldchange2logratio'), - calculate probabilities
and generate random numbers from Dirichlet distributions ('rdirichlet',
'ddirichlet'), - apply a function over adjacent subsets of a vector
('running'), - modify the TCP_NODELAY ('de-Nagle') flag for socket
objects, - efficient 'rbind' of data frames, even if the column names
don't match ('smartbind'), - generate significance stars from p-values
('stars.pval'), - convert characters to/from ASCII codes ('asc', 'chr'), -
convert character vector to ASCII representation ('ASCIIfy').

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
