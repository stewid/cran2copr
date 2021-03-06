%global packname  spant
%global packver   1.7.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.7.0
Release:          1%{?dist}
Summary:          MR Spectroscopy Analysis Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-complexplus 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-smoother 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-ptw 
BuildRequires:    R-CRAN-viridisLite 
BuildRequires:    R-CRAN-mmand 
BuildRequires:    R-CRAN-RNifti 
BuildRequires:    R-CRAN-RNiftyReg 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-miniUI 
BuildRequires:    R-CRAN-oro.dicom 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-jsonlite 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-complexplus 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-nnls 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-smoother 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-ptw 
Requires:         R-CRAN-viridisLite 
Requires:         R-CRAN-mmand 
Requires:         R-CRAN-RNifti 
Requires:         R-CRAN-RNiftyReg 
Requires:         R-CRAN-fields 
Requires:         R-MASS 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-miniUI 
Requires:         R-CRAN-oro.dicom 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-jsonlite 

%description
Tools for reading, visualising and processing Magnetic Resonance
Spectroscopy data. <https://martin3141.github.io/spant/>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
