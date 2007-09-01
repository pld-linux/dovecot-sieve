Summary: Sieve plugin for dovecot
Name: dovecot-sieve
Version: 1.0.2
Release: 1%{?dist}
License: LGPL
Group: System Environment/Daemons
URL: http://www.dovecot.org/
Source0: http://dovecot.org/releases/sieve/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: dovecot-devel
BuildRequires: autoconf, automake, libtool
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: flex, bison
Requires: dovecot

%description
Sieve is a language that can be used to create filters for electronic
mail. It owes its creation to the CMU Cyrus Project, creators of Cyrus
IMAP server.

This dovecot plugin is derived is from Cyrus IMAP v2.2.12.

%prep
%setup -q

%build
# crude hack ...
perl -pi -e's,have_dovecot_libs=no,have_dovecot_libs=yes,g' configure
%configure --with-dovecot=%{_includedir}/dovecot \
  INSTALL_DATA="install -c -p -m644"
# Replace -I$(dovecotdir)/src with -I$(dovecotdir)/src
# and $(dovecotdir)/src with $(libdir)/dovecot for libraries
for f in `find . -name Makefile`
do
    mv -f $f $f.orig
    sed -e's/\-I\$(dovecot_incdir)\/src/\-I\$(dovecot_incdir)/g' \
        -e's/\$(dovecotdir)\/src\(\/lib\/.*\.a\)/\$(libdir)\/dovecot\/plugins\1/g' \
        < $f.orig > $f
done
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/dovecot/plugins/lda/*.a
mkdir %{buildroot}%{_libdir}/dovecot/plugins
mv %{buildroot}%{_libdir}/dovecot/lda %{buildroot}%{_libdir}/dovecot/plugins/. 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libexecdir}/dovecot/sievec
%{_libexecdir}/dovecot/sieved
%{_libdir}/dovecot/plugins/lda/*.so
%{_libdir}/dovecot/plugins/lda/*.la

%changelog
