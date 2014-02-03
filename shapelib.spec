Name:          shapelib
Version:       1.3.0
Release:       1%{?dist}
Summary:       C library for handling ESRI Shapefiles
# The core library is dual-licensed LGPLv2 or MIT.
# Some contributed files have different licenses:
# - contrib/csv2shp.c: GPLv2+
# - contrib/dbfinfo.c: Public domain
# - contrib/dbfcat.c:  Public domain
License:       (LGPLv2+ or MIT) and GPLv2+ and Public Domain
URL:           http://shapelib.maptools.org/
Source:        http://download.osgeo.org/shapelib/%{name}-1.3.0.tar.gz
# This patch replaces the handmade makefiles with autotools scripts. This patch was generated by
# git clone https://github.com/manisandro/shapelib.git
# cd shapelib
# git checkout autotools
# git diff master..autotools > shapelib_autotools.patch
#
# Upstream is notified about these modifications: http://bugzilla.maptools.org/show_bug.cgi?id=2447
Patch0:        shapelib_autotools.patch

BuildRequires: autoconf automake libtool
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
%setup -q -n %{name}-1.3.0
%patch0 -p1

%build
NOCONFIGURE=1 sh ./autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

# Remove static libraries
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING README README.tree ChangeLog web/*.html
%{_libdir}/libshp.so.*

%files devel
%{_includedir}/shapefil.h
%{_libdir}/libshp.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%doc contrib/doc/
%{_bindir}/*

%changelog
* Mon Feb 03 2014 Sandro Mani <manisandro@gmail.com> - 1.3.0-1
- Initial package for epel7
