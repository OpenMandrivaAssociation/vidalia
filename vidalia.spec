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
