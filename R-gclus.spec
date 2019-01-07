#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gclus
Version  : 1.3.2
Release  : 12
URL      : https://cran.r-project.org/src/contrib/gclus_1.3.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gclus_1.3.2.tar.gz
Summary  : Clustering Graphics
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
displays by some merit index. Package contains various indices of merit,
 ordering functions, and enhanced versions of pairs and parcoord which
 color panels according to their merit level.

%prep
%setup -q -c -n gclus

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546903080

%install
export SOURCE_DATE_EPOCH=1546903080
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gclus
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gclus
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gclus
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library gclus|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gclus/DESCRIPTION
/usr/lib64/R/library/gclus/INDEX
/usr/lib64/R/library/gclus/Meta/Rd.rds
/usr/lib64/R/library/gclus/Meta/data.rds
/usr/lib64/R/library/gclus/Meta/features.rds
/usr/lib64/R/library/gclus/Meta/hsearch.rds
/usr/lib64/R/library/gclus/Meta/links.rds
/usr/lib64/R/library/gclus/Meta/nsInfo.rds
/usr/lib64/R/library/gclus/Meta/package.rds
/usr/lib64/R/library/gclus/Meta/vignette.rds
/usr/lib64/R/library/gclus/NAMESPACE
/usr/lib64/R/library/gclus/R/gclus
/usr/lib64/R/library/gclus/R/gclus.rdb
/usr/lib64/R/library/gclus/R/gclus.rdx
/usr/lib64/R/library/gclus/data/bank.RData
/usr/lib64/R/library/gclus/data/body.RData
/usr/lib64/R/library/gclus/data/ozone.RData
/usr/lib64/R/library/gclus/data/wine.RData
/usr/lib64/R/library/gclus/doc/gclus.R
/usr/lib64/R/library/gclus/doc/gclus.Rmd
/usr/lib64/R/library/gclus/doc/gclus.html
/usr/lib64/R/library/gclus/doc/index.html
/usr/lib64/R/library/gclus/help/AnIndex
/usr/lib64/R/library/gclus/help/aliases.rds
/usr/lib64/R/library/gclus/help/gclus.rdb
/usr/lib64/R/library/gclus/help/gclus.rdx
/usr/lib64/R/library/gclus/help/paths.rds
/usr/lib64/R/library/gclus/html/00Index.html
/usr/lib64/R/library/gclus/html/R.css
