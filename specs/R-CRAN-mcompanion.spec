%global packname  mcompanion
%global packver   0.4-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.5
Release:          1%{?dist}
Summary:          Objects and Methods for Multi-Companion Matrices

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-gbutils 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-Rdpack 
Requires:         R-methods 
Requires:         R-Matrix 
Requires:         R-CRAN-gbutils 
Requires:         R-MASS 
Requires:         R-CRAN-Rdpack 

%description
Provides a class for multi-companion matrices with methods for arithmetic
and factorization.  A method for generation of multi-companion matrices
with prespecified spectral properties is provided, as well as some
utilities for periodically correlated and multivariate time series models.
See Boshnakov (2002) <doi:10.1016/j.laa.2007.02.010> and Boshnakov &
Iqelan (2009) <doi:10.1111/j.1467-9892.2009.00617.x>.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX