Summary: 	FSViewer is a NeXT FileViewer lookalike for Window Maker.
Summary(pl):	FSViewer jest przegl±dark± plików dla WindowMakera.
Name: 		FSViewer
Version: 	0.2.1
Release: 	2
Copyright: 	GPL
Group: 		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
URL: 		http://www.csn.ul.ie/~clernong/projects/fsviewer.html
Source0: 	http://www.csn.ul.ie/~clernong/download/FSViewer.app-%{version}.tar.gz
Source1:	http://www.csn.ul.ie/~clernong/download/icons.tar.gz
Source2:	FSViewer.desktop
BuildPrereq:	libjpeg-devel
BuildPrereq:	libpng-devel
BuildPrereq:	libPropList-devel
BuildPrereq:	libtiff-devel
BuildPrereq:	libungif-devel
BuildPrereq:	WindowMaker-devel
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildPrereq:	zlib-devel
Requires:	WindowMaker >= 0.53
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
FSViewer is a NeXT FileViewer lookalike for Window Maker. Viewing is currently 
supported via browser mode. It has been written in C using the WINGs library.  

%description -l pl
FSViewer jest przegl±dark± plików dla WindowMakera wygl±daj±c± 
jak NeXT FileViewer.

%prep
%setup -q -a1 -n FSViewer.app-%{version}
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-extralibs=" -lPropList"

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/GNUstep/Apps/FSViewer.app/{xpm,tiff} \
	$RPM_BUILD_ROOT/etc/X11/applnk/Utilities

make install-strip DESTDIR=$RPM_BUILD_ROOT

install xpm/*.xpm $RPM_BUILD_ROOT%{_prefix}/GNUstep/Apps/FSViewer.app/xpm
install tiff/* $RPM_BUILD_ROOT%{_prefix}/GNUstep/Apps/FSViewer.app/tiff
install -s defs/chdef $RPM_BUILD_ROOT%{_prefix}/GNUstep/Apps/FSViewer.app
install %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/applnk/Utilities

gzip -9nf AUTHORS ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,README}.gz

%dir %{_prefix}/GNUstep/Apps/FSViewer.app
%attr(755,root,root) %{_prefix}/GNUstep/Apps/FSViewer.app/FSViewer
%attr(755,root,root) %{_prefix}/GNUstep/Apps/FSViewer.app/chdef

%{_prefix}/GNUstep/Apps/FSViewer.app/MagicFiles
%{_prefix}/GNUstep/Apps/FSViewer.app/xpm
%{_prefix}/GNUstep/Apps/FSViewer.app/tiff

/etc/X11/applnk/Utilities/FSViewer.desktop

%changelog
* Wed Jun 23 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [0.2.0-1]
- modified for PLD use,
- based on spec file by Ryan Weaver <ryanw@infohwy.com>.
