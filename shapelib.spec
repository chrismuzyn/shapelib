# This RPM will possibly fail on PowerPCs, but I am ignoring this.
Summary: API in "C" for Shapefile handling
Name: shapelib
Version: 1.2.10
Release: 6
Epoch: 0
URL: http://shapelib.maptools.org/
Source: http://shapelib.maptools.org/dl/shapelib-%{version}.tar.gz
Patch0: shapelib-%{version}.patch
Patch1: shapelib-1.2.10-endian.patch
License: LGPL/MIT
Group: Development/Libraries
Buildrequires: libtool
BuildRequires: proj-devel >= 0:4.4.1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%package devel
Summary:	Development files for shapelib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

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

%doc LICENSE.LGPL README README.tree dbf_api.html shapelib.html shp_api.html 
%doc contrib/doc/shpproj.txt stream1.sh stream1.out stream2.sh 
%doc stream2.out makeshape.sh stream3.out ChangeLog

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%exclude %{_libdir}/libshp.la

%changelog
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
