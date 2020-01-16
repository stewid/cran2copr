%global packname  GET
%global packver   0.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Global Envelopes

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-fda.usc 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-fda.usc 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-gstat 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-spatstat 
Requires:         R-stats 
Requires:         R-utils 

%description
Implementation of global envelopes with intrinsic graphical interpretation
which can be used for graphical Monte Carlo and permutation tests where
the test statistic is a multivariate vector or function (e.g.
goodness-of-fit testing for point patterns and random sets, functional
analysis of variance, functional general linear model, n-sample test of
correspondence of distribution functions), for central regions of
functional or multivariate data (e.g. outlier detection, functional
boxplot) and for global confidence and prediction bands (e.g. confidence
band in polynomial regression, Bayesian posterior prediction). See
Myllymäki et al. (2017) <doi: 10.1111/rssb.12172>, Mrkvička et al. (2017)
<doi: 10.1007/s11222-016-9683-9>, Mrkvička et al. (2016) <doi:
10.1016/j.spasta.2016.04.005>, Mrkvička et al. (2018) <arXiv:1612.03608>,
Mrkvička et al. (2019) <arXiv:1906.09004>, Mrkvička et al. (2019)
<arXiv:1902.04926>.

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