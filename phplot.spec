Summary:	Class for creating esientific and business charts
Summary(pl):	Klasa do tworzenia naukowych i biznesowych wykresów
Name:		phplot
Version:	4.4.6
Release:	2
Group:		Libraries
License:	GPL/PHP
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
Klasa do tworzenia naukowych i biznesowych wykresów.

%prep
%setup  -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

install *.php *.ttf	$RPM_BUILD_ROOT%{_phpsharedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* doc/*
%{_phpsharedir}/%{name}
