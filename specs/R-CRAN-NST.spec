%global packname  NST
%global packver   2.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.4
Release:          3%{?dist}
Summary:          Normalized Stochasticity Ratio

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-permute 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-vegan 
Requires:         R-parallel 
Requires:         R-CRAN-permute 
Requires:         R-CRAN-ape 

%description
To estimate ecological stochasticity in community assembly. Understanding
the community assembly mechanisms controlling biodiversity patterns is a
central issue in ecology. Although it is generally accepted that both
deterministic and stochastic processes play important roles in community
assembly, quantifying their relative importance is challenging. The new
index, normalized stochasticity ratio (NST), is to estimate ecological
stochasticity, i.e. relative importance of stochastic processes, in
community assembly. With functions in this package, NST can be calculated
based on different similarity metrics and/or different null model
algorithms, as well as some previous indexes, e.g. previous Stochasticity
Ratio (ST), Standard Effect Size (SES), modified Raup-Crick metrics (RC).
Functions for permutational test and bootstrapping analysis are also
included. Previous ST is published by Zhou et al (2014)
<doi:10.1073/pnas.1324044111>. NST is modified from ST by considering two
alternative situations and normalizing the index to range from 0 to 1
(Ning et al 2019) <doi:10.1073/pnas.1904623116>. A modified version, MST,
is a special case of NST, used in some recent or upcoming publications,
e.g. Liang et al (2019) <doi:10.1101/638908>. SES is calculated as
described in Kraft et al (2011) <doi:10.1126/science.1208584>. RC is
calculated as reported by Chase et al (2011) <doi:10.1890/es10-00117.1>
and Stegen et al (2013) <doi:10.1038/ismej.2013.93>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
