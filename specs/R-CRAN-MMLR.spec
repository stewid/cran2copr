%global packname  MMLR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Fitting Markov-Modulated Linear Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-matlib 
Requires:         R-CRAN-matlib 

%description
A set of tools for fitting Markov-modulated linear regression, where
responses Y(t) are time-additive, and model operates in the external
environment, which is described as a continuous time Markov chain with
finite state space. Model is proposed by Alexander Andronov (2012)
<arXiv:1901.09600v1> and algorithm of parameters estimation is based on
eigenvalues and eigenvectors decomposition. Also, package will provide a
set of data simulation tools for Markov-modulated linear regression (for
academical/research purposes). Research project No. 1.1.1.2/VIAA/1/16/075.

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
%{rlibdir}/%{packname}/INDEX