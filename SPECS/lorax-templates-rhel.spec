Name:           lorax-templates-rhel
Version:        10.1
Release:        3%{?dist}
Summary:        RHEL build templates for lorax and livemedia-creator

License:        GPLv2+
URL:            https://gitlab.com/redhat/centos-stream/rpms/lorax-templates-rhel/
BuildArch:      noarch

# This tarball is generated from the contents of this dist-git repository
# by running the command `make tar`.
# See README for full details of how to update this package
Source0:        lorax-templates-rhel-10.1-3.tar.gz

# Required for the template branding support
Requires:       lorax >= 34.9.1

Provides: lorax-templates = %{version}-%{release}

# Where are these supposed to end up?
%define templatedir %{_datadir}/lorax/templates.d/80-rhel

%description
RHEL-specific Lorax templates for creating the boot.iso and live isos are
placed in %{templatedir}

%prep
%setup

%build
# nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{templatedir}
cp -a 80-rhel/* $RPM_BUILD_ROOT/%{templatedir}

%files
%dir %{templatedir}
%{templatedir}/*

%changelog
* Thu Jul 10 2025 Brian C. Lane <bcl@redhat.com> - 10.1-3
- config_files: Do not remove `chcon` in runtime cleanup (ppolawsk)
  Resolves: RHEL-102872
- runtime-postinstall: allow pipewire to run as root (awilliam)
  Resolves: RHEL-102419
- runtime-cleanup: Do not clean up rpm binaries (bcl)
  Resolves: RHEL-101695

* Tue May 27 2025 Brian C. Lane <bcl@redhat.com> - 10.1-2
- Set ppc64le default boot to test the media (bcl)
  Resolves: RHEL-93171

* Mon May 19 2025 Brian C. Lane <bcl@redhat.com> - 10.1-1
- Bump release version to 10.1 (bcl)
  Related: RHEL-91929
- Add a boot menu for fips=1 (bcl)
  Resolves: RHEL-91929

* Tue Feb 18 2025 Brian C. Lane <bcl@redhat.com> - 10.0-56
- runtime-cleanup: Leave the stat binary (bcl)
  Resolves: RHEL-79945

* Mon Nov 18 2024 Brian C. Lane <bcl@redhat.com> - 10.0-55
- SERIAL: Bump to 54 to match spec change for mass rebuild (bcl)
  Related: RHEL-67586
- tests: Fix the repos used for the test (bcl)
  Related: RHEL-67586
- runtime-cleanup: Newer glibc installs /usr/sbin/ldconfig (bcl)
  Resolves: RHEL-67586

* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 10.0-54
- Bump release for October 2024 mass rebuild:
  Resolves: RHEL-64018

* Tue Sep 10 2024 Brian C. Lane <bcl@redhat.com> - 10.0-53
- runtime-cleanup: fonttosfnt no longer installed (bcl)
  Resolves: RHEL-54717
- Use the same page args in all the per-arch templates (bcl)
  Resolves: RHEL-54535
- Remove manual /root/lorax-packages.log creation (bcl)
  Resolves: RHEL-54534
- Remove libuser.conf (bcl)
  Resolves: RHEL-54533

* Thu Aug 08 2024 Brian C. Lane <bcl@redhat.com> - 10.0-52
- runtime-postinstall: Remove blacklist_exceptions from multipath.conf (bcl)
  Resolves: RHEL-53779

* Mon Aug 05 2024 Brian C. Lane <bcl@redhat.com> - 10.0-51
- runtime-install: Revert "Replace wget with wget2" (yselkowi)
  Resolves: RHEL-45269

* Wed Jul 17 2024 Brian C. Lane <bcl@redhat.com> - 10.0-50
- runtime-cleanup: Fix gshadow typo (bcl)
  Resolves: RHEL-35396
- runtime-install: Add redhat-release-eula (bcl)
  Related: RHEL-35396
- kernel: Keep nvram module (bcl)
  Resolves: RHEL-36443
- kernel: Keep hid-multitouch module (bcl)
  Resolves: RHEL-49546

* Thu Jun 27 2024 Brian C. Lane <bcl@redhat.com> - 10.0-49
- SERIAL: Bump to 48 to match spec change for mass rebuild (bcl)
- firmware: Exclude installation of audio firmware (bcl)
  Related: RHEL-44311
- tests: Replace $stream with 10-stream (bcl)
  Related: RHEL-44311
- runtime-install: Only install qcom-firmware on aarch64 (bcl)
  Related: RHEL-44311
- runtime-cleanup: Cleanup firmware moved to brcmfmac-firmware (bcl)
  Related: RHEL-44311
- runtime-cleanup: Cleanup firmware moved to intel-audio-firmware (bcl)
  Related: RHEL-44311
- runtime-cleanup: Cleanup firmware moved to dvb-firmware (bcl)
  Related: RHEL-44311
- runtime-cleanup: qcom firmware is now in the qcom-firmware package (bcl)
  Related: RHEL-44311
- Drop Tiger VNC from templates (mkolman)
  Resolves: RHEL-38741

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 10.0-48
- Bump release for June 2024 mass rebuild

* Wed Jun 05 2024 Brian C. Lane <bcl@redhat.com> - 10.0-47
- Makefile: Add PREV support for clog (bcl)
  Related: RHEL-40021
- git-changelog: Change line length limit to 120 (bcl)
  Related: RHEL-40021
- README: Update README with note about PREV= (bcl)
  Related: RHEL-40021
- Remove libvisual from runtime-cleanup as it's being removed from RHEL 10 (tpopela)
  Resolves: RHEL-39949
- tests: Do not use fedora.repo for the test build (bcl)
  Resolves: RHEL-40021
- Drop libreport from templates (mkolman)
  Resolves: RHEL-39794

* Tue May 28 2024 Brian C. Lane <bcl@redhat.com> - 10.0-46
- Adjust Lorax templates for the Xorg to Wayland switch (mkolman)
  Resolves: RHEL-38740

* Wed May 22 2024 Brian C. Lane <bcl@redhat.com> - 10.0-45
- tools: Add support for Jira RHEL-XXX issues (bcl)
  Related: RHEL-22656
- Makefile: Fix clog target (bcl)
  Related: RHEL-22656
- aarch64: Replace spaces and escape characters in isolabel with '-' (bcl)
  Resolves: RHEL-22656
- s390: Replace spaces and escape characters in isolabel with '-' (bcl)
  Resolves: RHEL-22658
- ppc: Remove unused ppc templates and config files (bcl)
  Resolves: RHEL-35394
- Drop gdisk from the boot.iso (bcl)
  Resolves: RHEL-38339
- tests: Name the test iso RHEL 10 instead of 9
  Resolves: RHEL-38199
- Add prefixdevname to Anaconda image
  Related: RHEL-30010
- spec: Update URL to point to gitlab project
  Resolves: RHEL-32959

* Thu Apr 18 2024 Parag Nemade <pnemade AT redhat DOT com> - 10.0-44
- Resolves: RHEL-32728 (pnemade)
- runtime-install: Update font packages
- runtime-cleanup: Update font packages

* Wed Feb 21 2024 Brian Stinson <bstinson@redhat.com> - 10.0-43
- Remove shim-ia32 from the installed packages since we don't produce shim-ia32
  any more. (bstinson) Rerelease

* Wed Feb 21 2024 Brian Stinson <bstinson@redhat.com> - 10.0-42
- Remove shim-ia32 from the installed packages list

* Sun Jan 14 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 10.0-41
- Replace wget with wget2

* Wed Dec 13 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-40
-  ()

* Fri Sep 08 2023 Adam Williamson <awilliam@redhat.com> - 10.0-39
- runtime-install: install dosfstools to fix UEFI install

* Wed Aug 16 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 10.0-38
- Drop packages not in RHEL

* Tue Jul 25 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-37
- Install rsvg-pixbuf-loaders to the install environment

* Fri Jun 09 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-35
-  ()

* Fri Jun 09 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-34
-  ()

* Fri Jun 09 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-33
-  ()

* Fri Jun 09 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-32
-  ()

* Fri Jun 09 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-31
- Drop system-storage-manager

* Fri Jun 09 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-28
- Drop jfs-utils

* Fri Jun 09 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-27
- Drop uboot-tools

* Fri Jun 09 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-26
- Drop b43-openfwwf

* Fri Jun 09 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-25
- Re-sync templates from Fedora

* Thu Jun 08 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-24
- Replace several fonts

* Mon Mar 27 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-23
- Update for Noto CJK Variable Fonts

* Fri Feb 17 2023 Stephen Gallagher <sgallagh@redhat.com> - 10.0-22
- Strip some things from gtk4

* Wed Dec 14 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-21
- Sync from CentOS Stream 9
- On ppc64le Use core.elf from grub2 package (bcl)
  Resolves: rhbz#2143422
- grub2 1:2.06-51 now ships a signed core.elf that includes all the needed
  modules, use that instead of making an unsigned one.

* Tue Oct 18 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-20
- Sync from Fedora
- Commit (502cc01d9a8a8c6626e83ff7ea7f7853cce92df5)
- Drop 32-bit ARM and x86 support
- Drop anaconda auditd replacement
- Update kdump addon package name

* Thu Sep 15 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-19
-  ()

* Thu Jun 23 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-18
-  ()

* Thu Jun 23 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-18
- Add virtual Provides: lorax-templates

* Fri Jun 17 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-17
- Complete removal of syslinux

* Thu Jun 16 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-16
- Fix typo

* Thu Jun 16 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-15
- Pull in the latest changes from Fedora
- Use grub2 instead of syslinux for all x86 systems

* Thu Jun 16 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-14
- Exclude python-virt-firmware from pkginstall

* Thu Apr 07 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-13
- Re-sync from CentOS Stream 9

* Tue Mar 08 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-12
- Don't try to install packages that don't exist in ELN
  - redhat-release-eula
  - libreport-rhel-anaconda-bugzilla

* Tue Mar 08 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-11
- Don't move the restart-anaconda file

* Tue Mar 08 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-10
- Re-sync from CentOS Stream 9

* Mon Feb 07 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-9
- Update to new Malaysian font

* Mon Feb 07 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-8
- Re-sync from CentOS Stream 9

* Wed Jan 26 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-7
- Re-sync from CentOS Stream 9

* Tue Jan 04 2022 Stephen Gallagher <sgallagh@redhat.com> - 10.0-6
- Update runtime-cleanup.tmpl to handle changes in sound support

* Tue Nov 30 2021 Stephen Gallagher <sgallagh@redhat.com> - 10.0-5
- Regenerate tarball correctly

* Mon Nov 29 2021 Stephen Gallagher <sgallagh@redhat.com> - 10.0-4
- Re-sync from CentOS Stream 9

* Thu Jul 15 2021 Stephen Gallagher <sgallagh@redhat.com> - 10.0-3
- Drop prefixdevname

* Wed Jul 14 2021 Stephen Gallagher <sgallagh@redhat.com> - 10.0-2
- Re-sync from CentOS Stream 9

* Mon May 10 2021 Stephen Gallagher <sgallagh@redhat.com> - 10.0-1
- First release of lorax-templates-rhel for ELN
