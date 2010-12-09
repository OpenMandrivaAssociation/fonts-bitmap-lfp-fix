Name: fonts-bitmap-lfp-fix
Summary: Linux Font Project fixed width bitmap fonts for X11
Version: 0.83
Release: %mkrel 5
Source0: http://ovh.dl.sourceforge.net/sourceforge/xfonts/lfpfonts-fix-src-0.83.tar.bz2
License: Public Domain
Group: System/Fonts/X11 bitmap
Url: http://dreamer.nitro.dk/typography/bitmap-fonts.html
BuildRequires: bdftopcf
BuildRequires: mkfontdir
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
This package is a part of bigger project -- Linux Font Project. It includes
fixed width (character cell) fonts for X in PCF format.

The project is now inactive, but the fonts are still good.

%prep
%setup -q -n lfpfonts-fix-src

%build
pushd src
# use the provided ucs2any script, ucs2any from x11-font-util crashes badly
PATH=.:$PATH ./compile 2>/dev/null
popd
pushd lfp-fix
mkfontdir
popd


%install
rm -rf %{buildroot}
mkdir -p %buildroot%_datadir/fonts %buildroot%_sysconfdir/X11/fontpath.d
cp -pr lfp-fix %buildroot%_datadir/fonts/
ln -s ../../..%_datadir/fonts/lfp-fix \
   %buildroot%_sysconfdir/X11/fontpath.d/lfp-fix:unscaled:pri=50


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %_datadir/fonts/lfp-fix
%_datadir/fonts/lfp-fix/*
%_sysconfdir/X11/fontpath.d/lfp-fix:unscaled:pri=50
