Summary:	FSViewer is a NeXT FileViewer lookalike for Window Maker
Summary(pl):	FSViewer jest przegl±dark± plików dla WindowMakera
Name:		FSViewer
Version:	0.2.3
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.csn.ul.ie/~clernong/download/%{name}.app-%{version}.tar.gz
Source1:	http://www.csn.ul.ie/~clernong/download/icons.tar.gz
Source2:	%{name}.desktop
Patch0:		%{name}-ac_am15.patch
Patch1:		%{name}-WINGs.patch
Patch2:		%{name}-debian.patch
Patch3:		%{name}-no_libnsl.patch
URL:		http://www.csn.ul.ie/~clernong/projects/fsviewer.html
BuildRequires:	WindowMaker-devel >= 0.62.1
BuildRequires:	XFree86-devel
BuildRequires:	libPropList-devel >= 0.9.1
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	WindowMaker >= 0.61.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
FSViewer is a NeXT FileViewer lookalike for Window Maker. Viewing is
currently supported via browser mode. It has been written in C using
the WINGs library.

%description -l pl
FSViewer jest przegl±dark± plików dla WindowMakera wygl±daj±c± jak
NeXT FileViewer.

%prep
%setup -q -a1 -n FSViewer.app-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/GNUstep/Apps/FSViewer.app/{xpm,tiff} \
	$RPM_BUILD_ROOT%{_applnkdir}/Utilities

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install defs/chdef $RPM_BUILD_ROOT%{_prefix}/GNUstep/Apps/FSViewer.app
install xpm/*.xpm $RPM_BUILD_ROOT%{_prefix}/GNUstep/Apps/FSViewer.app/xpm
install tiff/* $RPM_BUILD_ROOT%{_prefix}/GNUstep/Apps/FSViewer.app/tiff
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

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

%{_applnkdir}/Utilities/FSViewer.desktop
