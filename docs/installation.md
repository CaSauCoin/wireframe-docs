# Installation

This page explains how to **download, install, and start** the WireFrame tool on:

- Windows
- macOS
- Linux

It is intended for **end users** (no compiling from source).  
For developer build instructions, refer to the separate developer documentation.

> **Image placeholder**  
> `![Installation overview](img/installation/installation-overview.png)`  
> _Simple diagram showing: go to download page → download installer → install → first run & sign‑in._

---

## 1. Downloading WireFrame

WireFrame is distributed as pre‑built packages:

- **Windows**: Installer (`.exe`)
- **macOS**: Disk image (`.dmg`)
- **Linux**: Package (`.deb`)

Go to the official download page:

- **Download page:** `https://<your-domain-or-github-release-page>/wireframe`

On that page:

1. Choose the **latest stable version**.
2. Select the package that matches your operating system and architecture:
   - Windows 10/11 64‑bit
   - macOS (Apple Silicon)
   - Linux x86_64

> **Image placeholder**  
> `![Download page](img/installation/download-page.png)`  
> _Web page showing a list of available installers for Windows, macOS and Linux, with the latest stable release highlighted._

---

## 2. Windows installation

### 2.1. Download

1. On the download page, click:
   - `WireFrame-Setup-x.y.z-Windows-x64.exe` (example name).
2. Save the file to a folder you can find easily (e.g. `Downloads`).

### 2.2. Run the installer

1. Double‑click the downloaded `.exe` file.
2. If Windows shows a **SmartScreen** dialog:
   - Click **More info** → **Run anyway** (if you trust the source).
3. Follow the steps in the setup wizard:
   - Accept the license agreement.
   - Choose the installation folder (default is recommended).
   - Choose whether to create desktop / Start Menu shortcuts.
4. Click **Install** and wait for the process to finish.
5. Click **Finish** to close the installer.

> **Image placeholder**  
> `![Windows installer wizard](img/installation/windows-installer.png)`  
> _Installer wizard on Windows showing license acceptance and install location selection._

### 2.3. Start the application

There are two common ways:

- From the **Start Menu**:
  - Open Start → search for **WireFrame** → press Enter.
- From the **Desktop shortcut** (if you chose to create one):
  - Double‑click the WireFrame icon.

When running for the first time, you may see a **sign‑in or activation** window.  
Follow the on‑screen steps, then continue with the [Getting Started](../../getting-started.md) guide.

---

## 3. macOS installation

### 3.1. Download

1. On the download page, click:
   - `WireFrame-x.y.z-macOS.dmg` (example name).
2. Save the file (usually to `Downloads`).

### 3.2. Install the app

1. Double‑click the downloaded `.dmg` file to open it.
2. A window appears showing:
   - The **WireFrame** app icon.
   - A shortcut to the **Applications** folder.
3. Drag the WireFrame icon onto the **Applications** folder icon.

> **Image placeholder**  
> `![macOS dmg](img/installation/macos-dmg.png)`  
> _Standard macOS DMG window with the app icon on the left and an Applications folder on the right, with an arrow indicating drag‑and‑drop._

4. Once copied, you can eject the DMG:
   - Right‑click on `WireFrame` in the Finder sidebar → **Eject**.

### 3.3. Verify permissions (Required)

After dragging the application to the folder, you must run a system command to clear quarantine attributes and ensure the app runs correctly.

1. Open **Terminal** (press Cmd + Space, type "Terminal", and press Enter).
2. Run the following command:

```bash
sudo xattr -cr /Applications/WireFrame.app
```

3. Enter your mac password if prompted.

### 3.4. First launch (Gatekeeper)

1. Open **Launchpad** or **Applications** folder.
2. Find **WireFrame** and click it.

If macOS shows a warning such as:

> *“WireFrame” cannot be opened because it is from an unidentified developer.*

You can:

1. Open **System Settings → Privacy & Security**.
2. Scroll to the security section and click **Open Anyway** next to WireFrame.
3. Launch WireFrame again and confirm.

> **Image placeholder**  
> `![macOS security prompt](img/installation/macos-gatekeeper.png)`  
> _macOS security & privacy settings showing the "Open Anyway" option for WireFrame._

After the first successful run, macOS will remember this choice.

---

## 4. Linux installation

### 4.1. Using `.deb` package

1. Download `WireFrame-x.y.z-amd64.deb`.
2. Install via terminal:

```bash
cd ~/Downloads
sudo dpkg -i ./WireFrame-x.y.z-amd64.deb
```

3. Launch WireFrame from:
   - Application menu → search for **WireFrame**.

---

### 4.2. Runtime requirements

To run the prebuilt binary, you generally need:

- A **64‑bit Linux** distribution.
- A working **OpenGL** driver (with hardware acceleration if possible).
- Standard desktop environment packages (GTK / Qt libraries as required by your build).

Most mainstream distributions (Ubuntu, Fedora, etc.) already satisfy these requirements by default.

---

## 5. First launch and sign‑in

On first start, you may see an **activation / login** screen:

1. Enter your account email and/or license key (depending on how your copy of WireFrame is distributed).
2. Click **Sign in** or **Activate**.
3. Wait until the tool confirms that activation was successful.
4. After activation, the main UI opens and you can start using the application.

For detailed screenshots and instructions, see the **Authentication & Activation Guide** in this documentation set.

> **Image placeholder**  
> `![Activation screen](img/installation/activation-screen.png)`  
> _Window overlay asking the user to enter email and license key, with a "Sign in" or "Activate" button and a short status message._

---

## 6. Next steps

Once WireFrame is installed and launched successfully:

- Read the [Getting Started](../../getting-started.md) guide to understand the basic workflow.
- Review the [User Interface Overview](../../ui-overview.md).
- Continue with:
  - [Schematic Editor Guide](../../schematic/index.md)
  - [PCB Editor Guide](../../pcb/index.md)

for detailed, step‑by‑step instructions on creating schematics and PCB layouts.
