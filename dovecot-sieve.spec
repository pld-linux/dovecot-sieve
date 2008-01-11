Summary:	Sieve plugin for dovecot
Summary(pl.UTF-8):	Wtyczka Sieve dla dovecota
Name:		dovecot-sieve
Version:	1.0.2
Release:	2
License:	LGPL
Group:		Daemons
Source0:	http://dovecot.org/releases/sieve/%{name}-%{version}.tar.gz
# Source0-md5:  508926fc9ff8e0f6e13506e237d4916b
URL:		http://www.dovecot.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	dovecot-devel
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig
Requires:	dovecot
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
# crude hack ...
perl -pi -e's,have_dovecot_libs=no,have_dovecot_libs=yes,g' configure
%configure \
	INSTALL_DATA="install -c -p -m644" \
	--with-dovecot=%{_includedir}/dovecot
# Replace -I$(dovecot_incdir)/src with -I$(dovecot_incdir)
# and $(dovecotdir)/src with $(libdir)/dovecot for libraries
for f in `find . -name Makefile`
do
	mv -f $f $f.orig
	sed -e's/\-I\$(dovecot_incdir)\/src/\-I\$(dovecot_incdir)/g' \
		-e's/\$(dovecotdir)\/src\(\/lib\/.*\.a\)/\$(libdir)\/dovecot\/plugins\1/g' \
		< $f.orig > $f
done
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# ??? one of two following commands is bogus
rm -f $RPM_BUILD_ROOT%{_libdir}/dovecot/plugins/lda/*.a
mkdir $RPM_BUILD_ROOT%{_libdir}/dovecot/plugins
mv $RPM_BUILD_ROOT%{_libdir}/dovecot/lda $RPM_BUILD_ROOT%{_libdir}/dovecot/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/dovecot/sievec
%attr(755,root,root) %{_libexecdir}/dovecot/sieved
%attr(755,root,root) %{_libdir}/dovecot/plugins/lda/*.so
# !needed?
%{_libdir}/dovecot/plugins/lda/*.la
