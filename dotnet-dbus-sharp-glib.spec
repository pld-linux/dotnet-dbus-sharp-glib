%include	/usr/lib/rpm/macros.mono
%define		module	dbus-sharp-glib

Summary:	D-Bus for .NET - GLib integration module
Summary(pl.UTF-8):	D-Bus dla .NET - moduł integrujący z GLib
Name:		dotnet-%{module}
Version:	0.5.0
Release:	2
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/mono/dbus-sharp/downloads
Source0:	http://github.com/downloads/mono/dbus-sharp/%{module}-%{version}.tar.gz
# Source0-md5:	2284293316eb3a89f0f78798b8a24418
Patch0:		%{name}-monodir.patch
URL:		http://mono.github.com/dbus-sharp/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dotnet-dbus-sharp-devel >= 1:0.7.0
BuildRequires:	mono-csharp >= 1.1.13
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	rpmbuild(monoautodeps)
Requires:	mono >= 1.1.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	dotnet-dbus-sharp-devel >= 1:0.7.0
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

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/dbus-sharp-glib-1.0
%{_pkgconfigdir}/dbus-sharp-glib-1.0.pc
