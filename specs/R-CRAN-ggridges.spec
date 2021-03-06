%global packname  ggridges
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          3%{?dist}
Summary:          Ridgeline Plots in 'ggplot2'

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-grid >= 3.0.0
BuildRequires:    R-CRAN-withr >= 2.1.1
BuildRequires:    R-CRAN-plyr >= 1.8.0
BuildRequires:    R-CRAN-scales >= 0.4.1
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-grid >= 3.0.0
Requires:         R-CRAN-withr >= 2.1.1
Requires:         R-CRAN-plyr >= 1.8.0
Requires:         R-CRAN-scales >= 0.4.1

%description
Ridgeline plots provide a convenient way of visualizing changes in
distributions over time or space. This package enables the creation of
such plots in 'ggplot2'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
