# NOTES
#  - draws unwanted, additional X labels in comparison with 4.4.6

%define		php_min_version 5.2.0
Summary:	Class for creating esientific and business charts
Summary(pl.UTF-8):	Klasa do tworzenia naukowych i biznesowych wykresów
Name:		phplot
Version:	6.2.0
Release:	1
License:	LGPL v2.1, PHP
Group:		Libraries
Source0:	https://downloads.sourceforge.net/phplot/%{name}-%{version}.tar.gz
# Source0-md5:	a53917038aac2d3d0ccb4b148179c894
Source1:	https://downloads.sourceforge.net/phplot/%{name}docs-20151105.zip
# Source1-md5:	0c3af626c64ac2c55bdb3acd273d358b
URL:		http://phplot.sourceforge.net/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	unzip
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(gd)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdocdir	%{_docdir}/phpdoc

%description
PHPlot is a graph library for dynamic scientific, business, and
stock-market charts. PHPlot allows PHP developers to create pie
charts, bar graphs, line graphs, point graphs, etc. from a PHP
application.

Optionally uses TrueType (TTF) fonts. Includes Pie, Bar, Line, Area,
Point and other plot types.

%description -l pl.UTF-8
Klasa do tworzenia naukowych i biznesowych wykresów.

%package phpdoc
Summary:	PHPlot Reference Manual
Summary(pl.UTF-8):	Dokumentacja online do phplot
Group:		Documentation
Requires:	php-dirs

%description phpdoc
PHPlot Reference Manual.

%description phpdoc -l pl.UTF-8
Dokumentacja do phplot.

%prep
%setup -q -a1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/%{name}
cp -a *.php $RPM_BUILD_ROOT%{php_data_dir}/%{name}

install -d $RPM_BUILD_ROOT%{_phpdocdir}/%{name}
cp -a phplotdocs/* $RPM_BUILD_ROOT%{_phpdocdir}/%{name}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a contrib/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS* README*
%{php_data_dir}/%{name}
%{_examplesdir}/%{name}-%{version}

%files phpdoc
%defattr(644,root,root,755)
%{_phpdocdir}/%{name}
