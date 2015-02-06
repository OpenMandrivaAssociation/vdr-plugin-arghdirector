%define plugin	arghdirector

Summary:	VDR plugin: plugin to use the premiere multifeed option
Name:		vdr-plugin-%plugin
Version:	0.2.6
Release:	21
Group:		Video
License:	GPL
URL:		http://www.arghgra.de/arghdirector.html
Source:		http://www.arghgra.de/vdr-%plugin-%version.tar.bz2
Patch0:		arghdirector-0.2.6-fonts-1.6.patch
Patch1:		arghdirector-0.2.6-i18n-1.6.patch
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
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.2.6-19mdv2010.0
+ Revision: 401662
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.2.6-17mdv2009.1
+ Revision: 359282
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.2.6-16mdv2009.0
+ Revision: 197897
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.2.6-15mdv2009.0
+ Revision: 197628
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt to font api changes of VDR 1.6 (P0)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.2.6-14mdv2008.1
+ Revision: 145019
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.2.6-13mdv2008.1
+ Revision: 144973
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.2.6-12mdv2008.1
+ Revision: 103057
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.2.6-11mdv2008.0
+ Revision: 49966
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.2.6-10mdv2008.0
+ Revision: 42053
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.2.6-9mdv2008.0
+ Revision: 22699
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.2.6-8mdv2007.0
+ Revision: 90888
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.2.6-7mdv2007.1
+ Revision: 73948
- rebuild for new vdr
- Import vdr-plugin-arghdirector

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.2.6-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.2.6-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.2.6-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.2.6-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.2.6-2mdv2007.0
- rebuild for new vdr

* Mon Jun 12 2006 Anssi Hannula <anssi@mandriva.org> 0.2.6-1mdv2007.0
- 0.2.6

* Sun Jun 11 2006 Anssi Hannula <anssi@mandriva.org> 0.2.4-1mdv2007.0
- initial Mandriva release

