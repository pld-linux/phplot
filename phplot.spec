#
# NOTES: - draws unwanted, additional X labels in comparison with 4.4.6
#
%define		_manual 20090121
#
Summary:	Class for creating esientific and business charts
Summary(pl.UTF-8):	Klasa do tworzenia naukowych i biznesowych wykresów
Name:		phplot
Version:	5.0.6
Release:	0.1
License:	GPL/PHP
Group:		Libraries
Source0:	http://dl.sourceforge.net/phplot/%{name}-%{version}.tar.gz
# Source0-md5:	80ccae467c550348c37f991e8ff81897
Source1:	http://dl.sourceforge.net/phplot/phplotdocs-%{_manual}.zip
# Source1-md5:	8500e3323910ace8cf4d9da97126a939
URL:		http://www.sourceforge.net/projects/phplot/
BuildRequires:	unzip
Requires:	php(gd)
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
This routine is a class for creating scientific and business charts.

%description -l pl.UTF-8
Klasa do tworzenia naukowych i biznesowych wykresów.

%prep
%setup -q -a1 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

install *.php $RPM_BUILD_ROOT%{_phpsharedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS* README* phplotdocs/*
%{_phpsharedir}/%{name}
