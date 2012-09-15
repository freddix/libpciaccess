Summary:	libpciaccess library to access PCI bus and devices
Name:		libpciaccess
Version:	0.13.1
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
# Source0-md5:	399a419ac6a54f0fc07c69c9bdf452dc
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires:	pciutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpciaccess library provides generic access to the PCI bus and
devices.

%package devel
Summary:	Header files for pciaccess library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files needed to develop programs that
use pciaccess library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-pciids-path=/etc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libpciaccess.so.?
%attr(755,root,root) %{_libdir}/libpciaccess.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpciaccess.so
%{_pkgconfigdir}/pciaccess.pc
%{_includedir}/pciaccess.h

