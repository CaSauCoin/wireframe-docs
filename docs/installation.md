# Installation

Install WireFrame only from the official release channel and choose the package that matches your operating system and CPU architecture. This guideline covers pre-built end-user packages, not source builds.

## Before downloading

Download from the [official WireFrame download page](https://wireframe.com.vn/download).

1. Confirm whether you need the stable release or the v1.5.47 release candidate.
2. Read the release notes and back up active production projects before testing a release candidate.
3. Verify the downloaded filename, version, platform, and architecture.
4. Keep operating-system security protections enabled.

### Image — Official release download page

!!! note "Image capture brief"
    1. **Prepare:** Compare the existing asset with the current release UI and list every changed label or control before recapturing.
    2. **Build the frame:** Capture the final v1.5.47 download page with version, platform, architecture, file size, and checksum visible. Replace the current image if any filename or product branding differs.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Windows

1. Download the official 64-bit Windows installer.
2. Open the installer and review the publisher and filename shown by Windows.
3. Follow the installer steps and launch WireFrame from the Start menu.
4. If SmartScreen appears, continue only after confirming that the package came from the official release channel and its checksum matches the published value.

Do not disable SmartScreen globally. If the publisher, filename, or checksum is unexpected, cancel the installation and obtain a fresh package.

### Image — Windows installer

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the signed v1.5.47 installer or its first setup page with the exact product version visible. The previous image file was a 1×1 placeholder and must be replaced.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## macOS

1. Download the package built for your Mac architecture.
2. Open the disk image and drag WireFrame to **Applications**.
3. Eject the disk image.
4. Launch WireFrame from **Applications**.

If macOS blocks the first launch, use **System Settings → Privacy & Security → Open Anyway** only after confirming the package source. Do not routinely remove quarantine attributes with a privileged Terminal command; that bypass should be reserved for a verified support procedure.

### Image — macOS installation and first launch

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the final disk-image layout and the legitimate Privacy & Security approval state for v1.5.47. The previous DMG and Gatekeeper image files were 1×1 placeholders.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## Linux

For a Debian package, open it with the system package installer or install the exact downloaded file from a terminal. If the package manager reports missing dependencies, use the distribution's normal dependency-repair workflow, then retry the launch from the application menu.

Before reporting a launch issue, record the distribution, release, desktop session, CPU architecture, WireFrame package version, and exact terminal output.

### Image — Linux package installation

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the supported v1.5.47 package in a current Debian-based graphical installer, including version and architecture but no local username.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

## First launch and sign-in

On first launch, complete the visible account or activation flow, then open **Preferences** and confirm:

- application version and tier;
- theme and units;
- autosave;
- simulation engine status;
- AI settings only when you intend to use Copilot.

Never show activation tokens or AI API keys in screenshots or support reports.

### Short video — First-run verification

!!! note "Video production brief"
    1. **Prepare:** Complete installation, use a test account, and remove credentials and private paths from every visible field.
    2. **Opening shot (2 s):** Start immediately before first launch with the installed WireFrame app visible.
    3. **Action shot (10–16 s):** Launch WireFrame, open the version/about view, open **Preferences**, then create a new empty project with a fictional name.
    4. **Result shot (4–6 s):** Hold on the empty project workspace and its **Project Structure** entry.
    5. **Deliver:** Export a **20–30 second** 1080p MP4; cut loading time and show no credentials.

## Upgrade checklist

1. Save and back up important projects.
2. Close WireFrame normally.
3. Install the new package using the platform's standard process.
4. Confirm the displayed version.
5. Open a copy of a representative project.
6. Verify libraries, simulation engines, AI settings, ERC/DFM behavior, and one fabrication preview before using the build for release work.

## Related guidelines

- [Getting Started](getting-started.md)
- [Configuration and Session](reference/config-and-session.md)
- [Release Notes](changelog.md)
- [FAQ and Troubleshooting](faq.md)
