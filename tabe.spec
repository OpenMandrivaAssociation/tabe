%define	major 2
%define libname %mklibname tabe %{major}
%define develname %mklibname tabe -d

Summary:	Chinese lexicons library for xcin-2.5
Name:		tabe
Version:	0.2.6
Release:	13
License:	BSD style
Group:		System/Libraries
URL:		http://libtabe.sourceforge.net/
Source:		%{name}-%{version}.tar.bz2
Patch0:		http://ftp.de.debian.org/debian/pool/main/libt/libtabe/libtabe_0.2.6-1.2.diff.gz
Patch1:		tabe-0.2.6-link.patch
BuildRequires:	db-devel
BuildRequires:	libx11-devel
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
