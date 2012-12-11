Name:           vidalia
Version:        0.2.15
Release:        1
Epoch:          0
Summary:        Cross-platform controller GUI for Tor, built using the Qt framework
License:        GPLv2+
Group:          Networking/Other
URL:            http://www.torproject.org/projects/vidalia
Source0:        http://www.torproject.org/dist/vidalia/%{name}-%{version}.tar.gz
Requires:       tor
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  openssl-devel
BuildRequires:  qt4-devel
BuildRequires:  qt4-linguist

%description
Vidalia is a cross-platform controller GUI for Tor, built using the Qt 
framework. Vidalia runs on any platform supported by Qt 4.1, including 
Windows, Mac OS X, and Linux or other Unix variants using the X11 
window system.

Vidalia allows you to start and stop Tor, view the status of Tor at a 
glance, and monitor Tor's bandwidth usage. Vidalia also makes it easy 
to contribute to the Tor network by helping you setup a Tor server, if 
you wish.

%prep
%setup -q

%build
%cmake_qt4
%make
# make the docs
make doxygen

%install
%makeinstall_std -C build

install -D -p -m 644 doc/vidalia.1 %{buildroot}%{_mandir}/man1/vidalia.1

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-Internet-Other" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG CREDITS HACKING LICENSE README README.marble
%doc build/doc/html
%{_bindir}/vidalia
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png 
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Nov 25 2011 Alexander Khrukin <akhrukin@mandriva.org> 0:0.2.15-1
+ Revision: 733367
- version update to 0.2.15

* Tue May 10 2011 Sandro Cazzaniga <kharec@mandriva.org> 0:0.2.12-1
+ Revision: 673231
- drop an unused patch
- new version
- upstream doesn't propose an sig anymore.

* Fri Oct 22 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0:0.2.10-1mdv2011.0
+ Revision: 587259
- update to 0.2.10
- update URL and Source tags to current locations

* Tue Aug 31 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0:0.2.9-1mdv2011.0
+ Revision: 574562
- update to 0.2.9
- rediff paths patch
- use make to build the doxygen docs
- clean spec and update file list

* Thu Dec 24 2009 Jérôme Brenier <incubusss@mandriva.org> 0:0.1.15-1mdv2010.1
+ Revision: 481945
- drop desktop file (Source2), one is already included
- new version 0.1.15
- rediff/redo P0
- drop hicolor icons manual installation (already done during install)
- fix file list

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Nov 27 2008 Funda Wang <fwang@mandriva.org> 0:0.1.10-1mdv2009.1
+ Revision: 307202
- new version 0.1.10

* Sat Aug 16 2008 David Walluck <walluck@mandriva.org> 0:0.1.7-1mdv2009.0
+ Revision: 272835
- BuildRequires: openssl-devel
- BuildRequires: cmake
- add sources
- 0.1.7

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Sep 05 2007 David Walluck <walluck@mandriva.org> 0:0.0.14-1mdv2008.0
+ Revision: 80406
- 0.0.14
- rediff paths patch
- no need to BuildRequires: gcc-c++
- fix build with Qt4

