%global packname  REddyProc
%global packver   1.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.2
Release:          3%{?dist}
Summary:          Post Processing of (Half-)Hourly Eddy-Covariance Measurements

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-mlegp 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-solartime 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-mlegp 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-solartime 

%description
Standard and extensible Eddy-Covariance data post-processing (Wutzler et
al. (2018) <doi:10.5194/bg-15-5015-2018>) includes uStar-filtering,
gap-filling, and flux-partitioning. The Eddy-Covariance (EC)
micrometeorological technique quantifies continuous exchange fluxes of
gases, energy, and momentum between an ecosystem and the atmosphere. It is
important for understanding ecosystem dynamics and upscaling exchange
fluxes. (Aubinet et al. (2012) <doi:10.1007/978-94-007-2351-1>). This
package inputs pre-processed (half-)hourly data and supports further
processing. First, a quality-check and filtering is performed based on the
relationship between measured flux and friction velocity (uStar) to
discard biased data (Papale et al. (2006) <doi:10.5194/bg-3-571-2006>).
Second, gaps in the data are filled based on information from
environmental conditions (Reichstein et al. (2005)
<doi:10.1111/j.1365-2486.2005.001002.x>). Third, the net flux of carbon
dioxide is partitioned into its gross fluxes in and out of the ecosystem
by night-time based and day-time based approaches (Lasslop et al. (2010)
<doi:10.1111/j.1365-2486.2009.02041.x>).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/genData
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
