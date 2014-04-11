Summary:	Set of Python bindings for Trolltech's Qt application framework
Name:		python-qt
Version:	3.18.1
Release:	16
Epoch:		1
License:	GPLv2+
Group:		Development/KDE and Qt
Url:		http://www.riverbankcomputing.co.uk/software/pyqt/intro
Source0:	http://www.riverbankcomputing.com/Downloads/PyQt3/GPL/PyQt-x11-gpl-%{version}.tar.gz
Patch0:		PyQt-x11-gpl-3.17.3-mandriva-multiarch.patch
Patch1:		PyQt-x11-gpl-3.18.1-sip415.patch
BuildRequires:	python-sip
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(qt-mt)
Requires:	python-sip
Provides:	PyQt = %{EVRD}

%description
PyQt is a set of Python bindings for Trolltech's Qt application framework and
runs on all platforms supported by Qt including Windows, MacOS/X and Linux.

%files
%{_bindir}/pyuic
%{_bindir}/pylupdate
%{_datadir}/sip/*
%{py_platsitedir}/q*
%{py_platsitedir}/pyqtconfig.py

#------------------------------------------------------------

%prep
%setup -q -n PyQt-x11-gpl-%{version}
%patch0 -p1
%patch1 -p0

%build
export QTDIR=%{qt3dir}
echo "yes" | python ./configure.py \
    -y qt-mt LIBDIR_QT=%{_libdir}

for name in pylupdate3 pyuic3 qt qtcanvas qtgl qtnetwork qtsql qttable qtui qtxml; do
	sed -i "s#^LIBS = #LIBS = $(python-config --libs) #g" ${name}/Makefile
	sed -i "s#^CFLAGS = #CFLAGS = -DANY=void %{optflags} #g" ${name}/Makefile
	sed -i "s#^CXXFLAGS = #CXXFLAGS = -DANY=void %{optflags} #g" ${name}/Makefile
	sed -i "s#^LFLAGS = #LFLAGS = %{ldflags} #g" ${name}/Makefile
done

%make

%install
%makeinstall_std

