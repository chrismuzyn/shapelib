# This RPM will possibly fail on PowerPCs, but I am ignoring this.
Summary: API in "C" for Shapefile handling
Name: shapelib
Version: 1.2.10
Release: 12.20060304cvs
URL: http://shapelib.maptools.org/
Source: http://shapelib.maptools.org/dl/shapelib-%{version}.tar.gz
Patch0: shapelib-1.2.10-Makefile.patch
Patch1: shapelib-1.2.10-endian.patch
Patch2: shapelib-1.2.10-Makefile2.patch
License: LGPL/MIT
Group: Development/Libraries
BuildRequires: proj-devel >= 4.4.1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%package devel
Summary: Development files for shapelib
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description
The Shapefile C Library provides the ability to write
simple C programs for reading, writing and updating (to a
limited extent) ESRI Shapefiles, and the associated
attribute file (.dbf).

%description devel
This package contains libshp and the appropriate header files.

%prep
%setup -q -T -b 0
%patch -p1 -b .buildroot
%patch1 -p1 -b .endian
%patch2 -p1 -b .buildroot

%build
make %{?_smp_mflags} libdir=%{_libdir} CFLAGS="$RPM_OPT_FLAGS" lib
make %{?_smp_mflags} libdir=%{_libdir} CFLAGS="$RPM_OPT_FLAGS" all

cd contrib
make %{?_smp_mflags} libdir=%{_libdir} EXTRACFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

cd contrib
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*.so.*

%doc LICENSE.LGPL README README.tree web/*.html
%doc contrib/doc/shpproj.txt stream1.sh stream1.out stream2.sh
%doc stream2.out makeshape.sh stream3.out ChangeLog

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%exclude %{_libdir}/libshp.la

%changelog
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

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
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
- Fixed %post and %postun
- Changed group to Development/Libraries, although this appears to be only
  somewhat satisfactory.
- Removed "which make"

* Wed Nov  5 2003 David M. Kaplan <dmk@erizo.ucdavis.edu> 0:1.2.10-0.fdr.1
- Updated to 1.2.10 release
- Major changes to spec for Fedora
- Changes to Makefile patch for Fedora
- Split off devel package
