%global packname  MedSurvey
%global packver   1.1.1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1.1.0
Release:          1%{?dist}
Summary:          Mediation Analysis for Complex Surveys

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.50
Requires:         R-core >= 2.50
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-survey 
Requires:         R-CRAN-lavaan 
Requires:         R-parallel 

%description
It is a computer tool to conduct mediation analysis for complex surveys
using multi-stage sampling. Specifically, the mediation analysis method
using balanced repeated replications was proposed by Mai, Ha, and
Soulakova (2019) <DOI:10.1080/10705511.2018.1559065>. The development of
'MedSurvey' was sponsored by American Lebanese Syrian Associated Charities
(ALSAC). However, the contents of MedSurvey do not necessarily represent
the policy of the ALSAC.

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
%{rlibdir}/%{packname}/INDEX