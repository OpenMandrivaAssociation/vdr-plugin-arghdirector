
%define plugin	arghdirector
%define name	vdr-plugin-%plugin
%define version	0.2.6
%define rel	16

Summary:	VDR plugin: plugin to use the premiere multifeed option
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.arghgra.de/arghdirector.html
Source:		http://www.arghgra.de/vdr-%plugin-%version.tar.bz2
Patch0:		arghdirector-0.2.6-fonts-1.6.patch
Patch1:		arghdirector-0.2.6-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Director is a plugin to use the multifeed option of some Premiere
channels(Direkt,Sport1,Sport2).

%prep
%setup -q -n %plugin-%version
chmod a-x HISTORY README
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


