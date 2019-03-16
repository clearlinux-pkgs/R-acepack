#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-acepack
Version  : 1.4.1
Release  : 20
URL      : https://cran.r-project.org/src/contrib/acepack_1.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/acepack_1.4.1.tar.gz
Summary  : ACE and AVAS for Selecting Multiple Regression Transformations
Group    : Development/Tools
License  : MIT
Requires: R-acepack-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
This package is based on public domain S and FORTRAN code for AVAS by
Tibshirani, and on FORTRAN code for ACE from Statlib, written by Spector
and Friedman.

%package lib
Summary: lib components for the R-acepack package.
Group: Libraries

%description lib
lib components for the R-acepack package.


%prep
%setup -q -c -n acepack

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552707658

%install
export SOURCE_DATE_EPOCH=1552707658
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library acepack
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library acepack
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library acepack
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  acepack || :


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
/usr/lib64/R/library/acepack/NEWS
/usr/lib64/R/library/acepack/R/acepack
/usr/lib64/R/library/acepack/R/acepack.rdb
/usr/lib64/R/library/acepack/R/acepack.rdx
/usr/lib64/R/library/acepack/README
/usr/lib64/R/library/acepack/README.ace
/usr/lib64/R/library/acepack/README.avas
/usr/lib64/R/library/acepack/ace.doc
/usr/lib64/R/library/acepack/help/AnIndex
/usr/lib64/R/library/acepack/help/acepack.rdb
/usr/lib64/R/library/acepack/help/acepack.rdx
/usr/lib64/R/library/acepack/help/aliases.rds
/usr/lib64/R/library/acepack/help/paths.rds
/usr/lib64/R/library/acepack/html/00Index.html
/usr/lib64/R/library/acepack/html/R.css
/usr/lib64/R/library/acepack/tests/testthat.R
/usr/lib64/R/library/acepack/tests/testthat/test_transform.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/acepack/libs/acepack.so
/usr/lib64/R/library/acepack/libs/acepack.so.avx2
/usr/lib64/R/library/acepack/libs/acepack.so.avx512
