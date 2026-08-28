# Configuration and Session Storage

WireFrame stores user configuration and session data in a JSON file via the configuration system. This page documents file locations, session behavior, and how to reset configuration.

---

## Config File Location

| OS | Path |
|---|---|
| **Linux** | `~/.config/wireframe/user_config.json` |
| **Windows** | `%APPDATA%\WireFrame\user_config.json` |
| **macOS** | `~/Library/Application Support/WireFrame/user_config.json` |

WireFrame ensures the directory exists and creates the file if it doesn't already exist.

---

## Config File Structure

The config file is a JSON document with the following sections:

```json
{
  "session": {
    "openProjects": [
      "/home/user/Projects/MyBoard.prjxml"
    ],
    "openDocs": [
      "/home/user/Projects/main.schxml",
      "/home/user/Projects/board.pcbxml"
    ],
    "simAnalysisType": 0,
    "simStopTime": 5.0,
    "simStopTimeUnit": 1,
    "simTimeStep": 10.0,
    "simTimeStepUnit": 2,
    "simEngineNgspiceCliPath": "",
    "simEngineXycePath": "",
    "simEngineLTspicePath": ""
  },
  "ai": {
    "apiKey": "",
    "provider": "openrouter"
  }
}
```

### Sections

| Section | Description |
|---|---|
| `session` | Session restoration data (open projects and documents) |
| `ai` | AI Copilot configuration (API key, provider) |

---

## Session Data

Session data tracks:

| Field | Type | Description |
|---|---|---|
| `openProjects` | Array of strings | Paths to project files (`.prjxml`) open during last session |
| `openDocuments` | Array of strings | Paths to schematic/PCB files (`.schxml`, `.pcbxml`) open during last session |
| `simAnalysisType` | Integer | Default simulation analysis: transient, AC, DC sweep, or operating point |
| `simStopTime` / `simStopTimeUnit` | Number / integer | Default transient duration and its unit |
| `simTimeStep` / `simTimeStepUnit` | Number / integer | Default transient step and its unit |
| `simEngine*Path` | String | Optional executable location for an external simulator |

### Startup behavior

1. WireFrame reads the config file.
2. WireFrame reopens listed projects (if files still exist on disk).
3. the document manager reopens listed documents.
4. The **Project Structure** and **Editor** tabs are re-populated.

### Automatic saving

The config is updated automatically when:

- You **open or close** a project or document.
- The app is **closed normally** (session snapshot).
- You change defaults or engine paths in **Preferences → Simulation**.

---

## Editing preferences safely

Use the in-app **Preferences** pages for normal changes. In particular, use **Preferences → Simulation** to set analysis defaults and optional simulator executables.

Edit `user_config.json` by hand only while WireFrame is closed. Unknown or invalid values may be replaced by defaults at startup.

### AI configuration

The `ai` section stores Copilot settings:

| Field | Type | Description |
|---|---|---|
| `apiKey` | String | OpenRouter API key for LLM access |
| `provider` | String | LLM provider name (default: `"openrouter"`) |

!!! info "Setting the API key"
    Open **View → AI Copilot → Settings**, then enter the API key in the application. Avoid placing real credentials in screenshots, example projects, or issue reports.

---

## Resetting Configuration

### Reset layout and session

| Method | Steps |
|---|---|
| **Delete config** | Remove `user_config.json` — the app recreates it with defaults on next launch |
| **Delete ImGui config** | Remove `imgui.ini` in the working directory to reset panel layout |

### Reset everything

```bash
# Linux
rm ~/.config/wireframe/user_config.json
rm imgui.ini  # if present in the app directory

# Windows (PowerShell)
Remove-Item "$env:APPDATA\WireFrame\user_config.json"
Remove-Item imgui.ini
```

!!! warning "Data loss"
    Deleting the config file removes all saved session data. You will need to reopen your projects.

---

## See Also

- [Installation](../installation.md)
- [Projects & Files](../projects.md) — project and document management.
- [Simulation Engines](../simulation/engines-and-models.md) — configure and troubleshoot optional simulators.
- [FAQ & Troubleshooting](../faq.md) — common config-related issues.
