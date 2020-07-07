%global packname  ARHT
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}
Summary:          Adaptable Regularized Hotelling's T^2 Test for High-DimensionalData

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
Requires:         R-stats 

%description
Perform the Adaptable Regularized Hotelling's T^2 test (ARHT) proposed by
Li et al., (2016) <arXiv:1609.08725>. Both one-sample and two-sample mean
test are available with various probabilistic alternative prior models. It
contains a function to consistently estimate higher order moments of the
population covariance spectral distribution using the spectral of the
sample covariance matrix (Bai et al. (2010)
<doi:10.1111/j.1467-842X.2010.00590.x>). In addition, it contains a
function to sample from 3-variate chi-squared random vectors approximately
with a given correlation matrix when the degrees of freedom are large.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
