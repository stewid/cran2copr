%global packname  conf
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization and Analysis of Statistical Measures of Confidence

License:          GPL (<= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-CRAN-STAR 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-statmod 
Requires:         R-CRAN-STAR 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rootSolve 
Requires:         R-utils 

%description
Enables: (1) plotting two-dimensional confidence regions, (2) coverage
analysis of confidence region simulations and (3) calculating confidence
intervals and the associated actual coverage for binomial proportions.
Each is given in greater detail next. (1) Plots the two-dimensional
confidence region for probability distribution parameters (supported
distribution suffixes: cauchy, gamma, invgauss, logis, llogis, lnorm,
norm, unif, weibull) corresponding to a user-given complete or
right-censored dataset and level of significance.  The crplot() algorithm
plots more points in areas of greater curvature to ensure a smooth
appearance throughout the confidence region boundary.  An alternative
heuristic plots a specified number of points at roughly uniform intervals
along its boundary. Both heuristics build upon the radial profile
log-likelihood ratio technique for plotting confidence regions given by
Jaeger (2016) <doi:10.1080/00031305.2016.1182946>, and are detailed in a
publication by Weld (2019) <doi:10.1080/00031305.2018.1564696>. (2)
Performs confidence region coverage simulations for a random sample drawn
from a user- specified parametric population distribution, or for a
user-specified dataset and point of interest with coversim(). (3)
Calculates confidence interval bounds for a binomial proportion with
binomTest(), calculates the actual coverage with binomTestCoverage(), and
plots the actual coverage with binomTestCoveragePlot(). Calculates
confidence interval bounds for the binomial proportion using an ensemble
of constituent confidence intervals with binomTestEnsemble(). Calculates
confidence interval bounds for the binomial proportion using a complete
enumeration of all possible transitions from one actual coverage
acceptance curve to another which minimizes the root mean square error for
n <= 15 and follows the transitions for well-known confidence intervals
for n > 15 using binomTestMSE().

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
