Name:           lorax-templates-rhel
Version:        8.7
Release:        1%{?dist}
Summary:        RHEL8 build templates for lorax and livemedia-creator

License:        GPLv2+
URL:            https://github.com/weldr/lorax
BuildArch:      noarch
Source0:        lorax-templates-rhel-8.7-1.tar.gz

# Required for the template branding support
Requires:       lorax > 28.14.68

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
* Mon Jun 13 2022 Brian C. Lane <bcl@redhat.com> - 8.7-1
- runtime-cleanup: Use new lorax branding support (bcl)
  Resolves: rhbz#2052154

* Fri Jan 14 2022 Brian C. Lane <bcl@redhat.com> - 8.6-3
- Enable sftp when using inst.sshd (bcl)
  Resolves: rhbz#2035050
- Revert "Drop ia32 uefi package installation" (bcl)
  Related: rhbz#2035050

* Tue Jan 11 2022 Brian C. Lane <bcl@redhat.com> - 8.6-2
- Drop ia32 uefi package installation (bcl)
  Resolves: rhbz#2035050

* Mon Nov 01 2021 Brian C. Lane <bcl@redhat.com> - 8.6-1
- Drop ppc 32 bit support from grub template for live iso (bcl)
  Resolves: rhbz#2016807

* Mon Oct 04 2021 Brian C. Lane <bcl@redhat.com> - 8.5-3
- runtime-install: Install nvme-cli tool
  Resolves: rhbz#1903339

* Mon May 10 2021 Brian C. Lane <bcl@redhat.com> - 8.5-2
- runtime-install: Install ipcalc (bcl)
  Resolves: rhbz#1958314

* Mon Mar 22 2021 Brian C. Lane <bcl@redhat.com> - 8.5-1
- Add inst. prefix to installer kernel cmdline arguments
  Resolves: rhbz#1939350

* Wed Dec 09 2020 Brian C. Lane <bcl@redhat.com> - 8.4-3
- sshd_config: Apply suggested changes (bcl)
  Resolves: rhbz#1872921

* Thu Dec 03 2020 Brian C. Lane <bcl@redhat.com> - 8.4-2
- Switch to using upstream mk-s390image for s390 cdboot.img creation (bcl)
  Resolves: rhbz#1892404
- Remove mdmonitor service from boot.iso (bcl)
  Resolves: rhbz#1888728

* Wed Oct 28 2020 Brian C. Lane <bcl@redhat.com> - 8.4-1
-  Install Xorg and tigervnc-server on s390 boot.iso (bcl)
   Resolves: rhbz#1854933

* Tue Jul 07 2020 Brian C. Lane <bcl@redhat.com> - 8.3-4
- rsyslog: Disable journal ratelimits during install
  Related: rhbz#1752754

* Thu Jun 25 2020 Brian C. Lane <bcl@redhat.com> - 8.3-3
- include generic.ins for s390 boot iso (dan)
  Resolves: rhbz#1844517

* Wed Jun 03 2020 Brian C. Lane <bcl@redhat.com> - 8.3-2
- Keep /etc/default/useradd in install.img
  Resolves: rhbz#1843609

* Wed May 13 2020 Brian C. Lane <bcl@redhat.com> - 8.3-1
- Use smarter multipath detection logic
  Resolves: rhbz#1763906

* Thu Feb 27 2020 Brian C. Lane <bcl@redhat.com> - 8.2-6
- Restore the 98dracut-systemd service files to the install.img (bcl)
  Related: rhbz#1805405
- Add eject back into the boot.iso (bcl)
  Resolves: rhbz#1805405

* Fri Jan 10 2020 Brian C. Lane <bcl@redhat.com> - 8.2-5
- Install rdma-core and libmlx4 packages
  Resolves: rhbz#1762662

* Wed Dec 11 2019 Brian C. Lane <bcl@redhat.com> - 8.2-4
- Use mkisofs for the s390 live-iso template
  Resolves: rhbz#1746424

* Tue Nov 12 2019 Brian C. Lane <bcl@redhat.com> - 8.2-3
- Add dmidecode on supported architectures
  Resolves: rhbz#1714793

* Fri Nov 08 2019 Brian C. Lane <bcl@redhat.com> - 8.2-2
- Update ppc64le isolabel to match x86_64 logic (bcl)
  Resolves: rhbz#1757338
- set inst.stage2 for ppc64le image (bcl)
  Resolves: rhbz#1757338

* Thu Oct 31 2019 Brian C. Lane <bcl@redhat.com> - 8.2-1
- Update package version for 8.2 release
- Drop unneeded uboot-tools, and remove iso-graft from the aarch64.tmpl
  Resolves: rhbz#1763922
- Add live iso support to s390
  Resolves: rhbz#1746424

* Tue Sep 03 2019 Brian C. Lane <bcl@redhat.com> - 8.1-3
- Fix path to generic.prm (bcl)
  Resolves: rhbz#1746424

* Wed May 15 2019 Brian C. Lane <bcl@redhat.com> - 8.1-2
- Install redhat-release-eula package (bcl)
  Related: rhbz#1700465
- Don't remove chmem and lsmem from install.img (bcl)
  Resolves: rhbz#1691472
- Include the hid-multitouch kernel module (bcl)
  Resolves: rhbz#1670182
- Add extra boot args to the livemedia-creator iso templates (bcl)
  Resolves: rhbz#1694180
- Add a ppc64le template for live iso creation (bcl)
  Related: rhbz#1694180
- Add live-install.tmpl (bcl)
  Related: rhbz#1694180

* Wed Mar 27 2019 Brian C. Lane <bcl@redhat.com> - 8.1-1
- Update package version for 8.1 release
- Make sure lscpu is installed
  Resolves: rhbz#1684735

* Wed Sep 19 2018 Brian C. Lane <bcl@redhat.com> - 8.0-19
- Include python3-pyatspi on boot.iso (bcl)
  Resolves: rhbz#1543290

* Wed Sep 12 2018 Brian C. Lane <bcl@redhat.com> - 8.0-18
- re-add temporarily removed packages (bcl)
  Related: rhbz#1622395
- Use google-noto-sans-cjk-ttc-fonts (bcl)
  Resolves: rhbz#1626368

* Fri Sep 07 2018 Brian C. Lane <bcl@redhat.com> - 8.0-17
- Install the oscap-anaconda-addon
  Resolves: rhbz#1626459

* Wed Aug 22 2018 Brian C. Lane <bcl@redhat.com> - 8.0-16
- Install libreport-rhel-anaconda-bugzilla
  Related: rhbz#1593734

* Mon Aug 20 2018 Brian C. Lane <bcl@redhat.com> - 8.0-15
- import-state.service from initscripts is needed by Anaconda
  Resolves: rhbz#1618668

* Mon Aug 20 2018 Josh Boyer <jwboyer@redhat.com> - 8.0-14
- Remove fbset from runtime-install
  Resolves: rhbz#1615430

* Wed Aug 15 2018 Brian C. Lane <bcl@redhat.com> - 8.0-13
- Add prefixdevname package
  Resolves: rhbz#1615991

* Thu Aug 02 2018 Troy Dawson <tdawson@redhat.com> - 8.0-12
- Drop dependency on bridge-utils Resolves: #1588705

* Thu Jul 26 2018 Troy Dawson <tdawson@redhat.com> - 8.0-11
- Expand variables and wildcards in runtime-install.tmpl
- Cleanup the sections and packages not in RHEL8.

* Wed Jul 25 2018 Andrew Hills <ahills@redhat.com> - 8.0-10
- Drop btrfs-progs from installpkgs (RCM-38058)

* Fri Jul 20 2018 Brian C. Lane <bcl@redhat.com> - 8.0-8
- Don't activate default auto connections after switchroot
  Resolves: rhbz#1555934

* Mon Jul 09 2018 Brian C. Lane <bcl@redhat.com> - 8.0-7
- Add hostname to the rootfs for iscsi
  Resolves: rhbz#1599183

* Thu Jun 21 2018 Ian McLeod <imcleod@redhat.com> - 8.0-6
- Temporarily disable dracut-fips to allow building images in VMs

* Wed Jun 20 2018 David Cantrell <dcantrell@redhat.com> - 8.0-5
- Make sure perl-interpreter is installed

* Tue Jun 19 2018 Ian McLeod <imcleod@redhat.com> - 8.0-4
- Comment where RHEL8 removals have taken place
- Temporarily remove X server and drivers from all architectures

* Tue Jun 19 2018 Ian McLeod <imcleod@redhat.com> - 8.0-3
- Properly update build environment to pull these changes in

* Tue Jun 19 2018 Ian McLeod <imcleod@redhat.com> - 8.0-2
- Remove several _more_ packages from installer - same reason as below

* Tue Jun 19 2018 Ian McLeod <imcleod@redhat.com> - 8.0-1
- Remove several packages from installer based on current state of BaseOS/AppStream

* Mon Jun 18 2018 Will Woods <wwoods@redhat.com> - 8.0-0
- Initial creation of lorax-templates-rhel package
