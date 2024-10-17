Summary: 	OpenVAS command line interface
Name:		openvas-cli
Version:	1.1.5
Release:	2
Source0:		http://wald.intevation.org/frs/download.php/851/%name-%version.tar.gz
source1:	.abf.yml
Group:		System/Configuration/Networking
Url:		https://www.openvas.org
License:	GPLv2+
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
%makeinstall_std -C build

%files
%defattr(-,root,root)
%{_bindir}/omp
%{_mandir}/man8/omp.8.*


%changelog
* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 1.1.2-1mdv2011.0
+ Revision: 649871
- import openvas-cli

