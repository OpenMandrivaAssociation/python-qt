Name: python-qt
Summary: Riverbanks's python sip
Version: 3.17.3
Release: %mkrel 1
Epoch: 1
Group: Development/KDE and Qt
URL: http://www.riverbankcomputing.co.uk/pyqt/index.php
Source0: http://www.riverbankcomputing.com/Downloads/PyQt3/GPL/PyQt-x11-gpl-%{version}.tar.gz
Patch0: PyQt-x11-gpl-3.17.3-mandriva-multiarch.patch
License: GPL
Provides: PyQt = %epoch:%version-%release
Requires: python-sip >= 1:4.7
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: qt3-devel 
BuildRequires: qscintilla-devel >= 1.7
BuildRequires: python-sip >= 1:4.7
%py_requires -d

%description

%files 
%defattr(-,root,root)
%_bindir/pyuic
%_bindir/pylupdate
%py_platsitedir/q*
%py_platsitedir/pyqtconfig.py
%_datadir/sip/*

#------------------------------------------------------------

%prep
%setup -q -n PyQt-x11-gpl-%version
%patch0 -p1

%build
export QTDIR=%qt3dir
echo "yes" | python ./configure.py \
    -y qt-mt

%make

%install
rm -rf %buildroot
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot

