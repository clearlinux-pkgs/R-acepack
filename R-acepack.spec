#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : R-acepack
Version  : 1.5.2
Release  : 64
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/acepack_1.5.2.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/acepack_1.5.2.tar.gz
Summary  : ACE and AVAS for Selecting Multiple Regression Transformations
Group    : Development/Tools
License  : MIT
Requires: R-acepack-lib = %{version}-%{release}
Requires: R-acepack-license = %{version}-%{release}
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The first, Alternative Conditional Expectations (ACE), 
  is an algorithm to find the fixed point of maximal
  correlation, i.e. it finds a set of transformed response variables that maximizes R^2
  using smoothing functions [see Breiman, L., and J.H. Friedman. 1985. "Estimating Optimal Transformations
  for Multiple Regression and Correlation". Journal of the American Statistical Association.

%package lib
Summary: lib components for the R-acepack package.
Group: Libraries
Requires: R-acepack-license = %{version}-%{release}

%description lib
lib components for the R-acepack package.


%package license
Summary: license components for the R-acepack package.
Group: Default

%description license
license components for the R-acepack package.


%prep
%setup -q -n acepack
pushd ..
cp -a acepack buildavx2
popd
pushd ..
cp -a acepack buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738079969

%install
export SOURCE_DATE_EPOCH=1738079969
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-acepack
cp %{_builddir}/acepack/LICENSE.note %{buildroot}/usr/share/package-licenses/R-acepack/698e04a130a50d9e0b990f4bd2569fa54366102a || :
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/acepack/DESCRIPTION
/usr/lib64/R/library/acepack/INDEX
/usr/lib64/R/library/acepack/LICENSE
/usr/lib64/R/library/acepack/Meta/Rd.rds
/usr/lib64/R/library/acepack/Meta/features.rds
/usr/lib64/R/library/acepack/Meta/hsearch.rds
/usr/lib64/R/library/acepack/Meta/links.rds
/usr/lib64/R/library/acepack/Meta/nsInfo.rds
/usr/lib64/R/library/acepack/Meta/package.rds
/usr/lib64/R/library/acepack/NAMESPACE
/usr/lib64/R/library/acepack/NEWS.md
/usr/lib64/R/library/acepack/R/acepack
/usr/lib64/R/library/acepack/R/acepack.rdb
/usr/lib64/R/library/acepack/R/acepack.rdx
/usr/lib64/R/library/acepack/help/AnIndex
/usr/lib64/R/library/acepack/help/acepack.rdb
/usr/lib64/R/library/acepack/help/acepack.rdx
/usr/lib64/R/library/acepack/help/aliases.rds
/usr/lib64/R/library/acepack/help/paths.rds
/usr/lib64/R/library/acepack/html/00Index.html
/usr/lib64/R/library/acepack/html/R.css
/usr/lib64/R/library/acepack/tests/testthat.R
/usr/lib64/R/library/acepack/tests/testthat/test_ace.R
/usr/lib64/R/library/acepack/tests/testthat/test_avas.R
/usr/lib64/R/library/acepack/tests/testthat/test_bullseye.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/acepack/libs/acepack.so
/V4/usr/lib64/R/library/acepack/libs/acepack.so
/usr/lib64/R/library/acepack/libs/acepack.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-acepack/698e04a130a50d9e0b990f4bd2569fa54366102a
