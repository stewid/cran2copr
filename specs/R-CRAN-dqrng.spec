%global packname  dqrng
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}
Summary:          Fast Pseudo Random Number Generators

License:          AGPL-3 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-CRAN-sitmo >= 2.0.0
BuildRequires:    R-CRAN-BH >= 1.64.0.1
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-Rcpp >= 0.12.16

%description
Several fast random number generators are provided as C++ header only
libraries: The PCG family by O'Neill (2014
<https://www.cs.hmc.edu/tr/hmc-cs-2014-0905.pdf>) as well as Xoroshiro128+
and Xoshiro256+ by Blackman and Vigna (2018 <arXiv:1805.01407>). In
addition fast functions for generating random numbers according to a
uniform, normal and exponential distribution are included. The latter two
use the Ziggurat algorithm originally proposed by Marsaglia and Tsang
(2000, <doi:10.18637/jss.v005.i08>). These functions are exported to R and
as a C++ interface and are enabled for use with the default 64 bit
generator from the PCG family, Xoroshiro128+ and Xoshiro256+ as well as
the 64 bit version of the 20 rounds Threefry engine (Salmon et al., 2011
<doi:10.1145/2063384.2063405>) as provided by the package 'sitmo'.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs