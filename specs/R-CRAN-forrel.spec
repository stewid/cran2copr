%global packname  forrel
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Forensic Pedigree Analysis and Relatedness Inference

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pedtools >= 0.9.3
BuildRequires:    R-CRAN-pedprobr 
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-pedmut 
Requires:         R-CRAN-pedtools >= 0.9.3
Requires:         R-CRAN-pedprobr 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-pedmut 

%description
Forensic applications of pedigree analysis, including likelihood ratios
for relationship testing, general relatedness inference, marker
simulation, and power analysis. General computation of exclusion powers is
based on Egeland et al. (2014) <doi:10.1016/j.fsigen.2013.05.001>. Several
functions deal specifically with family reunion cases, implementing and
developing ideas from Kling et al. (2017)
<doi:10.1016/j.fsigen.2017.08.006>. A novelty of 'forrel' is the ability
to model background inbreeding in forensic pedigree computations. This can
have significant impact in applications, as exemplified in Vigeland and
Egeland (2019) <doi:10.1016/j.fsigss.2019.10.175>. 'forrel' is part of the
ped suite, a collection of packages for pedigree analysis. In particular,
'forrel' imports 'pedtools' for creating and manipulating pedigrees and
markers, 'pedprobr' for likelihood computations, and 'pedmut' for mutation
modelling. Pedigree data may be created from scratch, or loaded from text
files. Data import from the 'Familias' software (Egeland et al. (2000)
<doi:10.1016/S0379-0738(00)00147-X>) is supported.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
