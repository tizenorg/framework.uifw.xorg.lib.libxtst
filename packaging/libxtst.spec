Name:       libxtst
Summary:    X.Org X11 libXtst runtime library
Version:    1.2.0
Release:    2.6
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(inputproto)
BuildRequires:  pkgconfig(recordproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xorg-macros)

%description
Description: %{summary}


%package devel
Summary:    Development components for the libXtst library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Description: %{summary}


%prep
%setup -q

%build

%reconfigure \
	CFLAGS="-Wall -g" \
	LDFLAGS="-Wl,--hash-style=both -Wl,--as-needed"

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig



%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog
%{_libdir}/libXtst.so.6
%{_libdir}/libXtst.so.6.1.0


%files devel
%defattr(-,root,root,-)
%{_libdir}/libXtst.so
%{_libdir}/pkgconfig/xtst.pc
%{_includedir}/X11/extensions/XTest.h
%{_includedir}/X11/extensions/record.h
%{_docdir}/libXtst/*.xml
