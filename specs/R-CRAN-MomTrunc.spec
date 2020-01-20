%global packname  MomTrunc
%global packver   5.63
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          5.63
Release:          1%{?dist}
Summary:          Moments of Folded and Doubly Truncated MultivariateDistributions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.14
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tlrmvnmvt 
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.14
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tlrmvnmvt 
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-tmvtnorm 

%description
It computes arbitrary products moments (mean vector and
variance-covariance matrix), for some double truncated (and folded)
multivariate distributions. These distributions belong to the family of
selection elliptical distributions, which includes well known skewed
distributions as the unified skew-t distribution (SUT) and its particular
cases as the extended skew-t (EST), skew-t (ST) and the symmetric
student-t (T) distribution. Analogous normal cases unified skew-normal
(SUN), extended skew-normal (ESN), skew-normal (SN), and symmetric normal
(N) are also included. Density, probabilities and random deviates are also
offered for these members. References used for this package:
Arellano-Valle, R. B. & Genton, M. G. (2005). On fundamental skew
distributions. Journal of Multivariate Analysis, 96, 93-116. Galarza C.E.,
Matos L.A., Dey D.K. & Lachos V.H. (2019) On Moments of Folded and
Truncated Multivariate Extended Skew-Normal Distributions. Technical
report. ID 19-14. University of Connecticut.
<https://stat.uconn.edu/tech-reports-2019/>.

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
%{rlibdir}/%{packname}/libs
