Name: python-qt
Summary: Set of Python bindings for Trolltech's Qt application framework
Version: 3.18.1
Release: %mkrel 9
Epoch: 1
Group: Development/KDE and Qt
URL: http://www.riverbankcomputing.co.uk/software/pyqt/intro
Source0: http://www.riverbankcomputing.com/Downloads/PyQt3/GPL/PyQt-x11-gpl-%{version}.tar.gz
Patch0: PyQt-x11-gpl-3.17.3-mandriva-multiarch.patch
License: GPLv2+
Provides: PyQt = %epoch:%version-%release
Requires: python-sip >= 1:4.7
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: qt3-devel 
BuildRequires: python-sip >= 1:4.7
BuildRequires: python-devel

%description
PyQt is a set of Python bindings for Trolltech's Qt application framework and
runs on all platforms supported by Qt including Windows, MacOS/X and Linux.

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
    -y qt-mt LIBDIR_QT=%{_libdir}

for name in pylupdate3 pyuic3 qt qtcanvas qtgl qtnetwork qtsql qttable qtui qtxml; do
	sed -i "s#^LIBS = #LIBS = $(python-config --libs) #g" ${name}/Makefile
	sed -i "s#^CFLAGS = #CFLAGS = %{optflags} #g" ${name}/Makefile
	sed -i "s#^CXXFLAGS = #CXXFLAGS = %{optflags} #g" ${name}/Makefile
	sed -i "s#^LFLAGS = #LFLAGS = %{ldflags} #g" ${name}/Makefile
done

%make

%install
rm -rf %buildroot
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot

