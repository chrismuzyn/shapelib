#global pre RC1

Name:          shapelib
Version:       1.4.0
Release:       2%{?pre:.%pre}%{?dist}
Summary:       C library for handling ESRI Shapefiles
# The core library is dual-licensed LGPLv2 or MIT.
# Some contributed files have different licenses:
# - contrib/csv2shp.c: GPLv2+
# - contrib/dbfinfo.c: Public domain
# - contrib/dbfcat.c:  Public domain
License:       (LGPLv2+ or MIT) and GPLv2+ and Public Domain
URL:           http://shapelib.maptools.org/
Source:        http://download.osgeo.org/shapelib/%{name}-%{version}%{?pre:%pre}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: proj-devel >= 4.4.1

%description
The Shapefile C Library provides the ability to write
simple C programs for reading, writing and updating (to a
limited extent) ESRI Shapefiles, and the associated
attribute file (.dbf).


%package devel
Summary:       Development files for shapelib
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libshp and the appropriate header files.


%package tools
Summary:       shapelib utility programs
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description tools
This package contains various utility programs distributed with shapelib.


%prep
%autosetup


%build
%configure --disable-static
%make_build


%install
%make_install

# Remove static libraries
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README README.tree ChangeLog web/*.html
%license COPYING
%{_libdir}/libshp.so.2*

%files devel
%{_includedir}/shapefil.h
%{_libdir}/libshp.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%doc contrib/doc/
%{_bindir}/*


%changelog
* Wed Jan 25 2017 Sandro Mani <manisandro@gmail.com> - 1.4.0-2
- Rebuild (proj)

* Sun Dec 11 2016 Sandro Mani <manisandro@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Wed Dec 07 2016 Sandro Mani <manisandro@gmail.com> - 1.4.0-0.1.RC1
- Update to 1.4.0-RC1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0f-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0f-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.0f-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 12 2015 Sandro Mani <manisandro@gmail.com> - 1.3.0f-5
- Rebuild (proj)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0f-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0f-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 06 2014 Sandro Mani <manisandro@gmail.com> - 1.3.0f-3
- Backport some fixes from the gdal bundled shapelib

* Thu Aug 08 2013 Sandro Mani <manisandro@gmail.com> - 1.3.0f-2
- Add missing licenses

* Mon Aug 05 2013 Sandro Mani <manisandro@gmail.com> - 1.3.0f-1
- Update to 1.3.0 final

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0b2-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0b2-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0b2-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Apr 21 2011 Karsten Hopp <karsten@redhat.com> 1.3.0b2-7.1
- remove endian definition from Makefile, leave it to endian.h

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0b2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed May 19 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b2-6
- update to latest upstream beta

* Tue Mar 09 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b1-5
- update to latest upstream version

* Fri Feb 19 2010 Lucian Langa <cooly@gnome.eu.org> - 1.2.10-2.20100216cvs
- update patch0-3 fix undefined symbols

* Tue Feb 16 2010 Lucian Langa <cooly@gnome.eu.org> - 1.2.10-1.20100216cvs
- revert to latest cvs snapshot

* Thu Feb 04 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b1-4
- misc cleanups

* Thu Feb 04 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b1-3
- do not package static libfiles (#556094)

* Thu Jan 07 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b1-2
- fix patch2 - no not depend on gdal

* Thu Jan 07 2010 Lucian Langa <cooly@gnome.eu.org> - 1.3.0b1-1
- misc cleanups
- update BR
- fix source0
- update to latest upstream snapshot

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-20.20060304cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10-19.20060304cvs
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.10-18.20060304cvs
- fix patch application

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.2.10-17.20060304cvs
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.10-16.20060304cvs
- Autorebuild for GCC 4.3

* Sun Oct  21 2007 Shawn McCann <mccann0011@hotmail.com> - 1.2.10-15.20060304cvs
- Fix for bug 339931

* Sat Sep  16 2006 Shawn McCann <mccann0011@hotmail.com> - 1.2.10-12.20060304cvs
- Rebuild for FC6

* Sun Mar  5 2006 Shawn McCann <mccann0011@hotmail.com> - 1.2.10-11.20060304cvs
- Fixed a makefile bug that messed up parallel builds

* Sat Mar  4 2006 Shawn McCann <mccann0011@hotmail.com> - 1.2.10-10.20060304cvs
- Upgraded to cvs snapshot taken on March 4, 2006

* Sat Mar  4 2006 Shawn McCann <mccann0011@hotmail.com> - 1.2.10-9
- Rebuild for Fedora Extras 5

* Mon Apr 11 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.2.10-8
- Fix "invalid lvalue in assignment" for GCC4.

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Feb 13 2005 David Woodhouse <dwmw2@infradead.org> 0:1.2.10-6
- Don't hard-code endianness; just use endian.h

* Wed Dec 15 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:1.2.10-5
- Patched patch and spec file according to suggestions of Michael Schwendt
- In particular, this separates the building from the installing in the rpm.

* Thu Aug 12 2004 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:1.2.10-0.fdr.4
- Moved RPM_OPT_FLAGS out of make files.
- Removed backup files from patch.
- Made sure that make was using the appropriate libdir.

* Mon Dec 22 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:1.2.10-0.fdr.3
- Added url tag, changed copyright to license and changed permissions on patch file.

* Mon Dec 22 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:1.2.10-0.fdr.2
- Add source URL
- Removed proj requirement as it is automatically detected.
- Added epoch to proj-devel requirement
- Fixed post and postun
- Changed group to Development/Libraries, although this appears to be only
  somewhat satisfactory.
- Removed "which make"

* Wed Nov  5 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:1.2.10-0.fdr.1
- Updated to 1.2.10 release
- Major changes to spec for Fedora
- Changes to Makefile patch for Fedora
- Split off devel package
