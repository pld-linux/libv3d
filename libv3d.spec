Summary:	LibV3D
Summary(pl):	LibV3D
Name:		libv3d
Version:	0.1.14
Release:	1
Copyright:	LGPL
Group:		X11/Library
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
BuildRequires:	OpenGL-devel	
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description

%description -l pl

%package devel
Summary:	LibV3D devel
Summary(pl):	LibV3D nag³ówki
Group:		Library/Development
%description devel
%description -l pl devel

%prep
%setup -q

#%patch

%build
./configure Linux
%{__make} CC=gcc CXX=g++ INC_DIRS="-I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man3 install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_libdir}/libv3d.*

%files devel
%attr(644,root,root) %{_includedir}/v3d/*.h
%attr(644,root,root) %{_mandir}/man3/*
