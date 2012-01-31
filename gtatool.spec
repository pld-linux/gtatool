# TODO: [lib]matio, [lib]pcl_io >= 1.0, [lib]pfs, dcmingle/dcmtk
#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
#
Summary:	Tools to manipulate Generic Tagged Array (GTA) files
Summary(pl.UTF-8):	Narzędzia do obróbki plików GTA (ogólnych tablic etykietowanych)
Name:		gtatool
Version:	1.0.2
Release:	1
License:	GPL v3+
Group:		Applications/File
Source0:	http://download.savannah.nongnu.org/releases/gta/%{name}-%{version}.tar.xz
# Source0-md5:	13c454e28a760f03f691f9d21b5c08b3
URL:		http://gta.nongnu.org/gtatool.html
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	QtGui-devel >= 4.4.3
%{?with_apidocs:BuildRequires:	doxygen}
# libavformat >= 52.110.0 libavcodec libavdevice libavutil libswscale
BuildRequires:	ffmpeg-devel
BuildRequires:	gdal-devel
BuildRequires:	libgta-devel >= 0.9.4
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	muparser-devel
BuildRequires:	netpbm-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4.4.3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtatool manipulates Generic Tagged Array (GTA) files.

It provides a set of commands that manipulate GTAs on various levels,
and it can import from and export to many other file formats.

%description -l pl.UTF-8
gtatool pracuje na plikach GTA (Generic Tagged Array - ogólnych
tablicach etykietowanych).

Pakiet zawiera zestaw poleceń obrabiających GTA na różnych poziomach,
potrafiących importować i eksportować do wielu innych formatów plików.

%package component-compute
Summary:	gtatool module to compute array element components
Summary(pl.UTF-8):	Moduł gtatool do obliczania składowych elementów tablicy
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description component-compute
gtatool module to compute array element components.

%description component-compute -l pl.UTF-8
Moduł gtatool do obliczania składowych elementów tablicy.

%package conv-exr
Summary:	gtatool module to convert from/to EXR format
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatu EXR
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-exr
gtatool module to convert from/to EXR format.

%description conv-exr -l pl.UTF-8
Moduł gtatool do konwersji z/do formatu EXR.

%package conv-ffmpeg
Summary:	gtatool module to convert from FFmpeg formats
Summary(pl.UTF-8):	Moduł gtatool do konwersji z formatów FFmpeg
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-ffmpeg
gtatool module to convert from FFmpeg formats.

%description conv-ffmpeg -l pl.UTF-8
Moduł gtatool do konwersji z formatów FFmpeg.

%package conv-gdal
Summary:	gtatool module to convert from/to GDAL supported formats
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatów obsługiwanych przez GDAL
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-gdal
gtatool module to convert from/to GDAL supported formats.

%description conv-gdal -l pl.UTF-8
Moduł gtatool do konwersji z/do formatów obsługiwanych przez GDAL.

%package conv-magick
Summary:	gtatool module to convert from/to ImageMagick supported formats
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatów obsługiwanych przez ImageMagick
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-magick
gtatool module to convert from/to ImageMagick supported formats.

%description conv-magick -l pl.UTF-8
Moduł gtatool do konwersji z/do formatów obsługiwanych przez
ImageMagick.

%package conv-mat
Summary:	gtatool module to convert from/to MAT format
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatu MAT
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-mat
gtatool module to convert from/to MAT (Matlab) format.

%description conv-mat -l pl.UTF-8
Moduł gtatool do konwersji z/do formatu MAT (z programu Matlab).

%package conv-netpbm
Summary:	gtatool module to convert from/to NetPBM supported formats
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatów obsługiwanych przez NetPBM
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-netpbm
gtatool module to convert from/to NetPBM supported formats.

%description conv-netpbm -l pl.UTF-8
Moduł gtatool do konwersji z/do formatów obsługiwanych przez NetPBM.

%package conv-sndfile
Summary:	gtatool module to convert from/to libsndfile supported formats
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatów obsługiwanych przez libsndfile
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-sndfile
gtatool module to convert from/to libsndfile supported formats.

%description conv-sndfile -l pl.UTF-8
Moduł gtatool do konwersji z/do formatów obsługiwanych przez
libsndfile.

%package gui
Summary:	Qt-based GUI module for gtatool
Summary(pl.UTF-8):	Moduł graficznego interfejsu użytkownika opartego na Qt dla narzędzia gtatool
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	QtGui >= 4.4.3

%description gui
Qt-based GUI module for gtatool.

%description gui -l pl.UTF-8
Moduł graficznego interfejsu użytkownika opartego na Qt dla narzędzia
gtatool.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gta
%dir %{_libdir}/gtatool
%attr(755,root,root) %{_libdir}/gtatool/conv-ply.so
%attr(755,root,root) %{_libdir}/gtatool/conv-rat.so
%attr(755,root,root) %{_libdir}/gtatool/conv-raw.so
%{_mandir}/man1/gta.1*
%{_infodir}/gta.info*

%files component-compute
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/component-compute.so

%files conv-exr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-exr.so

%files conv-ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-ffmpeg.so

%files conv-gdal
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-gdal.so

%files conv-magick
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-magick.so

%files conv-mat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-mat.so

%files conv-netpbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-netpbm.so

%files conv-sndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-sndfile.so

%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/gui.so
