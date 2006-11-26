Summary:	Class for creating esientific and business charts
Summary(pl):	Klasa do tworzenia naukowych i biznesowych wykresów
Name:		phplot
Version:	4.4.6
Release:	4
License:	GPL/PHP
Group:		Libraries
Source0:	http://dl.sourceforge.net/phplot/%{name}-%{version}.tar.gz
# Source0-md5:	8a5b34e09fa29f20e31814cbd8c0d0b5
URL:		http://www.sourceforge.net/projects/phplot/
Requires:	php(gd)
Requires:	php-common
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
