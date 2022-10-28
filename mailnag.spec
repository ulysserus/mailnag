Name: mailnag
Version: 2.2.0
Release: alt1

Summary: Mail notification daemon
License: GPLv2
Group: Networking/Mail

Url: https://github.com/pulb/mailnag
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: desktop-file-utils
#BuildRequires: libappstream-glib

Requires: gnome-keyring

%description
Mailnag checks POP3 and IMAP servers for new mail and when it finds one
creates a proper GNOME 3 notification that mentions sender and subject.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
desktop-file-validate %buildroot%_desktopdir/%name.desktop
desktop-file-validate %buildroot%_desktopdir/%name-config.desktop
#appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%_datadir/metainfo/*.appdata.xml
%find_lang %name

%files -f %name.lang
%doc AUTHORS LICENSE NEWS README.md
%_bindir/%name
%_bindir/%name-config
%_datadir/%name

#setup.py spells package name this way:
%python3_sitelibdir_noarch/Mailnag

#desktop apps
%_desktopdir/%name.desktop
%_desktopdir/%name-config.desktop

#app icons in various sizes
%_iconsdir/hicolor/*/apps/%name.png

#python meta info, not required for desktop app
#python3_sitelibdir/%name-*-*.egg-info

# Appstream folder, usable in Alt?
#_datadir/metainfo/

%changelog
* Fri Oct 28 2022 Ivan G <lordvivec@mail.ru> 2.2.0-alt1
- initial alt build

