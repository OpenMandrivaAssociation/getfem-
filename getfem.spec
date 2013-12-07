# Debug package is empty
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define	major	4
%define	libname	%mklibname getfem %{major}
%define	devname	%mklibname getfem -d

Summary:	Generic and efficient C++ library for finite element methods
Name:		getfem
Version:	4.2
Release:	5
License:	LGPLv2+
Group:		Development/C++
Url:		http://home.gna.org/getfem/
Source0:	http://download.gna.org/getfem/stable/%{name}-%{version}.tar.gz
Patch0:		getfem-4.2-sfmt.patch

BuildRequires:	boost-devel
BuildRequires:	pkgconfig(blas)
BuildRequires:	pkgconfig(muparser)
Obsoletes:	getfem++ < 4.2-3

%description
The Getfem++ project focuses on the development of a generic and efficient
C++ library for finite element methods. The goal is to provide a library
allowing the computation of any elementary matrix (even for mixed finite
element methods) on the largest class of methods and elements, and for
arbitrary dimension (i.e. not only 2D and 3D problems).

%package -n %{libname}
Summary:	Main library for gupnp
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q
%apply_patches

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure2_5x \
	--disable-static \
	--enable-shared \
	--enable-boost \
	--enable-muparser \
	--disable-python
%make

%install
%makeinstall_std

%files
%doc README COPYING
%{_prefix}/getfem_toolbox

%files -n %{libname}
%{_libdir}/libgetfem.so.%{major}*

%files -n %{devname}
%{_bindir}/getfem-config
%{_libdir}/libgetfem.so
%{_includedir}/gmm
%{_includedir}/getfem
%{_includedir}/getfem_boost

