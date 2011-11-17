Summary: 	OpenVAS command line interface
Name:		openvas-cli
Version:	1.1.3
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Configuration/Networking
URL:		http://www.openvas.org
Source:		http://wald.intevation.org/frs/download.php/851/%name-%version.tar.gz
BuildRequires:	cmake
BuildRequires:	openvas-devel >= 4.0
BuildRequires:	glib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The module OpenVAS-CLI collects command line tools
to handle with the OpenVAS services via the respective
protocols.

The best supported service is currently the OpenVAS-Manager (openvasmd).

%prep
%setup -qn %name-%version

sed -i -e 's#-Werror##' `grep -rl Werror *|grep CMakeLists.txt`

%build
%cmake -DSYSCONFDIR=%{_sysconfdir}
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/omp
%{_mandir}/man8/omp.8.*
