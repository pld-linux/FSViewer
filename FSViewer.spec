%define name fsviewer
%define version 0.1.1
%define release 1
%define serial 3
%define prefix /usr

Summary: 	FSViewer is a NeXT FileViewer lookalike for Window Maker.
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Serial: 	%{serial}
Copyright: 	GPL
Group: 		X11/Utilities
URL: 		http://www.csn.ul.ie/~clernong/projects/fsviewer.html
Vendor: 	George Clernon <clernong@tinet.ie>
Source: 	http://www.csn.ul.ie/~clernong/download/FSViewer.app-%{version}.tar.gz
Prefix: 	%{prefix}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
FSViewer is a NeXT FileViewer lookalike for Window Maker. Viewing is currently 
supported via browser mode. It has been written in C using the WINGs library.  

**** For Use With Window Maker 0.51.x ****

%prep
%setup -q -n FSViewer.app-%{version}
CFLAGS=$RPM_OPT_FLAGS \
./configure --prefix=%{prefix}

%build
make

%install
if [ -e $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT%{prefix}/{bin,share}
make prefix=$RPM_BUILD_ROOT%{prefix} install
install -m 644 FSViewer $RPM_BUILD_ROOT%{prefix}/share/FSViewer.app/FSViewer

%post
cat <<EOM

==============================================================================
You must copy %{prefix}/share/FSViewer.app/FSViewer to ~/GNUstep/Defaults/
==============================================================================

EOM

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{prefix}/bin/fsviewer
%{prefix}/share/FSViewer.app

%changelog
* Wed Feb 23 1999 Ryan Weaver <ryanw@infohwy.com>
  [fsviewer-0.1.1-1]
- FSViewer.app-0.1.1 (19990223)
- o Commented out FSDisk related code in FSUtils.c, should fix
    some multi-platform compilation problems.
- o Added a patch to automatically detect HOME dir.
- o Fixed a bug that crashes the app if the inital path contains a
    long path component.
- o Zombie process are now cleaned up.
- o Fixed WMJustified bug (should be WAJustified) in inspector.c and 
    iconInspector.c
- o Implemented Revert in attributes inspector.
- o Initial launch path is now the users home dir.
- o Now checks return value of getpwuid and getgrgid calls in 
    attribsInspector.c, used to seg fault if either group or user
    was unknown.
- o Disabled hiding of app via 'h' key, leaving it up to Window Maker 
    and changed the quit key from 'q' to '^q' to prevent accidents :).
- o Added in a "Console" menu option under the "Tools" menu. It launches
    an xterm at the current directory.
- o The window and miniwindow icon titles are set with the current 
    selection.
- o Added in rudimentary magic files support. This allows certain kinds
    of unknown files to be viewed. 
- o Fixed bug wrt to displaying/hiding dot files.
- o Added in file filtering.

* Wed Feb  3 1999 Ryan Weaver <ryanw@infohwy.com>
  [fsviewer-0.1.0-1]
- FSViewer.app-0.1.0 (19990201)
- o Reorganised the initialisation of the app.
- o Multiple Windows can be opened.
- o Display hidden files.
- o Permissions can be set from attributes inspector.
- o Icons can be set for extensions from File Extension
    inspector.
- o Added legal panel.
- o Added info panel (broke app for other platforms though).
- o Tidied up code for file browsing to easily add other
    views.
- o In the process of moving odds and ends to FSUtils.c
- o Rewrote the scrollview code that displays the current path.
- o The window(s) can be resized in both width and height.
- o Using nodename from utsname struct as the hostname.
- o Using timestampWidget instead of timestamp in attribsInspector 
    as it can display the year.
- o Updated the configure script to take into account datadir value
    when generating the FSViewer default file.
- o Added in Cut, Copy, Paste, Rename, Delete and Link.
- o Inspector window now updates automatically if it is open.
- o Added in the shelf.
- o Added new file/directory creation.
- o Before launching an app, the pwd is changed to the selected dir.
- o Added in the Tools submenu and moved the Inspector there.
- o Created icons and src sub directories.

* Fri Dec 18 1998 Ryan Weaver <ryanw@infohwy.com>
  [fsviewer-0.0.2-1]
- FSViewer.app-0.0.2 (19981217)
- o Added in more checks to the configure script.
- o Replaced basename with GetNameFromPathname.
- o Using strrchr instead of rindex.
- o Searches the Window Maker defaults domain for IconPath
-   instead of PixmapPath
- o Using "/" if environment variable HOSTNAME is not set.
- o Added command line option to start FSViewer at a specified
-   path.


* Thu Dec 10 1998 Ryan Weaver <ryanw@infohwy.com>
  [fsviewer-19981214-1]
- First RPM
- 14/12/98
    The source code for FSViewer is now available. This is a preliminary
  release. It's not guaranteed to do anything. Hopefully it will compile and
  run straight out of the box. I'm currently working on getting it to compile
  on my Sun at work.
