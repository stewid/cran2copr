%global packname  compareGroups
%global packver   4.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.4.3
Release:          2%{?dist}
Summary:          Descriptive Analysis by Groups

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.1
Requires:         R-core >= 2.13.1
BuildArch:        noarch
BuildRequires:    R-CRAN-SNPassoc 
BuildRequires:    R-survival 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-HardyWeinberg 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-chron 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-officer 
Requires:         R-CRAN-SNPassoc 
Requires:         R-survival 
Requires:         R-tools 
Requires:         R-CRAN-HardyWeinberg 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-methods 
Requires:         R-CRAN-chron 
Requires:         R-stats 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-officer 

%description
Create data summaries for quality control, extensive reports for exploring
data, as well as publication-ready univariate or bivariate tables in
several formats (plain text, HTML,LaTeX, PDF, Word or Excel. Create
figures to quickly visualise the distribution of your data (boxplots,
barplots, normality-plots, etc.). Display statistics (mean, median,
frequencies, incidences, etc.). Perform the appropriate tests (t-test,
Analysis of variance, Kruskal-Wallis, Fisher, log-rank, ...) depending on
the nature of the described variable (normal, non-normal or qualitative).
Summarize genetic data (Single Nucleotide Polymorphisms) data displaying
Allele Frequencies and performing Hardy-Weinberg Equilibrium tests among
other typical statistics and tests for these kind of data.

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
