%define name tabe
%define version 0.2.6
%define release %mkrel 5

%define	major	2
%define libname %mklibname tabe %{major}

Summary:	Chinese lexicons library for xcin-2.5
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD style
Group:		System/Libraries
URL:		http://libtabe.sourceforge.net/
Buildroot:	%_tmppath/%{name}-%{version}-%{release}-root

Source:		%{name}-%{version}.tar.bz2
Patch0:		%{name}-db4.1.patch
Patch1:		%{name}-0.2.3-notestdb.patch

BuildRequires:	db4-devel >= 4.1
BuildRequires:	XFree86-devel
Requires:	%{libname} = %{version}-%{release}
Requires:	locales-zh
Provides:	libtabe
Obsoletes:	libtabe

%description
Chinese lexicons library for xcin-2.5's bimsphone input method.

%package	-n %{libname}
Summary:	Libraries needed to use packages using libtabe
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description	-n %{libname}
Chinese lexicons library for xcin-2.5's bimsphone input method.

This package contains shared libraries.

%package	-n %{libname}-devel
Summary:	Header files and libraries for developing apps which will use libtabe
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{libname}-devel
Chinese lexicons library for xcin-2.5's bimsphone input method.

This package contains static libraries and headers files.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .db41

cp script/configure.in .
%__libtoolize --copy --force

%build
%configure \
	--enable-shared \
	--datadir=%{_libdir}/tabe \
	--with-x \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir} \
	--with-dbinc=%{_includedir}/db4

make

%install
rm -rf %{buildroot}
%makeinstall datadir=%{buildroot}%{_libdir}/tabe

# AdamW: shouldn't be needed with xcin 2.5.3.pre2
# Make link so that xcin-2.5 can use yin.db and tsi.db
#install -d %{buildroot}%{_prefix}/X11R6/%{_lib}/X11/xcin/tab/big5 \
#           %{buildroot}%{_prefix}/X11R6/%{_lib}/X11/xcin/tab/utf-8
#
#pushd %{buildroot}%{_prefix}/X11R6/%{_lib}/X11/xcin/tab/big5
#ln -sf %{_libdir}/tabe/tsi.db .
#ln -sf %{_libdir}/tabe/yin.db .
#popd
#pushd %{buildroot}%{_prefix}/X11R6/%{_lib}/X11/xcin/tab/utf-8
#ln -sf %{_libdir}/tabe/tsi.db .
#ln -sf %{_libdir}/tabe/yin.db .
#popd

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING  doc/libtabe.sgml
%{_bindir}/*
%{_libdir}/%{name}

%files -n %{libname}
%defattr(-,root,root,-)
%doc doc/*.shtml
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc doc/*.txt
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
