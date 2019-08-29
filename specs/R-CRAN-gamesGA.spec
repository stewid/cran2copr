%global packname  gamesGA
%global packver   1.1.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3.6
Release:          1%{?dist}
Summary:          Genetic Algorithm for Sequential Symmetric Games

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-grDevices >= 3.4.0
BuildRequires:    R-graphics >= 3.4.0
BuildRequires:    R-stats >= 3.4.0
BuildRequires:    R-CRAN-shiny >= 1.0.0
Requires:         R-grDevices >= 3.4.0
Requires:         R-graphics >= 3.4.0
Requires:         R-stats >= 3.4.0
Requires:         R-CRAN-shiny >= 1.0.0

%description
Finds adaptive strategies for sequential symmetric games using a genetic
algorithm. Currently, any symmetric two by two matrix is allowed, and
strategies can remember the history of an opponent's play from the
previous three rounds of moves in iterated interactions between players.
The genetic algorithm returns a list of adaptive strategies given payoffs,
and the mean fitness of strategies in each generation.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
