%define		module	dbus-sharp-glib

Summary:	D-Bus for .NET - GLib integration module
Summary(pl.UTF-8):	D-Bus dla .NET - moduł integrujący z GLib
Name:		dotnet-%{module}
Version:	0.6.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/mono/dbus-sharp-glib/releases
Source0:	https://github.com/mono/dbus-sharp-glib/releases/download/v0.6/%{module}-%{version}.tar.gz
# Source0-md5:	398475a4ed7793eb587c4f0eb913bb7f
Patch0:		%{name}-monodir.patch
URL:		http://mono.github.io/dbus-sharp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dotnet-dbus-sharp-devel >= 1:0.8.0
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.015
Requires:	mono >= 1.1.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no native code
%define		_enable_debug_packages	0

%description
dbus-sharp-glib is a fork of ndesk-dbus-glib, which provides GLib main
loop integration for Managed D-Bus.

%description -l pl.UTF-8
dbus-sharp-glib to odgałęzienie projektu ndesk-dbus-glib,
zapewniającego integrację głównej pętli GLib dla "zarządzanego D-Bus".

%package devel
Summary:	Development files for D-Bus GLib .NET library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki .NET D-Bus GLib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-dbus-sharp-devel >= 1:0.8.0
Requires:	mono-devel >= 1.1.13

%description devel
Development files for D-Bus GLib .NET library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki .NET D-Bus GLib.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	GMCS=/usr/bin/mcs
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%{_prefix}/lib/mono/gac/dbus-sharp-glib

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/dbus-sharp-glib-2.0
%{_pkgconfigdir}/dbus-sharp-glib-2.0.pc
