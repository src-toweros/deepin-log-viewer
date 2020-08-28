%bcond_with check

%global with_debug 1
%if 0%{?with_debug}
%global debug_package   %{nil}
%endif
Name:          deepin-log-viewer
Version:        5.6.1
Release:        2
Summary:        Log Viewer is a useful tool for viewing system logs.
License:        GPLv3+
URL:            https://uos-packages.deepin.com/uos/pool/main/d/deepin-log-viewer/
Source0:        %{name}-%{version}.orig.tar.xz


BuildRequires: qt5-qtbase-devel
BuildRequires: dtkcore-devel
BuildRequires: dtkwidget-devel
BuildRequires: dtkgui-devel
BuildRequires: deepin-gettext-tools
BuildRequires: qt5-linguist
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: systemd-devel

%description
Log Viewer is a useful tool for viewing system logs.


%prep
%autosetup

%build
export PATH=$PATH:/usr/lib64/qt5/bin
mkdir build && cd build
%{_libdir}/qt5/bin/qmake ..
%{__make}

%install
pushd %{_builddir}/%{name}-%{version}/build
%make_install INSTALL_ROOT=%{buildroot}
popd


%files
%{_bindir}/deepin-log-viewer
%{_bindir}/logViewerAuth
%{_datadir}/applications/deepin-log-viewer.desktop
%{_datadir}/deepin-log-viewer/translations/deepin-log-viewer.qm
%{_datadir}/deepin-log-viewer/translations/deepin-log-viewer_zh_CN.qm
%{_datadir}/icons/hicolor/scalable/apps/deepin-log-viewer.svg
%{_datadir}/polkit-1/actions/com.deepin.pkexec.logViewerAuth.policy
%doc README.md

%changelog
* Fri Aug 28 2020 chenbo pan <panchenbo@uniontech.com> - 5.0.10-2
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-1
- Package init
