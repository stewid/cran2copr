%global packname  RPESE
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Estimates of Standard Errors for Risk and Performance Measures

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RPEIF 
BuildRequires:    R-CRAN-RPEGLMEN 
BuildRequires:    R-CRAN-PerformanceAnalytics 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-sandwich 
Requires:         R-CRAN-RPEIF 
Requires:         R-CRAN-RPEGLMEN 
Requires:         R-CRAN-PerformanceAnalytics 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-robustbase 
Requires:         R-boot 
Requires:         R-CRAN-sandwich 

%description
Estimates of standard errors of popular risk and performance measures for
asset or portfolio returns using methods as described in Chen and Martin
(2019) <https://ssrn.com/abstract=3085672>.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX