#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v13
# autospec commit: dc0ff31
#
# Source0 file verified with key 0x76E6FEEC95FC5E22 (smd.seandavis@gmail.com)
#
Name     : lightdm-gtk-greeter
Version  : 2.0.9
Release  : 9
URL      : https://github.com/Xubuntu/lightdm-gtk-greeter/releases/download/lightdm-gtk-greeter-2.0.9/lightdm-gtk-greeter-2.0.9.tar.gz
Source0  : https://github.com/Xubuntu/lightdm-gtk-greeter/releases/download/lightdm-gtk-greeter-2.0.9/lightdm-gtk-greeter-2.0.9.tar.gz
Source1  : https://github.com/Xubuntu/lightdm-gtk-greeter/releases/download/lightdm-gtk-greeter-2.0.9/lightdm-gtk-greeter-2.0.9.tar.gz.asc
Source2  : 76E6FEEC95FC5E22.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: lightdm-gtk-greeter-bin = %{version}-%{release}
Requires: lightdm-gtk-greeter-data = %{version}-%{release}
Requires: lightdm-gtk-greeter-license = %{version}-%{release}
Requires: lightdm-gtk-greeter-locales = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file
BuildRequires : gettext
BuildRequires : gnupg
BuildRequires : gobject-introspection-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(exo-2)
BuildRequires : pkgconfig(gmodule-export-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(liblightdm-gobject-1)
BuildRequires : pkgconfig(libxklavier)
BuildRequires : pkgconfig(x11)
BuildRequires : xfce4-dev-tools
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# LightDM GTK Greeter
**LightDM GTK Greeter** is a greeter that has moderate requirements (GTK).

%package bin
Summary: bin components for the lightdm-gtk-greeter package.
Group: Binaries
Requires: lightdm-gtk-greeter-data = %{version}-%{release}
Requires: lightdm-gtk-greeter-license = %{version}-%{release}

%description bin
bin components for the lightdm-gtk-greeter package.


%package data
Summary: data components for the lightdm-gtk-greeter package.
Group: Data

%description data
data components for the lightdm-gtk-greeter package.


%package doc
Summary: doc components for the lightdm-gtk-greeter package.
Group: Documentation

%description doc
doc components for the lightdm-gtk-greeter package.


%package license
Summary: license components for the lightdm-gtk-greeter package.
Group: Default

%description license
license components for the lightdm-gtk-greeter package.


%package locales
Summary: locales components for the lightdm-gtk-greeter package.
Group: Default

%description locales
locales components for the lightdm-gtk-greeter package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 76E6FEEC95FC5E22' gpg.status
%setup -q -n lightdm-gtk-greeter-2.0.9
cd %{_builddir}/lightdm-gtk-greeter-2.0.9
pushd ..
cp -a lightdm-gtk-greeter-2.0.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719973199
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719973199
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lightdm-gtk-greeter
cp %{_builddir}/lightdm-gtk-greeter-%{version}/COPYING %{buildroot}/usr/share/package-licenses/lightdm-gtk-greeter/31a3d460bb3c7d98845187c716a30db81c44b615 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang lightdm-gtk-greeter
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/lightdm-gtk-greeter
/usr/bin/lightdm-gtk-greeter

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/scalable/places/budgie-desktop_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/cinnamon2d_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/cinnamon_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/gnome-classic_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/gnome-fallback-compiz_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/gnome-fallback_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/gnome-flashback-compiz_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/gnome-flashback_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/gnome-shell_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/gnome_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/kde-plasma_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/kde_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/lubuntu_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/lxde_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/lxqt_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/mate_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/pantheon_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/ubuntu-2d_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/ubuntu_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/ubuntustudio_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/wmaker-common_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/xfce_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/xterm_badge-symbolic.svg
/usr/share/icons/hicolor/scalable/places/xubuntu_badge-symbolic.svg
/usr/share/xgreeters/lightdm-gtk-greeter.desktop

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/lightdm\-gtk\-greeter/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lightdm-gtk-greeter/31a3d460bb3c7d98845187c716a30db81c44b615

%files locales -f lightdm-gtk-greeter.lang
%defattr(-,root,root,-)

