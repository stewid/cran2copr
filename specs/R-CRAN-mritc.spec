%global packname  mritc
%global packver   0.5-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          3%{?dist}
Summary:          MRI Tissue Classification

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildRequires:    R-CRAN-misc3d >= 0.8.1
BuildRequires:    R-CRAN-oro.nifti >= 0.4.0
BuildRequires:    R-lattice >= 0.18.8
BuildRequires:    R-methods 
Requires:         R-CRAN-misc3d >= 0.8.1
Requires:         R-CRAN-oro.nifti >= 0.4.0
Requires:         R-lattice >= 0.18.8
Requires:         R-methods 

%description
Various methods for MRI tissue classification.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/tables
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
