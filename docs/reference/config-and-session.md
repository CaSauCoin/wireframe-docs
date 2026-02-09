# Configuration and Session Storage

WireFrame stores user configuration and session data in a JSON file via `ConfigManager`.

---

## Config file location

On Linux:

- Under the user’s home directory, in `~/.config/wireframe/user_config.json`.

On Windows (if used):

- Under `%APPDATA%\WireFrame\user_config.json`.

`ConfigManager::getConfigPath` ensures the directory exists and creates the file if needed.

---

## Session data

`SessionData`:

- `openProjects` – list of project paths open during last session.
- `openDocuments` – list of schematic/PCB files open during last session.

Stored as:

```json
"session": {
  "openProjects": [
    "/path/to/Project1.prjxml"
  ],
  "openDocs": [
    "/path/to/Project1_sch.schxml",
    "/path/to/Project1_pcb.pcbxml"
  ]
}
```

On startup:

1. `ConfigManager::load` reads config.
2. `ProjectManager` and `Document_Manager` reopen listed projects and documents, if they still exist.

---

## Updating and clearing config

The app updates config:

- When auth data changes (login/logout).
- When session data changes (opening/closing projects/documents).

You can:

- **Clear auth data**:
  - Use “Log out” / “Deactivate” action or delete the config file.
- **Reset layout and session**:
  - Delete `user_config.json` and let the app recreate it on next launch.

> **Image placeholder**  
> `![Config JSON](img/reference/config-json.png)`  
> _Example of the JSON config file opened in a text editor, with auth and session sections highlighted._