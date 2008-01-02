%define name dvgrab
%define version 3.1
%define release %mkrel 1

Summary: DV grabber through the FireWire interface
Name: %name
Version: %version
Release: %release
License: GPL
URl: http://www.kinodv.org/
Group: Video
Source0: %name-%version.tar.bz2
Buildroot: %_tmppath/%name-buildroot
BuildRequires: libraw1394-devel libavc1394-devel libiec61883-devel
BuildRequires: libdv-devel libquicktime-devel
BuildRequires: jpeg-devel

%description
Dvgrab is a small utility that grabs AVI-2 video from a DV camera using the
IEEE-1394 bus (aka FireWire).

%prep
%setup -q 
perl -p -i -e 's/quicktime\/quicktime.h/lqt\/quicktime.h/g' filehandler.h

%build
%configure2_5x
%make

%install
rm -fr $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%_bindir/*
%_mandir/man1/*
