Summary:	Lightweight network manager
Name:		lxnm
Version:	0.2.2
Release:	5
License:	GPLv2+
Group:		Graphical desktop/Other
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
URL:		https://lxde.sourceforge.net/
BuildRequires:	gtk+2-devel

%description
Lightweight network manager for LXDE supporting wireless connections.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
