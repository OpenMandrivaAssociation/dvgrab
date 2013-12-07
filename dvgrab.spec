Summary:	DV grabber through the FireWire interface
Name:		dvgrab
Version:	3.5
Release:	8
License:	GPLv2+
Group:		Video
Url:		http://www.kinodv.org/
Source0:	http://prdownloads.sourceforge.net/kino/%{name}-%{version}.tar.gz

BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libdv)
BuildRequires:	pkgconfig(libiec61883)
BuildRequires:	pkgconfig(libquicktime)
BuildRequires:	pkgconfig(libraw1394)

%description
Dvgrab is a small utility that grabs AVI-2 video from a DV camera using the
IEEE-1394 bus (aka FireWire).

%prep
%setup -q
sed -i -e 's/quicktime\/quicktime.h/lqt\/quicktime.h/g' filehandler.h

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README TODO
%{_bindir}/*
%{_mandir}/man1/*

