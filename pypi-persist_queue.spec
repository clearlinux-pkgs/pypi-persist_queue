#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-persist_queue
Version  : 0.8.1
Release  : 4
URL      : https://files.pythonhosted.org/packages/06/6f/78ff1a951f02cfcb5c0e17150428bf102eb984e003f1ced9c9164024a2e2/persist-queue-0.8.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/06/6f/78ff1a951f02cfcb5c0e17150428bf102eb984e003f1ced9c9164024a2e2/persist-queue-0.8.1.tar.gz
Summary  : A thread-safe disk based persistent queue in Python.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-persist_queue-license = %{version}-%{release}
Requires: pypi-persist_queue-python = %{version}-%{release}
Requires: pypi-persist_queue-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
persist-queue - A thread-safe, disk-based queue for Python
==========================================================

%package license
Summary: license components for the pypi-persist_queue package.
Group: Default

%description license
license components for the pypi-persist_queue package.


%package python
Summary: python components for the pypi-persist_queue package.
Group: Default
Requires: pypi-persist_queue-python3 = %{version}-%{release}

%description python
python components for the pypi-persist_queue package.


%package python3
Summary: python3 components for the pypi-persist_queue package.
Group: Default
Requires: python3-core
Provides: pypi(persist_queue)

%description python3
python3 components for the pypi-persist_queue package.


%prep
%setup -q -n persist-queue-0.8.1
cd %{_builddir}/persist-queue-0.8.1
pushd ..
cp -a persist-queue-0.8.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685980057
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-persist_queue
cp %{_builddir}/persist-queue-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-persist_queue/a1de90380d37f55aee0af3826f275aca53a74a99 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-persist_queue/a1de90380d37f55aee0af3826f275aca53a74a99

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
