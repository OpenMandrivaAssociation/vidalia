Name:           vidalia
Version:        0.1.15
Release:        %mkrel 1
Epoch:          0
Summary:        Cross-platform controller GUI for Tor, built using the Qt framework
License:        GPLv2+
Group:          Networking/Other
URL:            http://www.vidalia-project.net/
Source0:        http://vidalia-project.net:8001/vidalia/vidalia-%{version}.tar.gz
Source1:        http://vidalia-project.net:8001/vidalia/vidalia-%{version}.tar.gz.asc
Source2:        vidalia.desktop
Patch0:         vidalia-paths.patch
Requires:       tor
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  openssl-devel
BuildRequires:  qt4-devel
BuildRequires:  qt4-linguist
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch0 -p1

%build
%cmake_qt4
%make
cd ../doc
doxygen

%install
%{__rm} -rf %{buildroot}
%makeinstall_std -C build

%{__install} -D -p -m 644 doc/vidalia.1 %{buildroot}%{_mandir}/man1/vidalia.1

%{_bindir}/desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-Internet-Other" \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/*

%{__install} -D -p -m 644 src/vidalia/res/128x128/tor-logo.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files
%defattr(0644,root,root,0755)
%doc CHANGELOG CREDITS HACKING INSTALL LICENSE LICENSE-GPLV2 LICENSE-GPLV3 LICENSE-LGPLV3 LICENSE-OPENSSL README doc/TODO doc/*.txt doc/html
%attr(0755,root,root) %{_bindir}/vidalia 
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
