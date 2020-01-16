%global packname  Rquefts
%global packver   1.0-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Quantitative Evaluation of the Native Fertility of TropicalSoils

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-meteor 
BuildRequires:    R-methods 
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-meteor 
Requires:         R-methods 

%description
An implementation of the QUEFTS (Quantitative Evaluation of the Native
Fertility of Tropical Soils) model. The model estimates nutrient
requirements for crops to achieve a target yield given native soil
fertility, as estimated from a few soil chemical properties. See Janssen
et al. (1990) <doi:10.1016/0016-7061(90)90021-Z> for the technical details
and Sattari et al. (2014) <doi:10.1016/j.fcr.2013.12.005> for a recent
evaluation.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs