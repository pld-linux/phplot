Summary:	Class for creating esientific and business charts
Summary(pl):	Klasa do tworzenia naukowych i biznesowych wykresÛw
Name:		phplot
Version:	4.4.6
Release:	1
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
License:	GPL and PHP
Source0:	http://prdownloads.sourceforge.net/phplot/%{name}-%{version}.tar.gz
URL:		http://www.sourceforge.net/projects/phplot/
Requires:	php-common
Requires:	php-gd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
This routine is a class for creating scientific and business charts.

%description -l pl
Klasa do tworzenia naukowych i biznesowych wykresÛw.

%prep
%setup  -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

install *.php *.ttf	$RPM_BUILD_ROOT%{_phpsharedir}/%{name}

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*
%{_phpsharedir}/%{name}
