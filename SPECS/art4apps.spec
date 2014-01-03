%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary: Art4Apps images and data to use it
Name:    art4apps
Version: 0.3
Release: 0
URL:     http://www.art4apps.org
License: Creative cCommnn License (CC-BY-SA)
Group:   User Interface/Desktops
Source0: art4apps-0.3.tar

BuildRequires: python
Requires: art4apps-images
BuildArch: noarch

%description

Art4Apps is a database of images, audio,and videos files of words created 
by ET4D under a Creative Common License (CC BY-SA). 
We hope to help developers and educators create applications for educational 
uses at a low cost through the use of our resources. The primary objective 
in sharing this database is to promote apps development in the field of 
literacy in an effort to support and sustain the diversity among world languages.

%package images
Summary: Art4Apps English image files
%description images

%package audio-en
Summary: Art4Apps English audio files
%description audio-en

%package audio-fr
Summary: Art4Apps French audio files
%description audio-fr

%package audio-es
Summary: Art4Apps Spanish audio files
%description audio-es

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/%{name}/data
mkdir -p %{buildroot}/%{_datadir}/%{name}/images
mkdir -p %{buildroot}/%{python_sitelib}/%{name}
mkdir -p %{buildroot}/%{_datadir}/%{name}/audio
mkdir -p %{buildroot}/%{_datadir}/%{name}/audio/en
mkdir -p %{buildroot}/%{_datadir}/%{name}/audio/fr
mkdir -p %{buildroot}/%{_datadir}/%{name}/audio/es
mkdir -p %{buildroot}/%{_bindir}

cp %{_builddir}/%{name}-%{version}/data/* %{buildroot}/%{_datadir}/%{name}/data
cp %{_builddir}/%{name}-%{version}/images/* %{buildroot}/%{_datadir}/%{name}/images
cp %{_builddir}/%{name}-%{version}/__init__.py %{buildroot}/%{python_sitelib}/%{name}
cp %{_builddir}/%{name}-%{version}/audio/en/* %{buildroot}/%{_datadir}/%{name}/audio/en/
cp %{_builddir}/%{name}-%{version}/audio/fr/* %{buildroot}/%{_datadir}/%{name}/audio/fr/
cp %{_builddir}/%{name}-%{version}/audio/es/* %{buildroot}/%{_datadir}/%{name}/audio/es/
cp %{_builddir}/%{name}-%{version}/art4apps-translator.py %{buildroot}/%{_bindir}/art4apps-translator
chmod +x %{buildroot}/%{_bindir}/art4apps-translator

%files
%{_datadir}/%{name}/
%{python_sitelib}/*
%{_bindir}/*
%exclude %{_datadir}/%{name}/audio/
%exclude %{_datadir}/%{name}/images/

%files audio-en
%{_datadir}/art4apps/audio/en/

%files audio-fr
%{_datadir}/art4apps/audio/fr/

%files audio-es
%{_datadir}/art4apps/audio/es/

%files images
%{_datadir}/art4apps/images/

%changelog
* Sat Dec 7 2013 Gonzalo Odiard <gonzalo@laptop.org> 0.1-0
- 0.1 devel release
