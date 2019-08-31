%global packname  JQL
%global packver   2.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.3
Release:          1%{?dist}
Summary:          Jump Q-Learning for Individualized Interval-Valued Dose Rule

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-pdist 
BuildRequires:    R-stats 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-pdist 
Requires:         R-stats 

%description
We provide tools to estimate the individualized interval-valued dose rule
(I2DR) that maximizes the expected beneficial clinical outcome for each
individual and returns an optimal interval-valued dose, by using the jump
Q-learning method. The jump Q-learning method directly models the
conditional mean of the response given the dose level and the baseline
covariates via jump penalized least squares regression under the framework
of Q learning. We develop a searching algorithm by dynamic programming in
order to find the optimal I2DR with the time complexity O(n2) and spatial
complexity O(n). The outcome of interest includes the best partition of
the entire dosage of interest, the regression coefficients of each
partition, and the value function under the estimated I2DR as well as the
Wald-type confidence interval of value function constructed through the
Bootstrap.

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