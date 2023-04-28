# TODO: pmd (BR: proprietary libpmdaccess2)
#
# Conditional build:
%bcond_without	apidocs		# do not build and package API docs
%bcond_without	qt		# Qt-based GUI
%bcond_without	muparser	# compute component module (based on MuParser)
%bcond_without	dcmtk		# DCMTK conv module
%bcond_without	ffmpeg		# FFmpeg conv module
%bcond_without	gdal		# GDAL conv module
%bcond_without	png		# PNG conv module
%bcond_without	jpeg		# JPEG conv module (based on libjpeg)
%bcond_without	magick		# Magick conv module (based on ImageMagick's libMagick++)
%bcond_without	matio		# MAT conv module (MATLAB import/export, based on [lib]matio)
%bcond_without	netcdf		# NetCDF conv module
%bcond_without	netpbm		# NetPBM conv module
%bcond_with	openexr		# EXR conv module (based on OpenEXR)
%bcond_without	pcl		# PCD conv module (based on PCL's libpcl_io)
%bcond_without	pfs		# PFS conv module
%bcond_without	sndfile		# sndfile conv module
%bcond_without	teem		# teem (nrrd) conv module
#
Summary:	Tools to manipulate Generic Tagged Array (GTA) files
Summary(pl.UTF-8):	Narzędzia do obróbki plików GTA (ogólnych tablic etykietowanych)
Name:		gtatool
Version:	2.4.0
Release:	8
License:	GPL v3+
Group:		Applications/File
Source0:	https://marlam.de/gta/releases/%{name}-%{version}.tar.xz
# Source0-md5:	ea2ea1a0838c614ec8b7b4072c9e6ce1
Patch0:		%{name}-getopt.patch
Patch1:		%{name}-bashcomp.patch
Patch2:		imagemagick7.patch
Patch3:		pcl-1.11.patch
Patch4:		gcc11.patch
URL:		https://marlam.de/gta/
%{?with_magick:BuildRequires:	ImageMagick-c++-devel}
%{?with_openexr:BuildRequires:	OpenEXR-devel}
%{?with_qt:BuildRequires:	OpenGL-devel}
%{?with_qt:BuildRequires:	Qt5Gui-devel >= 5.5}
%{?with_qt:BuildRequires:	Qt5OpenGL-devel >= 5.5}
%{?with_qt:BuildRequires:	Qt5Widgets-devel >= 5.5}
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake >= 1:1.11.1
%{?with_dcmtk:BuildRequires:	dcmtk-devel}
%{?with_apidocs:BuildRequires:	doxygen}
# libavformat >= 52.110.0 libavdevice libswscale
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
%{?with_gdal:BuildRequires:	gdal-devel}
%{?with_qt:BuildRequires:	glew-devel >= 1.6.0}
BuildRequires:	libgta-devel >= 0.9.4
%{?with_jpeg:BuildRequires:	libjpeg-devel}
%{?with_png:BuildRequires:	libpng-devel >= 1.2.0}
%{?with_sndfile:BuildRequires:	libsndfile-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2.6
%{?with_matio:BuildRequires:	matio-devel >= 1.5.0}
%{?with_muparser:BuildRequires:	muparser-devel}
%{?with_netcdf:BuildRequires:	netcdf-devel}
%{?with_netpbm:BuildRequires:	netpbm-devel}
%{?with_pcl:BuildRequires:	pcl-devel >= 1.8}
%{?with_pfs:BuildRequires:	pfstools-devel >= 2.0}
BuildRequires:	pkgconfig
%{?with_qt:BuildRequires:	qt5-build >= 5.5}
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	tar >= 1:1.22
%{?with_teem:BuildRequires:	teem-devel}
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

%package conv-dcmtk
Summary:	gtatool module to convert from DICOM format
Summary(pl.UTF-8):	Moduł gtatool do konwersji z formatu DICOM
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-dcmtk
gtatool module to convert from DICOM format.

%description conv-dcmtk -l pl.UTF-8
Moduł gtatool do konwersji z formatu DICOM.

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

%package conv-png
Summary:	gtatool module to convert from/to PNG format
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatu PNG
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-png
gtatool module to convert from/to PNG format.

%description conv-png -l pl.UTF-8
Moduł gtatool do konwersji z/do formatu PNG.

%package conv-jpeg
Summary:	gtatool module to convert from/to JPEG formats
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatu JPEG
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-jpeg
gtatool module to convert from/to JPEG formats.

%description conv-jpeg -l pl.UTF-8
Moduł gtatool do konwersji z/do formatu JPEG.

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
Requires:	matio >= 1.5.0

%description conv-mat
gtatool module to convert from/to MAT (Matlab) format.

%description conv-mat -l pl.UTF-8
Moduł gtatool do konwersji z/do formatu MAT (z programu Matlab).

%package conv-netcdf
Summary:	gtatool module to convert from/to NetCDF format
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatu NetCDF
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-netcdf
gtatool module to convert from/to NetCDF format.

%description conv-netcdf -l pl.UTF-8
Moduł gtatool do konwersji z/do formatu NetCDF.

%package conv-netpbm
Summary:	gtatool module to convert from/to NetPBM supported formats
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatów obsługiwanych przez NetPBM
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-netpbm
gtatool module to convert from/to NetPBM supported formats.

%description conv-netpbm -l pl.UTF-8
Moduł gtatool do konwersji z/do formatów obsługiwanych przez NetPBM.

%package conv-pcd
Summary:	gtatool module to convert from/to PCD format
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatu PCD
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-pcd
gtatool module to convert from/to PCD format.

%description conv-pcd -l pl.UTF-8
Moduł gtatool do konwersji z/do formatu PCD.

%package conv-pfs
Summary:	gtatool module to convert from/to PFS format
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatu PFS
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-pfs
gtatool module to convert from/to PFS format.

%description conv-pfs -l pl.UTF-8
Moduł gtatool do konwersji z/do formatu PFS.

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

%package conv-teem
Summary:	gtatool module to convert from/to Teem (NRRD) format
Summary(pl.UTF-8):	Moduł gtatool do konwersji z/do formatu Teem (NRRD)
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}

%description conv-teem
gtatool module to convert from/to Teem (NRRD) format.

%description conv-teem -l pl.UTF-8
Moduł gtatool do konwersji z/do formatu Teem (NRRD).

%package gui
Summary:	Qt-based GUI module for gtatool
Summary(pl.UTF-8):	Moduł graficznego interfejsu użytkownika opartego na Qt dla narzędzia gtatool
Group:		X11/Applications
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Widgets >= 5.5
Requires:	hicolor-icon-theme

%description gui
Qt-based GUI module for gtatool.

%description gui -l pl.UTF-8
Moduł graficznego interfejsu użytkownika opartego na Qt dla narzędzia
gtatool.

%package -n bash-completion-gtatool
Summary:	Bash completion for gtatool command
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów programu gtatool
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2
BuildArch:	noarch

%description -n bash-completion-gtatool
Bash completion for gtatool command.

%description -n bash-completion-gtatool -l pl.UTF-8
Bashowe uzupełnianie parametrów programu gtatool.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%if %{with netpbm}
export CFLAGS="%{rpmcflags} -I/usr/include/netpbm"
export CXXFLAGS="%{rpmcxxflags} -I/usr/include/netpbm -std=gnu++14"
%endif
%configure \
	MOC=%{_libdir}/qt5/bin/moc \
	BASHCOMPLETIONDIR=%{bash_compdir} \
	--disable-silent-rules \
	--with-bashcompletion \
	%{!?with_dcmtk:--without-dcmtk} \
	%{!?with_ffmpeg:--without-ffmpeg} \
	%{!?with_gdal:--without-gdal} \
	%{!?with_jpeg:--without-jpeg} \
	%{!?with_png:--without-png} \
	%{?with_magick:--with-magick-flavor=ImageMagick} \
	%{!?with_magick:--without-magick} \
	%{!?with_matio:--without-matio} \
	%{!?with_muparser:--without-muparser} \
	%{!?with_netcdf:--without-netcdf} \
	%{!?with_netpbm:--without-netpbm} \
	%{!?with_openexr:--without-exr} \
	%{!?with_pcl:--without-pcd} \
	%{!?with_pfs:--without-pfs} \
	%{!?with_qt:--without-qt} \
	%{!?with_sndfile:--without-sndfile} \
	%{!?with_teem:--without-teem}
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

%post gui
%update_icon_cache hicolor

%postun gui
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gta
%dir %{_libdir}/gtatool
%attr(755,root,root) %{_libdir}/gtatool/conv-csv.so
%attr(755,root,root) %{_libdir}/gtatool/conv-datraw.so
%attr(755,root,root) %{_libdir}/gtatool/conv-ply.so
%attr(755,root,root) %{_libdir}/gtatool/conv-pvm.so
%attr(755,root,root) %{_libdir}/gtatool/conv-rat.so
%attr(755,root,root) %{_libdir}/gtatool/conv-raw.so
%{_mandir}/man1/gta.1*
%{_infodir}/gta.info*

%if %{with muparser}
%files component-compute
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/component-compute.so
%endif

%if %{with dcmtk}
%files conv-dcmtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-dcmtk.so
%endif

%if %{with openexr}
%files conv-exr
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-exr.so
%endif

%if %{with ffmpeg}
%files conv-ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-ffmpeg.so
%endif

%if %{with gdal}
%files conv-gdal
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-gdal.so
%endif

%if %{with png}
%files conv-png
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-png.so
%endif

%if %{with jpeg}
%files conv-jpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-jpeg.so
%endif

%if %{with magick}
%files conv-magick
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-magick.so
%endif

%if %{with matio}
%files conv-mat
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-mat.so
%endif

%if %{with netcdf}
%files conv-netcdf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-netcdf.so
%endif

%if %{with netpbm}
%files conv-netpbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-netpbm.so
%endif

%if %{with pcl}
%files conv-pcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-pcd.so
%endif

%if %{with pfs}
%files conv-pfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-pfs.so
%endif

%if %{with sndfile}
%files conv-sndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-sndfile.so
%endif

%if %{with teem}
%files conv-teem
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/conv-teem.so
%endif

%if %{with qt}
%files gui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtatool/gui.so
%{_desktopdir}/gta_gui.desktop
%{_iconsdir}/hicolor/*x*/apps/gta.png
%{_iconsdir}/hicolor/scalable/apps/gta.svg
%endif

%files -n bash-completion-gtatool
%defattr(644,root,root,755)
%{bash_compdir}/gta
