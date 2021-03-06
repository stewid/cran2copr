%global packname  maditr
%global packver   0.7.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.4
Release:          1%{?dist}
Summary:          Fast Data Aggregation, Modification, and Filtering with Pipesand 'data.table'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-data.table >= 1.12.6
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-data.table >= 1.12.6

%description
Provides pipe-style interface for 'data.table'. Package preserves all
'data.table' features without significant impact on performance. 'let' and
'take' functions are simplified interfaces for most common data
manipulation tasks. For example, you can write 'take(mtcars, mean(mpg), by
= am)' for aggregation or 'let(mtcars, hp_wt = hp/wt, hp_wt_mpg =
hp_wt/mpg)' for modification. Use 'take_if/let_if' for conditional
aggregation/modification. 'query_if' function translates its arguments
one-to-one to '[.data.table' method. Additionally there are some
conveniences such as automatic 'data.frame' conversion to 'data.table'.

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
