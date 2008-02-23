#
# TODO:
#  - should probably install itself into vendorlib dir, not vendorarch
#  - ajax example does not work
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Jemplate
Summary:	Jemplate - Javascript Templating with Template Toolkit
Summary(pl.UTF-8):	Jemplate - szablony javascriptowe z użyciem Template Toolkitu
Name:		perl-Jemplate
Version:	0.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/I/IN/INGY/%{pdir}-%{version}.tar.gz
# Source0-md5:	4d344f5c27543f14728a7bf24abff617
URL:		http://search.cpan.org/dist/Jemplate/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Template-Toolkit >= 2.14
%endif
# no arch stuff, but installs to vendorarch dir
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jemplate is a templating framework for Javascript that is built over
Perl's Template Toolkit (TT2).

Jemplate parses TT2 templates using the TT2 Perl framework, but with a
twist. Instead of compiling the templates into Perl code, it compiles
them into Javascript.

Jemplate then provides a Javascript runtime module for processing
the template code. Presto, we have full featured Javascript
templating language!

Combined with JSON and xmlHttpRequest, Jemplate provides a really
simple and powerful way to do Ajax stuff.

%description -l pl.UTF-8
Jemplate to szkielet szablonów dla Javascriptu stworzony w oparciu o
perlowy Template Toolkit (TT2).

Jemplate analizuje szablony TT2 przy użyciu perlowego szkieletu TT2,
ale z modyfikacją: zamiast kompilować szablony do kodu w Perlu,
kompiluje je do Javascriptu.

Jemplate udostępnia moduł uruchomieniowy Javascriptu do przetwarzania
kodu szablonów. W ten sposób mamy w pełni funkcjonalny język szablonów
dla Javascriptu!

W połączeniu z JSON i xmlHttpRequest Jemplate udostępnia naprawdę
proste i potężne metody obsługi technologii Ajax.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/share
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Jemplate/Jemplate.js \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/share

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/auto/Jemplate
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/Jemplate
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
