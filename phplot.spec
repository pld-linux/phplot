# NOTES
#  - draws unwanted, additional X labels in comparison with 4.4.6

%define		manual 20090614
Summary:	Class for creating esientific and business charts
Summary(pl.UTF-8):	Klasa do tworzenia naukowych i biznesowych wykresów
Name:		phplot
Version:	5.0.7
Release:	1
License:	GPL/PHP
Group:		Libraries
Source0:	http://dl.sourceforge.net/phplot/%{name}-%{version}.tar.gz
# Source0-md5:	c19b733fed664014cc1e4e2c6ae3bf44
Source1:	http://dl.sourceforge.net/phplot/%{name}docs-%{manual}.zip
# Source1-md5:	b2efead25f95f4e263011cfa1756a4da
URL:		http://www.sourceforge.net/projects/phplot/
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	unzip
Requires:	php-common
Requires:	php-gd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{php_data_dir}/%{name}
%define		_phpdocdir	%{_docdir}/phpdoc

%description
A graph library for dynamic scientific, business, and stock-market
charts. Written in PHP; requires PHP5 and GD.

Optionally uses TrueType (TTF) fonts. Includes Pie, Bar, Line, Area,
Point and other plot types.

%description -l pl.UTF-8
Klasa do tworzenia naukowych i biznesowych wykresów.

%package phpdoc
Summary:	Online manual for phplot
Summary(pl.UTF-8):	Dokumentacja online do phplot
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for phplot.

%description phpdoc -l pl.UTF-8
Dokumentacja do phplot.

%prep
%setup -q -a1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a *.php $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_phpdocdir}/%{name}
cp -a phplotdocs/* $RPM_BUILD_ROOT%{_phpdocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS* README*
%{_appdir}

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{name}
