Summary:	DV grabber through the FireWire interface
Name:		dvgrab
Version:	3.5
Release:	19
License:	GPLv2+
Group:		Video
Url:		http://www.kinodv.org/
Source0:	http://prdownloads.sourceforge.net/kino/%{name}-%{version}.tar.gz
# https://github.com/ddennedy/dvgrab/commit/8dd729f2cf4cc5b99ad2e3961419cf71d2dfb843.patch
Patch0:  dvgrab-gcc6.patch
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libavc1394)
BuildRequires:	pkgconfig(libdv)
BuildRequires:	pkgconfig(libiec61883)
BuildRequires:	pkgconfig(libquicktime)
BuildRequires:	pkgconfig(libraw1394)
BuildRequires:  pkgconfig(zlib)

%description
Dvgrab is a small utility that grabs AVI-2 video from a DV camera using the
IEEE-1394 bus (aka FireWire).

%prep
%autosetup -p1
sed -i -e 's/quicktime\/quicktime.h/lqt\/quicktime.h/g' filehandler.h

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog README TODO
%{_bindir}/*
%doc %{_mandir}/man1/*
