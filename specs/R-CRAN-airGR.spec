%global packname  airGR
%global packver   1.4.3.65
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3.65
Release:          3%{?dist}
Summary:          Suite of GR Hydrological Models for Precipitation-RunoffModelling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1

%description
Hydrological modelling tools developed at INRAE-Antony (HYCAR Research
Unit, France). The package includes several conceptual rainfall-runoff
models (GR4H, GR5H, GR4J, GR5J, GR6J, GR2M, GR1A), a snow accumulation and
melt model (CemaNeige) and the associated functions for their calibration
and evaluation. Use help(airGR) for package description and references.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/vignettesData
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
