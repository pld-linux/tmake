Summary:	Easy-to-use tool for creating and maintaining portable makefiles
Summary(pl):	£atwe_w_u¿ytkowaniu narzêdzie do tworzenia i zarz±dzania przeno¶nymi makefile'ami
Name:		tmake
Version:	1.8
Release:	1
License:	BSD-like
Group:		Development/Building
Source0:	ftp://ftp.troll.no/freebies/tmake/%{name}-%{version}.tar.gz
URL:		http://www.troll.no/freebies/tmake.html
Requires:	perl >= 5.001
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an easy-to-use tool for creating and maintaining makefiles
across many platforms and compilers. The idea is that you should spend
your time writing code, not makefiles.

%description -l pl
Jest to £atwe_w_u¿ytkowaniu narzêdzie do tworzenia i zarz±dzania 
makefile'ami po¶ród wielu platform i kompilatorów. Idea jest taka, ¿e
powiniene¶ spêdzaæ czas pisz±c kod, a nie Makefile.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/tmake,%{_bindir}}

install bin/progen $RPM_BUILD_ROOT%{_bindir}
install lib/unix/*.t $RPM_BUILD_ROOT%{_datadir}/tmake
sed 's@$(QTDIR)@/usr/X11R6@;s@^TMAKE_INCDIR_QT.*@TMAKE_INCDIR_QT		= /usr/X11R6/include/qt@' \
	lib/linux-g++/tmake.conf > $RPM_BUILD_ROOT%{_datadir}/tmake/tmake.conf
sed "s@\$ENV{\"TMAKEPATH\"}@\"%{_datadir}/tmake\"@" bin/tmake > $RPM_BUILD_ROOT%{_bindir}/tmake

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/* example
%attr(755,root,root) %{_bindir}/*
%{_datadir}/tmake
