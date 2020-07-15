%global packname  freesurferformats
%global packver   0.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          3%{?dist}
Summary:          Read and Write 'FreeSurfer' Neuroimaging File Formats

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pkgfilecache >= 0.1.1
BuildRequires:    R-CRAN-xml2 
Requires:         R-CRAN-pkgfilecache >= 0.1.1
Requires:         R-CRAN-xml2 

%description
Provides functions to read and write neuroimaging data in various file
formats, with a focus on 'FreeSurfer' <http://freesurfer.net/> formats.
This includes, but is not limited to, the following file formats: 1)
MGH/MGZ format files, which can contain multi-dimensional images or other
data. Typically they contain time-series of three-dimensional brain scans
acquired by magnetic resonance imaging (MRI). They can also contain
vertex-wise measures of surface morphometry data. The MGH format is named
after the Massachusetts General Hospital, and the MGZ format is a
compressed version of the same format. 2) 'FreeSurfer' morphometry data
files in binary 'curv' format. These contain vertex-wise surface measures,
i.e., one scalar value for each vertex of a brain surface mesh. These are
typically values like the cortical thickness or brain surface area at each
vertex. 3) Annotation file format. This contains a brain surface
parcellation derived from a cortical atlas. 4) Surface file format.
Contains a brain surface mesh, given by a list of vertices and a list of
faces.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
