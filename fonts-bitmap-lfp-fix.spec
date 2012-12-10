Name: fonts-bitmap-lfp-fix
Summary: Linux Font Project fixed width bitmap fonts for X11
Version: 0.83
Release: %mkrel 6
Source0: http://ovh.dl.sourceforge.net/sourceforge/xfonts/lfpfonts-fix-src-0.83.tar.bz2
License: Public Domain
Group: System/Fonts/X11 bitmap
Url: http://dreamer.nitro.dk/typography/bitmap-fonts.html
BuildRequires: bdftopcf
BuildRequires: mkfontdir
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: fontconfig

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


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.83-6mdv2011.0
+ Revision: 675499
- br fontconfig for fc-query used in new rpm-setup-build

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.83-5mdv2011.0
+ Revision: 618311
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.83-4mdv2010.0
+ Revision: 428825
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.83-3mdv2009.0
+ Revision: 245253
- rebuild

* Fri Feb 22 2008 Gustavo De Nardin <gustavodn@mandriva.com> 0.83-1mdv2008.1
+ Revision: 173805
- import fonts-bitmap-lfp-fix


