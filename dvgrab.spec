%define name dvgrab
%define version 3.5
%define release %mkrel 5

Summary: DV grabber through the FireWire interface
Name: %name
Version: %version
Release: %release
License: GPLv2+
URl: http://www.kinodv.org/
Group: Video
Source0: http://prdownloads.sourceforge.net/kino/%{name}-%{version}.tar.gz
Buildroot: %_tmppath/%name-buildroot
BuildRequires: libavc1394-devel libiec61883-devel libraw1394-devel
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
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TODO
%_bindir/*
%_mandir/man1/*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 3.5-5mdv2011.0
+ Revision: 663899
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 3.5-4mdv2011.0
+ Revision: 604836
- rebuild

* Fri Jan 15 2010 Emmanuel Andry <eandry@mandriva.org> 3.5-3mdv2010.1
+ Revision: 491797
- use latest libraw1394

* Sun Jan 10 2010 Oden Eriksson <oeriksson@mandriva.com> 3.5-2mdv2010.1
+ Revision: 488748
- rebuilt against libjpeg v8

* Wed Sep 09 2009 Frederik Himpe <fhimpe@mandriva.org> 3.5-1mdv2010.0
+ Revision: 435928
- Update to new version 3.5

* Sat Aug 15 2009 Oden Eriksson <oeriksson@mandriva.com> 3.4-3mdv2010.0
+ Revision: 416650
- rebuilt against libjpeg v7

* Mon Aug 10 2009 Funda Wang <fwang@mandriva.org> 3.4-2mdv2010.0
+ Revision: 414136
- fix build with gcc44

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Tue Feb 24 2009 Antoine Ginies <aginies@mandriva.com> 3.4-1mdv2009.1
+ Revision: 344359
- new release 3.4

* Thu Jan 29 2009 Funda Wang <fwang@mandriva.org> 3.3-1mdv2009.1
+ Revision: 335169
- new version 3.3

* Fri Aug 08 2008 Frederik Himpe <fhimpe@mandriva.org> 3.2-1mdv2009.0
+ Revision: 269537
- Update to version 3.2
- Fix license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 12 2007 Giuseppe Ghibò <ghibo@mandriva.com> 3.1-1mdv2008.1
+ Revision: 119032
- Release 3.1.

* Tue Aug 07 2007 Austin Acton <austin@mandriva.org> 3.0-1mdv2008.0
+ Revision: 59983
- new version
- clean spec

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 2.1-1mdv2008.0
+ Revision: 29462
- add libiec61883 buildrequires
- release 2.1
- Import dvgrab



* Tue Aug 30 2005 Austin Acton <austin@mandriva.org> 1.8-1mdk
- New release 1.8

* Fri Mar 18 2005 Austin Acton <austin@mandrake.org> 1.7-1mdk
- 1.7
- source URL

* Tue Aug 10 2004 Austin Acton <austin@mandrake.org> 1.6-1mdk
- 1.6

* Sun May 23 2004 Austin Acton <austin@mandrake.org> 1.5-2mdk
- rebuild for new libdv
- minor cleaning
- configure 2.5

* Sun Jan 25 2004 Austin Acton <austin@mandrake.org> 1.5-1mdk
- 1.5

* Mon Jan 12 2004 Franck Villaume <fvill@freesurf.fr> 1.4-2mdk
- add some BuildRequires

* Tue Nov 26 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.4-1mdk
- 1.4

* Sat Sep 27 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.3-1mdk
- 1.3
 
* Tue Mar 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2-2mdk
- fix requires

* Mon Feb 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2-1mdk
- 1.2

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1-0.2b3mdk
- rebuild

* Mon Sep 02 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1-0.1b3mdk
- rebuild

* Wed Jun 26 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1-0.1b2mdk
- rebuild

* Tue Mar 26 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.1-0.1b1mdk
- new release:
	* Writing of large (>2 GByte) AVI files is now supported.
	* A commandline	parameter for choosing between different AVI index records
	  was added to improve compatibility with legacy and Windows software)
- add %%doc AUTHORS ChangeLog COPYING TODO
- remove references to inexistant docs
- put a real Summary
- requires a recent enough kernel
- add BuildRequires: libraw1394 >= 0.6
- enhanced description

* Mon Sep 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.01-1mdk
- updated by Gregoire Colbert <gregus@linux-mandrake.com> 

* Sun Aug 26 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0-1mdk
- updated to 1.0

* Tue Jan 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.89-1mdk
- updated to 0.89

* Wed Jul 05 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.84-1mdk
- new release
- change group for Video

* Mon Jul 03 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.83-1mdk
- initial spec
