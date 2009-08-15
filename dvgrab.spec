%define name dvgrab
%define version 3.4
%define release %mkrel 3

Summary: DV grabber through the FireWire interface
Name: %name
Version: %version
Release: %release
License: GPLv2+
URl: http://www.kinodv.org/
Group: Video
Source0: http://prdownloads.sourceforge.net/kino/%{name}-%{version}.tar.gz
Patch0: dvgrab-3.3-fix-gcc-4.4-build.patch
Buildroot: %_tmppath/%name-buildroot
BuildRequires: libavc1394-devel libiec61883-devel libraw1394_8-devel
BuildRequires: libdv-devel libquicktime-devel
BuildRequires: jpeg-devel

%description
Dvgrab is a small utility that grabs AVI-2 video from a DV camera using the
IEEE-1394 bus (aka FireWire).

%prep
%setup -q
%patch0 -p1 -b .gcc44
perl -p -i -e 's/quicktime\/quicktime.h/lqt\/quicktime.h/g' filehandler.h

%build
%configure2_5x
%make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%_bindir/*
%_mandir/man1/*
