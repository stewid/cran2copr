%global packname  AzureStor
%global packver   3.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2.2
Release:          2%{?dist}
Summary:          Storage Management in 'Azure'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-AzureRMR >= 2.3.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-mime 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-AzureRMR >= 2.3.0
Requires:         R-utils 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-mime 
Requires:         R-CRAN-openssl 
Requires:         R-CRAN-xml2 

%description
Manage storage in Microsoft's 'Azure' cloud:
<https://azure.microsoft.com/services/storage>. On the admin side,
'AzureStor' includes features to create, modify and delete storage
accounts. On the client side, it includes an interface to blob storage,
file storage, and 'Azure Data Lake Storage Gen2': upload and download
files and blobs; list containers and files/blobs; create containers; and
so on. Authenticated access to storage is supported, via either a shared
access key or a shared access signature (SAS). Part of the 'AzureR' family
of packages.

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
