%global packname  RISCA
%global packver   0.8.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.2
Release:          3%{?dist}
Summary:          Causal Inference and Prediction in Cohort-Based Analyses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-relsurv 
BuildRequires:    R-CRAN-date 
BuildRequires:    R-graphics 
BuildRequires:    R-nlme 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-nnet 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-SuperLearner 
Requires:         R-splines 
Requires:         R-survival 
Requires:         R-CRAN-relsurv 
Requires:         R-CRAN-date 
Requires:         R-graphics 
Requires:         R-nlme 
Requires:         R-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-statmod 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-nnet 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-SuperLearner 

%description
We propose numerous functions for cohort-based analyses, either for
prediction or causal inference. For causal inference, it includes Inverse
Probability Weighting and G-computation for marginal estimation of an
exposure effect when confounders are expected. We deal with binary
outcomes, times-to-events (Le Borgne, 2016, <doi:10.1002/sim.6777>),
competing events (Trebern-Launay, 2018, <doi: 10.1007/s10654-017-0322-3>),
and multi-state data (Gillaizeau, 2018, <doi: 10.1002/sim.7550>). For
multistate data, semi-Markov model with interval censoring (Foucher, 2008,
<doi: 10.1177/0962280208093889>) may be considered and we propose the
possibility to consider the excess of mortality related to the disease
compared to reference lifetime tables (Gillaizeau, 2017, <doi:
10.1177/0962280215586456>). For predictive studies, we propose a set of
functions to estimate time-dependent receiver operating characteristic
(ROC) curves with the possible consideration of right-censoring
times-to-events or the presence of confounders (Le Borgne, 2018, <doi:
10.1177/0962280217702416>). Finally, several functions are available to
assess time-dependent ROC curves (Combescure, 2017, <doi:
10.1177/0962280212464542>) or survival curves (Combescure, 2014, <doi:
10.1002/sim.6111>) from aggregated data.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
