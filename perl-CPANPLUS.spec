#
# Conditional build:
%bcond_with	tests	# perform "make test" (may fail depending on what you 
			# have in your ~/.gnupg dir)
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	CPANPLUS
Summary:	Ameliorated interface to CPAN
Summary(pl):	Ulepszony interfejs do CPAN-u
Name:		perl-CPANPLUS
Version:	0.0499
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
Source0:	http://www.cpan.org/modules/by-authors/id/A/AU/AUTRIJUS/%{pnam}-%{version}.tar.gz
# Source0-md5:	2a4bb58d27a5647dc42bbd4878600ee4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
CPANPLUS daje dostêp z linii poleceñ do interfejsu CPAN. Importowane
do przestrzeni nazw s± trzy funkcje: fetch, install i shell. Dodatkowo
get jest aliasem do fetch.

Mimo ¿e modu³u CPANPLUS mo¿na u¿ywaæ w skryptach, zaleca siê w takich
sytuacjach u¿ywaæ CPANPLUS::Backend. Oprócz dostarczania obiektowo
zorientowanego interfejsu, CPANPLUS::Backend jest bardziej wydajny ni¿
CPANPLUS przy wielu operacjach. CPANPLUS s³u¿y g³ównie do u¿ywania z
linii poleceñ, aby by³ wstecznie kompatybilny z CPAN.pm.

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
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
