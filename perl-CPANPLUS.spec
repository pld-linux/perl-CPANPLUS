
# Conditional build:
%bcond_without tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pnam	CPANPLUS
Summary:	Ameliorated interface to CPAN
Summary(pl):	Ulepszony intefejs do CPAN-u
Name:		perl-CPANPLUS
Version:	0.044
Release:	3
License:	Same as Perl itself
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
Source0:	http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/%{pnam}-%{version}.tar.gz
# Source0-md5:	ab2dd142040d7e65d6b5cb999dd79acf
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Your::Module::Here)'

%description
CPANPLUS provides command-line access to the CPAN interface. Three
functions, fetch, install and shell are imported in to your namespace.
get - an alias for fetch - is also provided.

Although CPANPLUS can also be used within scripts, it is highly
recommended that you use CPANPLUS::Backend in such situations. In
addition to providing an OO interface, CPANPLUS::Backend is more
efficient than CPANPLUS for multiple operations. CPANPLUS is provided
primarily for the command-line, in order to be backwards compatible
with CPAN.pm.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	SETUP=n

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ChangeLog AUTHORS
%{perl_vendorlib}/CPANPLUS.pm
%{perl_vendorlib}/CPANPLUS
%exclude %{perl_vendorlib}/CPANPLUS/*.pod
%{_mandir}/man3/*
