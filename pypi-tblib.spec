#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-tblib
Version  : 1.7.0
Release  : 28
URL      : https://files.pythonhosted.org/packages/d3/41/901ef2e81d7b1e834b9870d416cb09479e175a2be1c4aa1a9dcd0a555293/tblib-1.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d3/41/901ef2e81d7b1e834b9870d416cb09479e175a2be1c4aa1a9dcd0a555293/tblib-1.7.0.tar.gz
Summary  : Traceback serialization library.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-tblib-license = %{version}-%{release}
Requires: pypi-tblib-python = %{version}-%{release}
Requires: pypi-tblib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pip)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pypi(virtualenv)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
Overview
        ========
        
        
        
        Serialization library for Exceptions and Tracebacks.

%package license
Summary: license components for the pypi-tblib package.
Group: Default

%description license
license components for the pypi-tblib package.


%package python
Summary: python components for the pypi-tblib package.
Group: Default
Requires: pypi-tblib-python3 = %{version}-%{release}

%description python
python components for the pypi-tblib package.


%package python3
Summary: python3 components for the pypi-tblib package.
Group: Default
Requires: python3-core
Provides: pypi(tblib)

%description python3
python3 components for the pypi-tblib package.


%prep
%setup -q -n tblib-1.7.0
cd %{_builddir}/tblib-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641588539
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tblib
cp %{_builddir}/tblib-1.7.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tblib/b3dd3604c35c29b5f35f22a314820cbe8a0132b3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tblib/b3dd3604c35c29b5f35f22a314820cbe8a0132b3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*