Name:    perl-Crypt-PasswdMD5
Version: 1.3
Release: 6%{?dist}
Summary: Provides interoperable MD5-based crypt() functions 
License: GPL+ or Artistic
Group:   Development/Libraries
URL:     http://search.cpan.org/dist/Crypt-PasswdMD5/
Source0: http://search.cpan.org/CPAN/authors/id/L/LU/LUISMUNOZ/Crypt-PasswdMD5-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: %{_bindir}/iconv

%description
This package provides MD5-based crypt() functions

%prep
%setup -q -n Crypt-PasswdMD5-%{version}
%{_bindir}/iconv -f iso-8859-1 -t utf-8 -o PasswdMD5.pm.new PasswdMD5.pm && mv PasswdMD5.pm.new PasswdMD5.pm
%{__sed} -i -e 's/ISO-8859-1/UTF-8/' PasswdMD5.pm
%{_bindir}/iconv -f iso-8859-1 -t utf-8 -o README.new README && mv README.new README

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc README
%{perl_vendorlib}/Crypt
%{_mandir}/man3/*

%changelog
* Wed Feb 10 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.3-6
- make rpmlint happy
- Resolves: rhbz#543948

* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.3-5.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3-3.1
Rebuild for new perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Tue Feb 27 2007 Mike McGrath <mmcgrath@redhat.com> - 1.3-2
- Basic fixes (BZ 230228)

* Tue Feb 27 2007 Mike McGrath <mmcgrath@redhat.com> - 1.3-1
- Initial Packaging
