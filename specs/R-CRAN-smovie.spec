%global packname  smovie
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          3%{?dist}
Summary:          Some Movies to Illustrate Concepts in Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rpanel >= 1.1.3
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-rpanel >= 1.1.3
Requires:         R-graphics 
Requires:         R-stats 

%description
Provides movies to help students to understand statistical concepts.  The
'rpanel' package <https://cran.r-project.org/package=rpanel> is used to
create interactive plots that move to illustrate key statistical ideas and
methods.  There are movies to: visualise probability distributions
(including user-supplied ones); illustrate sampling distributions of the
sample mean (central limit theorem), the median, the sample maximum
(extremal types theorem) and (the Fisher transformation of the) Pearson
product moment correlation coefficient; examine the influence of an
individual observation in simple linear regression; illustrate key
concepts in statistical hypothesis testing. Also provided are dpqr
functions for the distribution of the Fisher transformation of the
correlation coefficient under sampling from a bivariate normal
distribution.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
