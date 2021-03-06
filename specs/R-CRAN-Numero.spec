%global packname  Numero
%global packver   1.6.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.0
Release:          2%{?dist}
Summary:          Statistical Framework to Define Subgroups in Complex Datasets

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.11.4
Requires:         R-CRAN-Rcpp >= 0.11.4

%description
High-dimensional datasets that do not exhibit a clear intrinsic clustered
structure pose a challenge to conventional clustering algorithms. For this
reason, we developed an unsupervised framework that helps scientists to
better subgroup their datasets based on visual cues, please see Gao S,
Mutter S, Casey A, Makinen V-P (2019) Numero: a statistical framework to
define multivariable subgroups in complex population-based datasets, Int J
Epidemiology, 48:369-37, <doi:10.1093/ije/dyy113>. The framework includes
the necessary functions to construct a self-organizing map of the data, to
evaluate the statistical significance of the observed data patterns, and
to visualize the results.

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

%files
%{rlibdir}/%{packname}
