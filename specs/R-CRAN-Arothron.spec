%global packname  Arothron
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          3%{?dist}
Summary:          Geometric Morphometrics Analysis and Virtual Anthropology

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-methods >= 3.5
BuildRequires:    R-graphics >= 3.4.0
BuildRequires:    R-grDevices >= 3.4.0
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-utils >= 3.4.0
BuildRequires:    R-CRAN-Morpho >= 2.5
BuildRequires:    R-CRAN-vegan >= 2.4
BuildRequires:    R-CRAN-compositions >= 1.40.1
BuildRequires:    R-CRAN-foreach >= 1.4.4
BuildRequires:    R-CRAN-abind >= 1.4
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-alphashape3d >= 1.3
BuildRequires:    R-CRAN-doParallel >= 1.0.11
BuildRequires:    R-parallel >= 1.0
BuildRequires:    R-CRAN-rgl >= 0.93.0
BuildRequires:    R-CRAN-geometry >= 0.3.6
BuildRequires:    R-CRAN-Rvcg >= 0.17
Requires:         R-methods >= 3.5
Requires:         R-graphics >= 3.4.0
Requires:         R-grDevices >= 3.4.0
Requires:         R-stats >= 3.4.0
Requires:         R-utils >= 3.4.0
Requires:         R-CRAN-Morpho >= 2.5
Requires:         R-CRAN-vegan >= 2.4
Requires:         R-CRAN-compositions >= 1.40.1
Requires:         R-CRAN-foreach >= 1.4.4
Requires:         R-CRAN-abind >= 1.4
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-alphashape3d >= 1.3
Requires:         R-CRAN-doParallel >= 1.0.11
Requires:         R-parallel >= 1.0
Requires:         R-CRAN-rgl >= 0.93.0
Requires:         R-CRAN-geometry >= 0.3.6
Requires:         R-CRAN-Rvcg >= 0.17

%description
Tools for geometric morphometric analysis. The package includes tools of
virtual anthropology to align two not articulated parts belonging to the
same specimen, to build virtual cavities as endocast (Profico et al, 2018
<doi:10.1002/ajpa.23493>).

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
%{rlibdir}/%{packname}/INDEX
