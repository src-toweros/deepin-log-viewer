Name:          deepin-log-viewer
Version:        5.8.0.23
Release:        1
Summary:        Log Viewer is a useful tool for viewing system logs.
License:        GPLv3+
URL:            https://github.com/linuxdeepin/deepin-log-viewer
Source0:        %{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake3
BuildRequires: dtkcore-devel
BuildRequires: dtkwidget-devel
BuildRequires: systemd-devel
BuildRequires: libicu-devel
BuildRequires: qt5-devel

%description
%{summary}.

%prep
%autosetup

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
sed -i "s|^cmake_minimum_required.*|cmake_minimum_required(VERSION 3.0)|" $(find . -name "CMakeLists.txt")
mkdir build && pushd build
%cmake -DCMAKE_BUILD_TYPE=Release ../  -DAPP_VERSION=%{version} -DVERSION=%{version}
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/logViewerAuth
%{_bindir}/logViewerTruncate
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/translations/%{name}*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/polkit-1/actions/*.policy

%changelog
* Mon Jul 12 2021 weidong <weidong@uniontech.com> - 5.8.0.23-1
- Update 5.8.0.23

* Fri Aug 28 2020 chenbo pan <panchenbo@uniontech.com> - 5.0.10-2
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.1-1
- Package init
