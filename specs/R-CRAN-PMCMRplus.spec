%global packname  PMCMRplus
%global packver   1.4.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.4
Release:          3%{?dist}
Summary:          Calculate Pairwise Multiple Comparisons of Mean Rank SumsExtended

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel >= 4.2.3
BuildRequires:    mpfr-devel >= 3.0.0
BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-kSamples >= 1.2.7
BuildRequires:    R-CRAN-mvtnorm >= 1.0
BuildRequires:    R-CRAN-BWStest >= 0.2.1
BuildRequires:    R-CRAN-multcompView 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-CRAN-Rmpfr 
BuildRequires:    R-CRAN-SuppDists 
BuildRequires:    R-MASS 
Requires:         R-CRAN-kSamples >= 1.2.7
Requires:         R-CRAN-mvtnorm >= 1.0
Requires:         R-CRAN-BWStest >= 0.2.1
Requires:         R-CRAN-multcompView 
Requires:         R-CRAN-gmp 
Requires:         R-CRAN-Rmpfr 
Requires:         R-CRAN-SuppDists 
Requires:         R-MASS 

%description
For one-way layout experiments the one-way ANOVA can be performed as an
omnibus test. All-pairs multiple comparisons tests (Tukey-Kramer test,
Scheffe test, LSD-test) and many-to-one tests (Dunnett test) for normally
distributed residuals and equal within variance are available.
Furthermore, all-pairs tests (Games-Howell test, Tamhane's T2 test,
Dunnett T3 test, Ury-Wiggins-Hochberg test) and many-to-one
(Tamhane-Dunnett Test) for normally distributed residuals and
heterogeneous variances are provided. Van der Waerden's normal scores test
for omnibus, all-pairs and many-to-one tests is provided for non-normally
distributed residuals and homogeneous variances. The Kruskal-Wallis, BWS
and Anderson-Darling omnibus test and all-pairs tests (Nemenyi test, Dunn
test, Conover test, Dwass-Steele-Critchlow- Fligner test) as well as
many-to-one (Nemenyi test, Dunn test, U-test) are given for the analysis
of variance by ranks. Non-parametric trend tests (Jonckheere test, Cuzick
test, Johnson-Mehrotra test, Spearman test) are included. In addition, a
Friedman-test for one-way ANOVA with repeated measures on ranks (CRBD) and
Skillings-Mack test for unbalanced CRBD is provided with consequent
all-pairs tests (Nemenyi test, Siegel test, Miller test, Conover test,
Exact test) and many-to-one tests (Nemenyi test, Demsar test, Exact test).
A trend can be tested with Pages's test. Durbin's test for a two-way
balanced incomplete block design (BIBD) is given in this package as well
as Gore's test for CRBD with multiple observations per cell is given.
Outlier tests, Mandel's k- and h statistic as well as functions for Type I
error and Power analysis as well as generic summary, print and plot
methods are provided.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/README
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
