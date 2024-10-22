%global  kf_version 6.6.0

Name:    kf6-kxmlgui
Version: 6.6.0
Release: 0%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for user-configurable main windows
License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/kxmlgui
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  kf6-kcolorscheme-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kitemviews-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qttools-devel

%description
KDE Frameworks 6 Tier 3 solution for user-configurable main windows.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-kconfig-devel
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6 -DFORCE_DISABLE_KGLOBALACCEL=ON
%cmake_build

%install
%cmake_install
# Own the kxmlgui directory
mkdir -p %{buildroot}%{_kf6_datadir}/kxmlgui5/
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kxmlgui.*
%{_kf6_libdir}/libKF6XmlGui.so.*
%dir %{_kf6_datadir}/kxmlgui5/

%files devel
%{_kf6_qtplugindir}/designer/*6widgets.so
%{_kf6_includedir}/KXmlGui/
%{_kf6_libdir}/libKF6XmlGui.so
%{_kf6_libdir}/cmake/KF6XmlGui/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
