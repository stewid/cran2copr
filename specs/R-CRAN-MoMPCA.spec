%global packname  MoMPCA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          Inference and Clustering for Mixture of Multinomial PrincipalComponent Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-topicmodels 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-CRAN-topicmodels 
Requires:         R-CRAN-tm 
Requires:         R-Matrix 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
Cluster any count data matrix with a fixed number of variables, such as
document/term matrices. It integrates the dimension reduction aspect of
topic models in the mixture models framework. Inference is done by means
of a greedy Classification Variational Expectation Maximisation (C-VEM)
algorithm. An Integrated Classication Likelihood (ICL) model selection is
designed for selecting the latent dimension (number of topics) and the
number of clusters. For more details, see the article of Jouvin et. al.
(2020) <arxiv.org/abs/1909.00721>.

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
