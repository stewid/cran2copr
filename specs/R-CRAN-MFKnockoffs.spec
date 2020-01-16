%global packname  MFKnockoffs
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          Model-Free Knockoff Filter for Controlled Variable Selection

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rdsdp 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-corpcor 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-gtools 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-Rdsdp 
Requires:         R-Matrix 
Requires:         R-CRAN-corpcor 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-gtools 

%description
Model-free knockoffs are a general procedure for controlling the false
discovery rate (FDR) when performing variable selection. For more
information, see the website below and the accompanying paper: Candes et
al., "Panning for Gold: Model-free Knockoffs for High-dimensional
Controlled Variable Selection", 2016, <arXiv:1610.02351>.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX