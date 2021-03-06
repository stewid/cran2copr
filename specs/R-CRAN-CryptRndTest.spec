%global packname  CryptRndTest
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}
Summary:          Statistical Tests for Cryptographic Randomness

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MissMech 
BuildRequires:    R-CRAN-kSamples 
BuildRequires:    R-CRAN-sfsmisc 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-LambertW 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-tseries 
BuildRequires:    R-methods 
Requires:         R-CRAN-MissMech 
Requires:         R-CRAN-kSamples 
Requires:         R-CRAN-sfsmisc 
Requires:         R-CRAN-Rmpfr 
Requires:         R-parallel 
Requires:         R-CRAN-LambertW 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-tseries 
Requires:         R-methods 

%description
Performs cryptographic randomness tests on a sequence of random integers
or bits. Included tests are greatest common divisor, birthday spacings,
book stack, adaptive chi-square, topological binary, and three random walk
tests. Tests except greatest common divisor and birthday spacings are not
covered by standard test suites. In addition to the chi-square
goodness-of-fit test, results of Anderson-Darling, Kolmogorov-Smirnov, and
Jarque-Bera tests are also generated by some of the cryptographic
randomness tests.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
