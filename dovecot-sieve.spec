Summary:	Sieve plugin for dovecot
Summary(pl.UTF-8):	Wtyczka Sieve dla dovecota
Name:		dovecot-sieve
Version:	1.1.6
Release:	4
License:	LGPL
Group:		Daemons
Source0:	http://dovecot.org/releases/sieve/%{name}-%{version}.tar.gz
# Source0-md5:	7acf3d98974a515b868addbdb73054eb
URL:		http://www.dovecot.org/
BuildRequires:	bison
BuildRequires:	dovecot-devel >= 1:1.1.1
BuildRequires:	flex
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
%setup -q

%build
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
%attr(755,root,root) %{_libdir}/dovecot/sievec
%attr(755,root,root) %{_libdir}/dovecot/sieved
%attr(755,root,root) %{_libdir}/dovecot/plugins/lda/lib90_cmusieve_plugin.so
