%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Summary: Art4Apps images and data to use it
Name:    art4apps
Version: 0.1
Release: 0
URL:     http://www.art4apps.org
License: Creative cCommnn License (CC-BY-SA)
Group:   User Interface/Desktops
Source0: art4apps.tar

BuildRequires: python

BuildArch: noarch

%description

Art4Apps is a database of images, audio,and videos files of words created 
by ET4D under a Creative Common License (CC BY-SA). 
We hope to help developers and educators create applications for educational 
uses at a low cost through the use of our resources. The primary objective 
in sharing this database is to promote apps development in the field of 
literacy in an effort to support and sustain the diversity among world languages.

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_datadir}/%{name}
mkdir -p %{buildroot}/%{_datadir}/%{name}/data
mkdir -p %{buildroot}/%{_datadir}/%{name}/images
mkdir -p %{buildroot}/%{python_sitelib}/%{name}

cp %{_builddir}/%{name}-%{version}/data/* %{buildroot}/%{_datadir}/%{name}/data
cp %{_builddir}/%{name}-%{version}/images/* %{buildroot}/%{_datadir}/%{name}/images
cp %{_builddir}/%{name}-%{version}/__init__.py %{buildroot}/%{python_sitelib}/%{name}

%files
%{_datadir}/%{name}/
%{python_sitelib}/*

%changelog
* Sat Dec 7 2013 Gonzalo Odiard <gonzalo@laptop.org> 0.1-0
- 0.1 devel release
