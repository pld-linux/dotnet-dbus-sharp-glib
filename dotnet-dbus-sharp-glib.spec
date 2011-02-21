%include	/usr/lib/rpm/macros.mono
%define		module	dbus-sharp-glib

Summary:	.NET library for using D-BUS message bus (GLib integration)
Summary(pl.UTF-8):	Biblioteka .NET do używania magistrali przesyłania komunikatów D-BUS z GLib
Name:		dotnet-%{module}
Version:	0.5.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://github.com/downloads/mono/dbus-sharp/%{module}-%{version}.tar.gz
# Source0-md5:	2284293316eb3a89f0f78798b8a24418
#URL:		http://www.ndesk.org/DBusSharp
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	rpmbuild(monoautodeps)
# DllImport, not detected by monoautodeps
%ifarch %{x8664} ia64 ppc64 s390x
Requires:	libglib-2.0.so.0()(64bit)
%else
Requires:	libglib-2.0.so.0
%endif
Obsoletes:	ndesk-dbus-glib
ExclusiveArch:	%{ix86} %{x8664} arm hppa ia64 ppc s390 s390x sparc sparcv9
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
.NET library for using D-BUS with GLib.

This code provides GLib main loop integration for Managed D-Bus.

%description -l pl.UTF-8
Biblioteka .NET do używania D-BUS wraz z GLib.

Ten kod udostępnia integrację głównej pętli GLib z Managed D-Bus.

%package devel
Summary:	Development files for ndesk D-BUS GLib .NET library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki .NET ndesk D-BUS GLib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-ndesk-dbus-sharp-devel >= 0.4

%description devel
Development files for ndesk D-BUS GLib .NET library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki .NET ndesk D-BUS GLib.

%prep
%setup -q -n %{module}-%{version}

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
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
%{_prefix}/lib/mono/dbus-sharp-glib-1.0

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/dbus-sharp-glib-1.0.pc
