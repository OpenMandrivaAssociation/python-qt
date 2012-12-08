Name: python-qt
Summary: Set of Python bindings for Trolltech's Qt application framework
Version: 3.18.1
Release: %mkrel 10
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
BuildRequires: mesaglu-devel
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



%changelog
* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 1:3.18.1-9mdv2011.0
+ Revision: 672522
- add br

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Fri Dec 24 2010 Funda Wang <fwang@mandriva.org> 1:3.18.1-8mdv2011.0
+ Revision: 624601
- rebuild for new python-sip

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 1:3.18.1-7mdv2011.0
+ Revision: 590772
- rebuild for py2.7

* Wed Sep 01 2010 Funda Wang <fwang@mandriva.org> 1:3.18.1-6mdv2011.0
+ Revision: 575011
- rebuild for new python-sip

* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 1:3.18.1-5mdv2011.0
+ Revision: 553431
- use correct flags

* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 1:3.18.1-4mdv2011.0
+ Revision: 553430
- rebuild

* Sat Jan 16 2010 Funda Wang <fwang@mandriva.org> 1:3.18.1-3mdv2010.1
+ Revision: 492114
- rebuild for new python-sip

* Mon Nov 23 2009 Funda Wang <fwang@mandriva.org> 1:3.18.1-2mdv2010.1
+ Revision: 469284
- rebuild for new sip

* Thu Jun 18 2009 Funda Wang <fwang@mandriva.org> 1:3.18.1-1mdv2010.0
+ Revision: 387136
- New version 3.18.1

* Mon Jun 08 2009 Funda Wang <fwang@mandriva.org> 1:3.18-1mdv2010.0
+ Revision: 383813
- New version 3.18

* Mon Dec 29 2008 Crispin Boylan <crisb@mandriva.org> 1:3.17.6-1mdv2009.1
+ Revision: 321218
- Set LIBDIR_QT
- New version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

* Thu May 22 2008 Funda Wang <fwang@mandriva.org> 1:3.17.4-1mdv2009.0
+ Revision: 209968
- New version 3.17.4

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Helio Chissini de Castro <helio@mandriva.com>
    - Rebuild to kick old revisions

* Mon Aug 20 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.17.3-2mdv2008.0
+ Revision: 68049
- Fix description
- Scintilla bindings isn't generated inside python-qt package, but inside new scintilla package

* Mon Aug 20 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.17.3-1mdv2008.0
+ Revision: 67993
- Restored external python-qt. kde 3 will not be updated with current releases sooner, and proper
  updates will appears directly on Riverbank official tarball, so we will drop the kebindings build
  in favor of external one. Same will happens with python-kde. The old move to kdebindings makes no
  sense anymore. This move back will help creation of qt4 ( and future kde4 ) python bindings.
- import python-qt-3.17.3-1mdv2008.0


