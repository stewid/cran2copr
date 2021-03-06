%global packname  suppdata
%global packver   1.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Downloading Supplementary Data from Published Manuscripts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite >= 1.5
BuildRequires:    R-CRAN-xml2 >= 1.2.0
BuildRequires:    R-CRAN-httr >= 1.0.0
BuildRequires:    R-CRAN-rcrossref >= 0.8.0
Requires:         R-CRAN-jsonlite >= 1.5
Requires:         R-CRAN-xml2 >= 1.2.0
Requires:         R-CRAN-httr >= 1.0.0
Requires:         R-CRAN-rcrossref >= 0.8.0

%description
Downloads data supplementary materials from manuscripts, using papers'
DOIs as references. Facilitates open, reproducible research workflows:
scientists re-analyzing published datasets can work with them as easily as
if they were stored on their own computer, and others can track their
analysis workflow painlessly. The main function suppdata() returns a
(temporary) location on the user's computer where the file is stored,
making it simple to use suppdata() with standard functions like
read.csv().

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
