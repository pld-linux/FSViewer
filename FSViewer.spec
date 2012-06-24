Summary:	FSViewer is a NeXT FileViewer lookalike for Window Maker
Summary(pl):	FSViewer jest przegl�dark� plik�w dla Window Makera
Name:		FSViewer
Version:	0.2.5
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.bayernline.de/~gscholz/linux/fsviewer/%{name}.app-%{version}.tar.gz
# Source0-md5:	d1f849d1f955c35b18201860e485d332
Source2:	%{name}.desktop
Patch0:		http://www.bayernline.de/~gscholz/linux/fsviewer/FSViewer.app-0.2.5-WM-0.81.0.patch.gz
Patch1:		%{name}-no_libnsl.patch
URL:		http://www.bayernline.de/~gscholz/linux/fsviewer/
BuildRequires:	WindowMaker-devel >= 0.81.0-0.20040321.4
BuildRequires:	XFree86-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
# the rest is required for libwraster (but not all libs from WindowMaker-devel):
BuildRequires:	Hermes-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
# the end of libwraster deps
Requires:	WindowMaker >= 0.70.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# well, WindowMaker-like, not gnustep*-like - because:
# - it requires WindowMaker, not gnustep-*
# - it doesn't follow gnustep-* hierarchy inside *.app
%define		gsappsdir	%{_libdir}/GNUstep/Apps

%description
FSViewer is a NeXT FileViewer lookalike for Window Maker. Viewing is
currently supported via browser mode. It has been written in C using
the WINGs library.

%description -l pl
FSViewer jest przegl�dark� plik�w dla Window Makera wygl�daj�c� jak
NeXT FileViewer.

%prep
%setup -q -n FSViewer.app-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-appspath=%{gsappsdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install defs/chdef $RPM_BUILD_ROOT%{gsappsdir}/FSViewer.app
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{gsappsdir}/FSViewer.app
%attr(755,root,root) %{gsappsdir}/FSViewer.app/FSViewer
%attr(755,root,root) %{gsappsdir}/FSViewer.app/chdef
%{gsappsdir}/FSViewer.app/MagicFiles
%{gsappsdir}/FSViewer.app/xpm
%{gsappsdir}/FSViewer.app/tiff
%{_desktopdir}/FSViewer.desktop
