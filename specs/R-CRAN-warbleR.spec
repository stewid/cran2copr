%global packname  warbleR
%global packver   1.1.24
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.24
Release:          2%{?dist}
Summary:          Streamline Bioacoustic Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-seewave >= 2.0.1
BuildRequires:    R-CRAN-tuneR 
BuildRequires:    R-CRAN-NatureSounds 
BuildRequires:    R-CRAN-dtw 
BuildRequires:    R-CRAN-fftw 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-monitoR 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
Requires:         R-CRAN-seewave >= 2.0.1
Requires:         R-CRAN-tuneR 
Requires:         R-CRAN-NatureSounds 
Requires:         R-CRAN-dtw 
Requires:         R-CRAN-fftw 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-monitoR 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-rjson 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-methods 

%description
Functions aiming to facilitate the analysis of the structure of animal
acoustic signals in 'R'. 'warbleR' makes use of the basic sound analysis
tools from the package 'seewave', and offers new tools for acoustic
structure analysis. The main features of the package are the use of loops
to apply tasks through acoustic signals referenced in a selection
(annotation) table and the production of spectrograms in image files that
allow to organize data and verify acoustic analyzes. The package offers
functions to explore, organize and manipulate multiple sound files,
explore and download 'Xeno-Canto' recordings, detect signals
automatically, create spectrograms of complete recordings or individual
signals, run different measures of acoustic signal structure, evaluate the
performance of measurement methods, catalog signals, characterize
different structural levels in acoustic signals, run statistical analysis
of duet coordination and consolidate databases and annotation tables,
among others.

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
