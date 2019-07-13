#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tblib
Version  : 1.4.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/b9/28/7c8825703fbeb10bc1b4c9c53e8f73b030bcb14d569ea5eb87c4a53cb98b/tblib-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b9/28/7c8825703fbeb10bc1b4c9c53e8f73b030bcb14d569ea5eb87c4a53cb98b/tblib-1.4.0.tar.gz
Summary  : Traceback serialization library.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: tblib-python = %{version}-%{release}
Requires: tblib-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
========
Overview
========
.. start-badges
.. list-table::
:stub-columns: 1
* - docs
- |docs|
* - tests
- | |travis| |appveyor| |requires|
| |coveralls| |codecov|
* - package
- | |version| |wheel| |supported-versions| |supported-implementations|
| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-tblib/badge/?style=flat
:target: https://readthedocs.org/projects/python-tblib
:alt: Documentation Status

%package python
Summary: python components for the tblib package.
Group: Default
Requires: tblib-python3 = %{version}-%{release}

%description python
python components for the tblib package.


%package python3
Summary: python3 components for the tblib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tblib package.


%prep
%setup -q -n tblib-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556824258
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
