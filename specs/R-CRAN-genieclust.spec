%global packname  genieclust
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}
Summary:          The Genie++ Hierarchical Clustering Algorithm with Noise PointsDetection

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.4
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 1.0.4
Requires:         R-stats 
Requires:         R-utils 

%description
A retake on the Genie algorithm - a robust hierarchical clustering method
(Gagolewski, Bartoszuk, Cena, 2016 <DOI:10.1016/j.ins.2016.05.003>). Now
faster and more memory efficient; determining the whole hierarchy for
datasets of 10M points in low dimensional Euclidean spaces or 100K points
in high-dimensional ones takes only 1-2 minutes. Allows clustering with
respect to mutual reachability distances so that it can act as a noise
point detector or a robustified version of 'HDBSCAN*' (that is able to
detect a predefined number of clusters and hence it does not dependent on
the somewhat fragile 'eps' parameter). The package also features an
implementation of economic inequity indices (the Gini, Bonferroni index)
and external cluster validity measures (partition similarity scores; e.g.,
the adjusted Rand, Fowlkes-Mallows, adjusted mutual information, pair sets
index). See also the 'Python' version of 'genieclust' available on 'PyPI',
which supports sparse data, more metrics, and even larger datasets.

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
