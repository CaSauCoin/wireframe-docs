# Product Documentation & Guides Portal (`/Guide_line`)

This directory houses the WireFrame official user manual, quickstart tutorials, advanced layout guides, and API reference documentation. It is built as a static website powered by **MkDocs** and the **Material for MkDocs** theme.

## 1. High-Level Architecture

Documentation source markdown files are hosted under `/docs` and compiled into a highly responsive, modern static website.

```
       ┌────────────────────────┐
       │   Markdown Guides      │
       │    (`/docs/*.md`)      │
       └───────────┬────────────┘
                   │
                   ▼ [MkDocs Build / mkdocs.yml]
       ┌────────────────────────┐
       │   Static HTML Site     │
       │    (`/site/*`)         │
       └───────────┬────────────┘
                   │
                   ▼ [Local Server / Vercel Cloud]
       ┌────────────────────────┐
       │     Doc Portal Web     │
       │  (http://127.0.0.1:8001)│
       └────────────────────────┘
```

---

## 2. Directory & Asset Layout

| Path | Purpose | Key Details |
|:---|:---|:---|
| `mkdocs.yml` | MkDocs Configuration | Outlines the documentation hierarchy (Navigation), custom search indices, color theme settings (Slate Dark / Light), and extensions. |
| `run_dev.sh` | Local developer script | Auto-initiates virtual environments, installs requirements, and boots the documentation server at `http://127.0.0.1:8001` with hot-reload enabled. |
| `package.json` | Web scripts | Maps build commands for deployment pipelines. |
| `vercel.json` | Vercel Static Config | Hosts and directs requests on Vercel networks. |
| `/docs` | Source Markdown files | Structured documentation files: tutorials, FAQs, PCB guidelines, UI overviews, and changelogs. |
| `/site` | Compiled Output | Directory generated on build, containing optimized static HTML, CSS, JS, and image assets. |

---

## 3. Guide Categories in `/docs`

- **Getting Started** (`getting-started.md`): Installation checklists, compiler dependencies, project creations, and workspace settings.
- **UI Overview** (`ui-overview.md`): Map of ImGui panel widgets (Canvas, Library Search, Properties Inspector, Command Console).
- **Schematic Capture** (`schematic/`): Symbol placements, wire drawings, net labels, and ERC audits.
- **PCB Layout** (`pcb/`): Physical routing, trace widths, layers settings, via structures, thermal relief zones, and DFM rules.
- **Advanced Features** (`advanced/`): Automated fuzzy symbol matching, AI Copilot chat controls, and NgSpice circuit simulator operations.

---

## 4. Run & Build Locally

### Launch Live Preview
Boot the documentation server locally with live reload:
```bash
chmod +x run_dev.sh
./run_dev.sh
```
This activates a background MkDocs server. Access the documentation portal in your browser at `http://127.0.0.1:8001`.

### Build Production Assets
To compile the static pages for web server deployment:
```bash
python3 -m mkdocs build
```
This generates the optimized static build inside the `/site` directory.
