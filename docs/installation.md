# Installation

This page explains how to **download, install, and launch** WireFrame EDA on all supported platforms.

| Platform | Package format | Architecture |
|---|---|---|
| **Windows** | Installer `.exe` | 64-bit (x86_64) |
| **macOS** | Disk image `.dmg` | Apple Silicon (arm64) |
| **Linux** | Debian package `.deb` | 64-bit (x86_64) |

!!! info "End-user guide"
    This page covers **pre-built packages** only. For building from source, see the developer documentation in the repository.

![Installation Overview](img/installation/installation-overview.png)


---

## 1. Downloading WireFrame

Go to the official download page:

:material-download: **Download:** `https://wireframe.com.vn/download`

On that page:

1. Choose the latest published stable version. For pre-release validation, choose the **v1.5.47 release candidate** only when you accept preview software.
2. Select the package that matches your operating system and architecture.

![Download Page](img/installation/download-page.png)


---

## 2. Windows Installation

### 2.1 Download the installer

1. On the download page, click the Windows installer link:
    - Release-candidate filename: `WireFrame-1.5.47-Windows.exe`
2. Save the file to a convenient location (e.g., your `Downloads` folder).

### 2.2 Run the installer

1. Double-click the downloaded `.exe` file.
2. If Windows **SmartScreen** shows a warning:
    - Click **More info** → **Run anyway**.

    !!! warning "SmartScreen warning"
        This dialog appears because the installer may not yet be code-signed with an EV certificate. The software is safe to install if you downloaded it from the official source.

3. Follow the setup wizard:
    - **Accept** the license agreement.
    - **Choose** the installation folder (default `C:\Program Files\WireFrame\` is recommended).
    - **Optionally** create a desktop shortcut and Start Menu entry.
4. Click **Install** and wait for the process to finish.
5. Click **Finish** to close the installer.

![Windows Installer](img/installation/windows-installer.png)


### 2.3 Launch the application

Two ways to start WireFrame on Windows:

- **Start Menu**: Open Start → search for "WireFrame" → press ++enter++.
- **Desktop shortcut**: Double-click the WireFrame icon on your desktop.

---

## 3. macOS Installation

### 3.1 Download the disk image

1. On the download page, click the macOS link:
    - Release-candidate filename: `WireFrame-1.5.47-Darwin.dmg`
2. Save the file (usually to `~/Downloads`).

### 3.2 Install the application

1. Double-click the downloaded `.dmg` to mount it.
2. A Finder window appears showing:
    - The **WireFrame** application icon.
    - A shortcut to the **Applications** folder.
3. **Drag** the WireFrame icon onto the Applications folder.

![Macos Dmg](img/installation/macos-dmg.png)


4. Once copied, eject the DMG:
    - Right-click on "WireFrame" in the Finder sidebar → **Eject**.

### 3.3 Clear quarantine attributes (required)

macOS applies quarantine flags to apps downloaded from the internet. You **must** remove them before the first launch:

1. Open **Terminal** (press ++cmd+space++, type "Terminal", press ++enter++).
2. Run:

```bash
sudo xattr -cr /Applications/WireFrame.app
```

3. Enter your macOS password when prompted.

!!! danger "Do not skip this step"
    Without clearing the quarantine attribute, macOS may prevent the application from opening or silently block certain features.

### 3.4 First launch (Gatekeeper)

1. Open **Launchpad** or the **Applications** folder.
2. Find **WireFrame** and click to launch.

If macOS shows a Gatekeeper warning:

> *"WireFrame" cannot be opened because it is from an unidentified developer.*

Resolve it:

1. Open **System Settings → Privacy & Security**.
2. Scroll down and click **Open Anyway** next to the WireFrame entry.
3. Launch WireFrame again and confirm.

![Macos Gatekeeper](img/installation/macos-gatekeeper.png)


---

## 4. Linux Installation

### 4.1 Install the `.deb` package

1. Download `WireFrame-1.5.47-Linux.deb` from the release-candidate page.
2. Install via terminal:

```bash
cd ~/Downloads
sudo dpkg -i ./WireFrame-1.5.47-Linux.deb
```

If there are missing dependencies:

```bash
sudo apt-get install -f
```

3. Launch WireFrame:
    - From the **application menu** → search for "WireFrame".
    - Or from terminal: `wireframe`

### 4.2 Runtime requirements

The pre-built binary requires:

| Requirement | Details |
|---|---|
| Architecture | 64-bit x86_64 |
| OpenGL | 3.3+ with hardware acceleration |
| Desktop environment | GTK / Qt runtime libraries (usually pre-installed) |
| Distros tested | Ubuntu 22.04+, Fedora 38+, Debian 12+ |

!!! tip "Wayland users"
    If you experience rendering issues under Wayland, try launching with the X11 backend: `GDK_BACKEND=x11 wireframe`

---

## 5. Verifying the Installation

After launching, verify that everything works:

- [x] The main window opens with the dark ImGui theme.
- [x] The **menu bar** is visible at the top (File, Edit, View, Project, Tools, Help).
- [x] You can open **File → New Schematic** and see an empty schematic canvas.
- [x] You can open **File → New PCB** and see an empty PCB canvas.
- [x] The **Library panel** is visible on the right side.
- [x] **Simulation → SPICE Simulation Panel** opens for a schematic and shows the bundled ngspice status.
- [x] **Preferences → Simulation** displays engine paths and saved analysis defaults.

If any of these fail, check the [FAQ & Troubleshooting](faq.md) page.

---

## 6. Next Steps

You're ready to start designing! Continue with:

| Next page | Description |
|---|---|
| [Getting Started](getting-started.md) | Learn the basic workflow and UI layout |
| [UI Overview](ui-overview.md) | Detailed tour of every panel and toolbar |
| [Full Tutorial](tutorial/index.md) | End-to-end project from install to Gerber export |
