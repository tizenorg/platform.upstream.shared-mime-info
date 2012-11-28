Name:           shared-mime-info
Version:        1.0
Release:        0
License:        GPL-2.0+
Summary:        Shared MIME Database
Url:            http://freedesktop.org/wiki/Software/shared-mime-info
Group:          System/X11/Utilities
Source:         http://people.freedesktop.org/~hadess/%{name}-%{version}.tar.xz
Source1:        mime-info-to-mime
Source2:        macros.shared-mime-info
BuildRequires:  intltool
# needed for xmllint
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       /usr/bin/fgrep
# needed by mime-info-to-mime:
Requires:       /usr/bin/mkdir
Requires:       /usr/bin/rm
# libgio-2_0-0 Requires: shared-mime-info, but this can't exist yet. We explicitly ignore this dependency here.
#!BuildIgnore:  shared-mime-info
# needed by update-mime-database
Provides:       %{name}-devel = %{version}

%description
This package contains:

- The freedesktop.org shared MIME database spec.

- The merged GNOME and KDE databases, in the new format.

- The update-mime-database command, used to install new MIME data.

%prep
%setup -q

%build
export CFLAGS=`echo $RPM_OPT_FLAGS |sed -e 's/atom/i686/g'`
%configure 
make V=1

%install
%make_install
install %{SOURCE1} %{buildroot}%{_bindir}/
%find_lang %{name} %{?no_lang_C}
# Install rpm macros
install -D -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/rpm/macros.shared-mime-info


%post
%{_bindir}/update-mime-database %{_datadir}/mime || true

%lang_package

%docs_package

%files
%defattr (-, root, root)
%license COPYING
%{_bindir}/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/pkgconfig/*.pc
%ghost %{_datadir}/mime/[a-ms-vxX]*
%{_sysconfdir}/rpm/macros.shared-mime-info

%changelog
