%define _disable_ld_no_undefined 1

%define py3verflags %(python3 -c "import sysconfig; print(sysconfig.get_config_var('SOABI'))")
%define py2verflags -python2.7
%define api 5.11

Summary:	The PySide project provides LGPL-licensed Python bindings for Qt5
Name:		pyside2-tools
Version:	5.11.2
Release:	1
License:	LGPLv2+
Group:		Development/KDE and Qt
Url:		https://wiki.qt.io/Qt_for_Python
Source0:	pyside-setup-everywhere-src-%{version}.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	cmake
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:  python-setuptools 
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(shiboken2)
BuildRequires:	pkgconfig(pyside2)

%description
The PySide project provides LGPL-licensed Python bindings for the Qt
cross-platform application and UI framework. PySide Qt bindings allow both free
open source and proprietary software development and ultimately aim to support
all of the platforms as Qt itself.

%files
%{_bindir}/pyside2-*
%{py_platsitedir}/pyside2uic
%{_mandir}/man1/pyside2-*

%prep
%setup -qn pyside-setup-everywhere-src-%{version}

%build

pushd sources/pyside2-tools
%cmake -DBUILD_TESTS=OFF \
     -DUSE_PYTHON_VERSION=3
%make


%install

%makeinstall_std -C sources/pyside2-tools/build

