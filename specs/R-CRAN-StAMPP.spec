%global packname  StAMPP
%global packver   1.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.1
Release:          3%{?dist}
Summary:          Statistical Analysis of Mixed Ploidy Populations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pegas 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-adegenet 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
Requires:         R-CRAN-pegas 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-adegenet 
Requires:         R-methods 
Requires:         R-utils 

%description
Allows users to calculate pairwise Nei's Genetic Distances (Nei 1972),
pairwise Fixation Indexes (Fst) (Weir & Cockerham 1984) and also Genomic
Relationship matrixes following Yang et al. (2010) in mixed and single
ploidy populations. Bootstrapping across loci is implemented during Fst
calculation to generate confidence intervals and p-values around pairwise
Fst values. StAMPP utilises SNP genotype data of any ploidy level (with
the ability to handle missing data) and is coded to utilise multithreading
where available to allow efficient analysis of large datasets. StAMPP is
able to handle genotype data from genlight objects allowing integration
with other packages such adegenet. Please refer to LW Pembleton, NOI Cogan
& JW Forster, 2013, Molecular Ecology Resources, 13(5), 946-952.
<doi:10.1111/1755-0998.12129> for the appropriate citation and user
manual. Thank you in advance.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
