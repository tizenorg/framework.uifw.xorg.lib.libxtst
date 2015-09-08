Summary: X.Org X11 libXtst runtime library
Name: libXtst
Version: 1.2.0
Release: 3
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXi-devel

%description
X.Org X11 libXtst runtime library

%package devel
Summary: X.Org X11 libXtst development package
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libXi-devel
Provides: libxtst-devel

%description devel
X.Org X11 libXtst development package

%prep
%setup -q

# Disable static library creation by default.
%define with_static 0

%build

%reconfigure --disable-static \
	       LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
make install DESTDIR=$RPM_BUILD_ROOT

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

rm -rf $RPM_BUILD_ROOT%{_docdir}

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
%doc COPYING ChangeLog
%{_libdir}/libXtst.so.6
%{_libdir}/libXtst.so.6.1.0

%files devel
%defattr(-,root,root,-)
#%doc specs/*.txt
%{_includedir}/X11/extensions/XTest.h
%{_includedir}/X11/extensions/record.h
%if %{with_static}
%{_libdir}/libXtst.a
%endif
%{_libdir}/libXtst.so
%{_libdir}/pkgconfig/xtst.pc
#%{_mandir}/man3/XTest*.3*
