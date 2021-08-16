Summary:	SIL Graphite Compiler
Summary(pl.UTF-8):	Kompilator SIL Graphite
Name:		grcompiler
Version:	4.2
Release:	11
License:	CPL v0.5+ or LGPL v2.1+
Group:		Applications
Source0:	http://downloads.sourceforge.net/silgraphite/%{name}-%{version}.tar.gz
# Source0-md5:	3df5dde12211d7d7e06a9e23306e5fe4
Patch0:		%{name}-make.patch
URL:		http://silgraphite.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	docbook2X >= 0.8.8-4
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SIL Graphite compiler builds a Graphite enabled font from a smart
font description, written in GDL (Graphite Description Language) and a
TrueType font by adding extra TrueType tables to it which the Graphite
engine can interpret.

%description -l pl.UTF-8
Kompilator SIL Graphite tworzy font Graphite z opisu inteligentnego
fontu, napisanego w języku GDL (Graphite Description Language) oraz
fontu TrueType poprzez dodanie dodatkowych tablic TrueType, które
potrafi zinterpretować silnik Graphite.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
cd test/GrcRegressionTest
%{__aclocal}
%{__autoconf}
%{__automake}
cd ../..
export CXXFLAGS="%{rpmcxxflags} -std=c++98"
%configure \
	DOCBOOK2MAN=/usr/bin/docbook2X2man
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/grcompiler

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO license/{LICENSING.txt,License_CPLv05.txt} doc/{README.gdlpp,*.pdf}
%attr(755,root,root) %{_bindir}/gdlpp
%attr(755,root,root) %{_bindir}/grcompiler
%{_datadir}/grcompiler
%{_mandir}/man1/gdlpp.1*
%{_mandir}/man1/grcompiler.1*
