%global packname  logmult
%global packver   0.7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.1
Release:          3%{?dist}
Summary:          Log-Multiplicative Models, Including Association Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gnm >= 1.0.5
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-qvcalc 
Requires:         R-CRAN-gnm >= 1.0.5
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-qvcalc 

%description
Functions to fit log-multiplicative models using 'gnm', with support for
convenient printing, plots, and jackknife/bootstrap standard errors. For
complex survey data, models can be fitted from design objects from the
'survey' package. Currently supported models include UNIDIFF (Erikson &
Goldthorpe), a.k.a. log-multiplicative layer effect model (Xie), and
several association models: Goodman's row-column association models of the
RC(M) and RC(M)-L families with one or several dimensions; two
skew-symmetric association models proposed by Yamaguchi and by van der
Heijden & Mooijaart. Functions allow computing the intrinsic association
coefficient (and therefore the Altham index), including via the Bayes
shrinkage estimator proposed by Zhou; and the RAS/IPF/Deming-Stephan
algorithm.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
