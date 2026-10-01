# Configuration and Session

WireFrame saves workspace preferences and enough session information to reopen recent projects and documents. Use the application settings for normal changes; manual file editing is a recovery procedure.

## What WireFrame remembers

Depending on the feature used, the local configuration can include:

- Open projects, open documents, and standalone files.
- Recent open, save, import, export, and project folders.
- Window position, size, docking slots, and multi-monitor behavior.
- Units, grid and snap settings, rotation step, and default trace width.
- Autosave preferences.
- Simulation defaults.
- Layer visibility and lock state.
- Custom keyboard shortcuts.
- Sign-in/device session data and AI provider settings.

!!! warning "Contains private data"
    The configuration can contain an authentication token and an AI API key. Never attach the complete file to an issue report or place it in source control.

## Change preferences safely

Open **Preferences** and use the relevant category:

| Category | Typical settings |
|---|---|
| Appearance | Theme, units, autosave |
| Panels or workspace | Docking, panel behavior, multi-monitor options |
| Grid and editing | Grid visibility, snapping, rotation, PCB defaults |
| Simulation | Engine executables, analysis, transient defaults |
| AI | OpenRouter key and model |
| Version and account | Tier, version, and update information |

Close Preferences after confirming the new value. For an important project, restart WireFrame once and verify that the setting persists.

## Session restoration

WireFrame records the currently open project and document paths during normal use and shutdown. At the next launch it attempts to restore files that are still available.

If an item is not restored:

1. Confirm that the file or drive still exists at the saved location.
2. Open the project manually from **File → Open Project (.prjxml)** or **Open File**.
3. Close WireFrame normally so the refreshed session is saved.

Unsaved design edits are not a substitute for autosave or a deliberate **Save** operation. Save before simulation, export, or application update.

## Local configuration location

Current builds use `user_config.json` in the WireFrame configuration directory:

| Platform | Current location |
|---|---|
| Windows | `%APPDATA%\WireFrame\user_config.json` |
| Linux | `~/.config/wireframe/user_config.json` |
| macOS | `~/.config/wireframe/user_config.json` |

The file is created automatically. Its internal fields are implementation details and may change between releases, so examples of the raw JSON are intentionally omitted from this guideline.

## Reset WireFrame preferences

Use this only when startup or workspace state remains broken after a normal restart.

1. Close WireFrame.
2. Make a private backup copy of `user_config.json`.
3. Rename the original file, for example to `user_config.backup.json`.
4. Start WireFrame and verify the clean defaults.
5. Re-enter preferences manually. Do not copy authentication or AI-key fields into a support ticket.

Renaming is preferable to immediate deletion because the previous settings remain recoverable. The reset clears saved session, layout-related preferences, custom shortcuts, sign-in state, and AI settings; it does not delete project files.

### Image — Preferences categories

!!! note "Image capture brief"
    1. **Prepare:** Open a clean release-build workspace with fictional or public sample data and prepare the requested state.
    2. **Build the frame:** Capture the complete Preferences window in v1.5.47 with the category list visible. Use a test account, hide all credentials, and show no local user path.
    3. **Clean the frame:** Close unrelated panels and tooltips, move the pointer away from key text, and hide credentials, usernames, customer data, and private paths.
    4. **Capture and finish:** Capture a native-resolution PNG, crop without cutting titles or primary actions, and add at most three subtle callouts without altering engineering content.
    5. **Approve:** Check the image at 100% zoom for current labels, readable evidence, correct release branding, and absence of sensitive information.

### Short video — Recover a damaged workspace configuration

!!! note "Video production brief"
    1. **Prepare:** Back up the demo configuration and open its folder at a neutral, masked path.
    2. **Opening shot (2 s):** Show WireFrame's intentionally altered demo layout, then close the app normally.
    3. **Action shot (10–16 s):** Rename only the demo config file, relaunch WireFrame, and wait for the default configuration to be recreated.
    4. **Result shot (4–6 s):** Hold on the restored default workspace and confirm the recreated config without exposing its full private path.
    5. **Deliver:** Export a **20–30 second** 1080p MP4; blur the operating-system username and retain the backup until review is complete.

## Related guidelines

- [Projects and Files](../projects.md)
- [Simulation Engines and Models](../simulation/engines-and-models.md)
- [AI Copilot](../ai/index.md)
- [FAQ and Troubleshooting](../faq.md)
