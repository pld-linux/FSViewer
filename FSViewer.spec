Summary: 	FSViewer is a NeXT FileViewer lookalike for Window Maker.
Summary(pl):	FSViewer jest przeglądarką plików dla WindowMakera.
Name: 		FSViewer
Version: 	0.2.2
Release: 	1
Copyright: 	GPL
Group: 		X11/Window Managers/Tools
Group(pl):	X11/Zarządcy Okien/Narzędzia
Source0: 	http://www.csn.ul.ie/~clernong/download/FSViewer.app-%{version}.tar.gz
Source1:	http://www.csn.ul.ie/~clernong/download/icons.tar.gz
Source2:	FSViewer.desktop
URL: 		http://www.csn.ul.ie/~clernong/projects/fsviewer.html
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libPropList-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	WindowMaker-devel
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	zlib-devel
Requires:	WindowMaker >= 0.60.0
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
FSViewer is a NeXT FileViewer lookalike for Window Maker. Viewing is currently 
supported via browser mode. It has been written in C using the WINGs library.  

%description -l pl
FSViewer jest przeglądarką plików dla WindowMakera wyglądającą 
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

install -s defs/chdef   $RPM_BUILD_ROOT%{_prefix}/GNUstep/Apps/FSViewer.app
install xpm/*.xpm	$RPM_BUILD_ROOT%{_prefix}/GNUstep/Apps/FSViewer.app/xpm
install tiff/*		$RPM_BUILD_ROOT%{_prefix}/GNUstep/Apps/FSViewer.app/tiff
install %{SOURCE2}	$RPM_BUILD_ROOT/etc/X11/applnk/Utilities

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
