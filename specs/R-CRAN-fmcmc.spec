%global packname  fmcmc
%global packver   0.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          A friendly MCMC framework

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-coda 
Requires:         R-stats 
Requires:         R-methods 

%description
Provides a friendly (flexible) Markov Chain Monte Carlo (MCMC) framework
for implementing Metropolis-Hastings algorithm in a modular way allowing
users to specify automatic convergence checker, personalized transition
kernels, and out-of-the-box multiple MCMC chains using parallel computing.
Most of the methods implemented in this package can be found in Brooks et
al. (2011, ISBN 9781420079425).

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/INDEX