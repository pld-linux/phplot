#
%define		_rc 3
%define		_manual 20061201
#
Summary:	Class for creating esientific and business charts
Summary(pl):	Klasa do tworzenia naukowych i biznesowych wykres�w
Name:		phplot
Version:	5.0
Release:	%{?_rc:0.rc%{_rc}}.0.1
License:	GPL/PHP
Group:		Libraries
Source0:	http://dl.sourceforge.net/phplot/%{name}-%{version}%{?_rc:rc%{_rc}}.tar.gz
# Source0-md5:	ddd9f4877c6f0a0b629ada1ce2bc4772
Source1:	http://dl.sourceforge.net/phplot/phplotdocs-%{_manual}.zip
# Source1-md5:	61cd9ef5fa6ac1c74d98b85fb7af816a
URL:		http://www.sourceforge.net/projects/phplot/
BuildRequires:	unzip
Requires:	php(gd)
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpsharedir	%{_datadir}/php

%description
This routine is a class for creating scientific and business charts.

%description -l pl
Klasa do tworzenia naukowych i biznesowych wykres�w.

%prep
%setup -q -n %{name}-%{version}%{?_rc:rc%{_rc}} -a1 

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
