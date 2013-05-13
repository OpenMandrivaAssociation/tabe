%define	major 2
%define libname %mklibname tabe %{major}
%define develname %mklibname tabe -d

Summary:	Chinese lexicons library for xcin-2.5
Name:		tabe
Version:	0.2.6
Release:	14
License:	BSD style
Group:		System/Libraries
URL:		http://libtabe.sourceforge.net/
Source:		%{name}-%{version}.tar.bz2
Patch0:		http://ftp.de.debian.org/debian/pool/main/libt/libtabe/libtabe_0.2.6-1.2.diff.gz
Patch1:		tabe-0.2.6-link.patch
BuildRequires:	db-devel
BuildRequires:	pkgconfig(x11)
Requires:	%{libname} = %{version}-%{release}
Requires:	locales-zh
Provides:	libtabe = %{version}-%{release}
Obsoletes:	libtabe
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Chinese lexicons library for xcin-2.5's bimsphone input method.

%package -n	%{libname}
Summary:	Libraries needed to use packages using libtabe
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n	%{libname}
Chinese lexicons library for xcin-2.5's bimsphone input method.

This package contains shared libraries.

%package -n	%{develname}
Summary:	Header files and libraries for developing apps which will use libtabe
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname tabe 2 -d}

%description -n	%{develname}
Chinese lexicons library for xcin-2.5's bimsphone input method.

This package contains static libraries and headers files.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p0

%build
export CFLAGS="%optflags %ldflags"
%configure2_5x \
	--enable-shared \
	--datadir=%{_datadir}/tabe \
	--with-dbinc=%{_includedir}/db51

make

%install
rm -rf %{buildroot}

%makeinstall datadir=%{buildroot}%{_datadir}/tabe

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc doc/libtabe.sgml
%{_bindir}/*
%{_datadir}/%{name}

%files -n %{libname}
%doc COPYING
%defattr(-,root,root,-)
%doc doc/*.shtml
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc doc/*.txt
%{_includedir}/bims.h
%{_includedir}/tabe.h
%{_libdir}/*.so
%{_libdir}/*.a


%changelog
* Tue May 15 2012 Crispin Boylan <crisb@mandriva.org> 0.2.6-13
+ Revision: 799075
- Ensure bims is built

* Tue May 08 2012 Crispin Boylan <crisb@mandriva.org> 0.2.6-12
+ Revision: 797595
- Rebuild

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - build with db 5.1 (from fwang | 2011-04-12 15:59:54 +0200)

* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 0.2.6-10
+ Revision: 633694
- turn to debian tarball and patch
- fix link

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.2.6-9mdv2009.0
+ Revision: 269405
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.6-8mdv2009.0
+ Revision: 209481
- build it against bdb 4.2
- fix devel package naming

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.2.6-7mdv2008.1
+ Revision: 140904
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel

* Thu May 03 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.6-7mdv2008.0
+ Revision: 22084
- build against db4.1 not 4.2

* Thu May 03 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.6-6mdv2008.0
+ Revision: 22079
- move .db files to /usr/share/tabe

* Thu May 03 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.6-5mdv2008.0
+ Revision: 20892
- Import tabe

