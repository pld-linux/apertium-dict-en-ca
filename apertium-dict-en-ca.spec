Summary:	English-Catalan language pair for Apertium
Summary(pl.UTF-8):	Para języków angielski-kataloński dla Apertium
%define	lpair	en-ca
Name:		apertium-dict-%{lpair}
Version:	0.9.3
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	c984145a73c10c332c45b92bb676c37a
URL:		http://www.apertium.org/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox >= 3.2.0
BuildRequires:	pkgconfig
Requires:	apertium >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apertium language pair, which can be used for translating
between English and Catalan, morphological analysis or part-of-speech
tagging of both languages.

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między angielskim a katalońskim, a także analizy morfologicznej lub
oznaczania części mowy w obu językach.

%prep
%setup -q -n apertium-%{lpair}-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apertium/modes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not needed here (see modes subdir) and contain wrong (builddir) paths
%{__rm} $RPM_BUILD_ROOT%{_datadir}/apertium/apertium-%{lpair}/*.mode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/ca-en.mode
%{_datadir}/apertium/modes/ca-en-multi.mode
%{_datadir}/apertium/modes/ca-en_US.mode
%{_datadir}/apertium/modes/en-ca.mode
%{_datadir}/apertium/modes/en-ca-multi.mode
%{_datadir}/apertium/modes/val-en-ca.mode
