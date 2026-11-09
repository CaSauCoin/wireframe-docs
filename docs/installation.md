# Installation

Install WireFrame only from the official release channel and choose the package that matches your operating system. This guide covers the pre-built packages, not source builds.

## System requirements

| | Windows | macOS | Linux |
|---|---|---|---|
| Operating system | Windows 10 or later, 64-bit | A recent macOS on Apple silicon | A Debian-based distribution (Ubuntu and similar), 64-bit |
| Package | `WireFrame_v<version>_Setup_Windows_x64.exe` | `WireFrame_v<version>_macOS.dmg` | `WireFrame_v<version>_<Distro>-<release>_amd64.deb` |
| Graphics | OpenGL 3.3 or later | OpenGL 3.3 or later | OpenGL 3.3 or later |

WireFrame draws with OpenGL, which comes from the computer's graphics driver and is not part of the installer. Without OpenGL 3.3, WireFrame cannot open its window: see [Graphics driver](#graphics-driver).

AI Copilot needs an internet connection to a hosted AI provider or a local endpoint; everything else works offline.

## Before downloading

Download from the [official WireFrame download page](https://wireframe.com.vn/download).

1. Choose the stable release unless you are deliberately testing a release candidate.
2. Read the release notes and back up active production projects before testing a release candidate.
3. Check that the downloaded file name matches your platform and the version you expect. If a checksum is published beside the download, compare it.
4. Keep operating-system security protections enabled.

### Image — Official release download page

!!! note "Image capture brief"
    1. **Prepare:** Compare the existing asset with the current release UI and list every changed label or control before recapturing.
    2. **Build the frame:** Capture the final 2.0.1 download page with version, platform, architecture, file size, and checksum visible. Replace the current image if any filename or product branding differs.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Windows

1. Run `WireFrame_v<version>_Setup_Windows_x64.exe` and check the publisher and file name Windows shows.
2. Follow the installer. It installs into *Program Files*, adds a Start menu entry, and can add a desktop icon.
3. Leave **Launch WireFrame** ticked on the last page, or start it from the Start menu.
4. If SmartScreen appears, continue (**More info → Run anyway**) only after confirming that the package came from the official release channel.

Do not disable SmartScreen globally. If the publisher, file name, or checksum is unexpected, cancel the installation and download a fresh package.

### Image — Windows installer

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the signed 2.0.1 installer or its first setup page with the exact product version visible. The previous image file was a 1×1 placeholder and must be replaced.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## macOS

1. Open `WireFrame_v<version>_macOS.dmg`.
2. Drag WireFrame to **Applications**.
3. Eject the disk image.
4. Launch WireFrame from **Applications**.

If macOS blocks the first launch, use **System Settings → Privacy & Security → Open Anyway** only after confirming the package source. Do not routinely remove quarantine attributes with a privileged Terminal command; reserve that for a verified support procedure.

### Image — macOS installation and first launch

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the final disk-image layout and the legitimate Privacy & Security approval state for 2.0.1. The previous DMG and Gatekeeper image files were 1×1 placeholders.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Linux

Download the `.deb` built for your distribution and release, then install it with the system package installer, or from a terminal:

```bash
sudo apt install ./WireFrame_v<version>_<Distro>-<release>_amd64.deb
```

`apt` installs missing dependencies. Start WireFrame from the application menu.

Before reporting a launch issue, record the distribution and release, the desktop session (X11 or Wayland), the WireFrame version, and the exact terminal output.

### Image — Linux package installation

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the supported 2.0.1 package in a current Debian-based graphical installer, including version and architecture but no local username.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## First launch

WireFrame runs in **community mode**: no account, licence key, or activation is needed. The account menu at the right end of the menu bar shows your name and mode (for example *Engineer | Community*), **Login is optional**, and offers **Check for Updates**, **Clear saved login**, **Star repository**, and **Donate / Buy me a coffee**.

On first launch, open **Preferences → Preferences...** (++ctrl+comma++) and check:

- **General** — display units (**Mil** or **Millimeter**) and autosave;
- **Appearance** — theme, accent colour, interface font and size;
- **Simulation** — that ngspice is available, and paths of optional engines;
- **AI Assistant** — only when you intend to use Copilot;
- **Updates** — the version and whether a newer one is ready.

Never show sign-in details or API keys in screenshots or support reports.

### Short video — First-run verification

!!! note "Video production brief"
    1. **Prepare:** Complete installation, use a test account, and remove credentials and private paths from every visible field.
    2. **Opening shot (2 s):** Start immediately before first launch with the installed WireFrame app visible.
    3. **Action shot (10–16 s):** Launch WireFrame, open the version/about view, open **Preferences**, then create a new empty project with a fictional name.
    4. **Result shot (4–6 s):** Hold on the empty project workspace and its **Project Structure** entry.
    5. **Deliver:** Export a **20–30 second** 1080p MP4; cut loading time and show no credentials.

<!-- wf:video id=first-run-verification
caption: Preferences, then a first empty project
project: none
setup:
- wait: 8
steps:
- wait: 1
- menu:
  - Preferences
  - Preferences...
- wait: 2
- click: '**/Cancel'
- wait: 1
- pick_folder: first-project
- menu:
  - File
  - New
  - New Project (.prjxml)...
- wait: 1
- type:
    text: My First Board
    enter: true
- wait: 3
brief_sha256: fc44e3f2c570ac8b
-->
<!-- wf:out id=first-run-verification sha=63436c8127a7 -->
<video controls muted playsinline preload="metadata" src="assets/wf/docs/installation/first-run-verification.mp4" title="Preferences, then a first empty project"></video>
<!-- /wf:out -->

## Graphics driver

WireFrame needs OpenGL 3.3, and the graphics driver is what provides it. Without it WireFrame does not open: on Windows, a message titled **WireFrame EDA could not start** says so; on Linux, WireFrame exits and prints the reason in the terminal. Macs on Apple silicon include it.

To update the driver on Windows:

1. Open **Settings → Windows Update**, install the available updates, and look under **Advanced options → Optional updates** for driver updates.
2. If that does not help, install the current driver from the maker of your graphics hardware: [Intel](https://www.intel.com/content/www/us/en/support/detect.html), [AMD](https://www.amd.com/en/support/download/drivers.html), or [NVIDIA](https://www.nvidia.com/en-us/drivers/). On a laptop, check the laptop maker's support page first.
3. Restart the computer and start WireFrame again.

On Linux, install your distribution's current graphics driver.

| Where WireFrame runs | What to do |
|---|---|
| A virtual machine | Turn on 3D acceleration in the machine's display settings. If it has none, run WireFrame on the host. |
| Remote Desktop | Start WireFrame on the computer itself first, then connect. A session started remotely may not reach the graphics hardware. |

## Updates

When a newer version is published, the **Help** menu shows **Update to v…** and **Preferences → Updates** says *A newer version is ready to download*. Use **Check for Updates** (account menu) or the check button in **Preferences → Updates** to look again. Updating opens the download page; install the new package over the old one.

If the server requires a newer version, WireFrame shows **UPDATE REQUIRED** with **UPDATE NOW** instead of the editor. **SERVICE UNAVAILABLE** means the update service could not be reached — try again later.

## Upgrade checklist

1. Save and back up important projects.
2. Close WireFrame normally.
3. Install the new package using the platform's standard process.
4. Confirm the displayed version (**Help → About WireFrame EDA** or **Preferences → Updates**).
5. Open a copy of a representative project.
6. Verify libraries, simulation engines, AI settings, ERC/DFM behavior, and one fabrication package before using the build for release work.

## Related guidelines

- [Getting Started](getting-started.md)
- [Configuration and Session](reference/config-and-session.md)
- [Release Notes](changelog.md)
- [FAQ and Troubleshooting](faq.md)
