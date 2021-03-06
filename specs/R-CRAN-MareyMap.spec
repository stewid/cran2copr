%global packname  MareyMap
%global packver   1.3.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.5
Release:          3%{?dist}
Summary:          Estimation of Meiotic Recombination Rates Using Marey Maps

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-tcltk 
BuildRequires:    R-CRAN-tkrplot 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-tcltk 
Requires:         R-CRAN-tkrplot 
Requires:         R-tools 
Requires:         R-utils 

%description
Local recombination rates are graphically estimated across a genome using
Marey maps.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/about.txt
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/gnome-settings.gif
%doc %{rlibdir}/%{packname}/gtk-add.gif
%doc %{rlibdir}/%{packname}/license.txt
%doc %{rlibdir}/%{packname}/stock_color.gif
%doc %{rlibdir}/%{packname}/stock_delete.gif
%doc %{rlibdir}/%{packname}/stock_help-agent.gif
%doc %{rlibdir}/%{packname}/stock_save.gif
%doc %{rlibdir}/%{packname}/stock_show-all.gif
%{rlibdir}/%{packname}/INDEX
