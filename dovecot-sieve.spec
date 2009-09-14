%define	dovecot_series	1.2
%define	sieve_version	0.1.12
Summary:	Sieve plugin for dovecot
Summary(pl.UTF-8):	Wtyczka Sieve dla dovecota
Name:		dovecot-sieve
Version:	%{dovecot_series}_%{sieve_version}
Release:	3
License:	LGPL
Group:		Daemons
Source0:	http://www.rename-it.nl/dovecot/%{dovecot_series}/dovecot-%{dovecot_series}-sieve-%{sieve_version}.tar.gz
# Source0-md5:	8749f26606c4563f0676bacc44e89ca2
URL:		http://www.dovecot.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	dovecot-devel >= 1:1.2.3
BuildRequires:	flex
BuildRequires:	libtool
%requires_eq_to	dovecot dovecot-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sieve is a language that can be used to create filters for electronic
mail. It owes its creation to the CMU Cyrus Project, creators of Cyrus
IMAP server.

This dovecot plugin is derived is from Cyrus IMAP v2.2.12.

%description -l pl.UTF-8
Sieve to język używany do tworzenia filtrów dla poczty elektronicznej.
Zawdzięcza swoje powstanie projektowi CMU Cyrus, twórcom serwera
pocztowego Cyrus IMAP.

Ta wtyczka dovecota wywodzi się z serwera Cyrus IMAP w wersji 2.2.12.

%prep
%setup -q -n dovecot-%{dovecot_series}-sieve-%{sieve_version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--with-dovecot=%{_libdir}/dovecot-devel

%{__make} \
	dovecot_incdir=%{_includedir}/dovecot \
	moduledir=%{_libdir}/dovecot/plugins

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	moduledir=%{_libdir}/dovecot/plugins

rm -f $RPM_BUILD_ROOT%{_libdir}/dovecot/plugins/lda/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS 
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/dovecot/plugins/lda/lib90_sieve_plugin.so
%{_mandir}/man1/*.1.gz
