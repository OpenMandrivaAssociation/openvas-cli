Summary: 	OpenVAS command line interface
Name:		openvas-cli
Version:	1.1.2
Release:	%mkrel 1
Source:		http://wald.intevation.org/frs/download.php/851/%name-%version.tar.gz
Group:		System/Configuration/Networking
Url:		http://www.openvas.org
License:	GPLv2+
BuildRoot:	%{_tmppath}/%name-%{version}-root
BuildRequires:	cmake
BuildRequires:	openvas-devel >= 4.0
BuildRequires:	glib2-devel

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/omp
%{_mandir}/man8/omp.8.*
