%global packname  implicitMeasures
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Computes the Scores for Different Implicit Measures

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-methods 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xtable 

%description
A tool for computing the scores for the Implicit Association Test (IAT;
Greenwald, McGhee & Schwartz (1998) <doi:10.1037/0022-3514.74.6.1464>) and
the Single Category-IAT (SC-IAT: Karpinski & Steinman (2006)
<doi:10.1037/0022-3514.91.1.16>). Functions for preparing the data (both
for the IAT and the SC-IAT), plotting the results, and obtaining a table
with the scores of implicit measures descriptive statistics are provided.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX