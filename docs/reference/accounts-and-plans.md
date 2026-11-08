---
description: Sign in to WireFrame EDA from the desktop app, how devices and plans work, working offline, usage statistics, updates, and where to report a problem.
---

# Account, Plans and Devices

Schematic, PCB layout, 3D, SPICE and fabrication output are free with no time limit. An account ties your copy of the app to a plan — which decides whether you have the AI Copilot, MCP, the High-Speed Workbench and the Power Analyzer, the AI credit, and how many computers you can use at once — and opens the full posts on the blog.

## Sign in

The first time the app starts it asks you to sign in. Choose **Sign in with browser**: your browser opens wireframe.com.vn, you sign in with **email**, **Google** or **GitHub**, and the app is signed in when you come back — no password is typed into the app. A new browser gets a 6-digit code by email the first time.

The account menu (top right of the window, *name · plan*) shows who is signed in — initials, name and email — and the plan, and has:

| Item | What it does |
|---|---|
| **Upgrade** | On Free: opens the pricing page |
| **Account & usage** | Opens the app's account window: plan, AI credit, the last 30 days, your devices |
| **Plans & billing** | Opens your account page on the website |
| **Check for updates** | Asks for a newer release now; the right-hand side says *Up to date* or which version is available |
| **Sign out of this device** | Signs out and frees this computer's device slot |

## Devices

Each plan allows a number of computers signed in at the same time:

| Plan | Computers at once |
|---|---|
| **Free** | 1 |
| **Pro** | 3 |
| **Max** | 5 |
| **Enterprise** | 10 |

To use another one, sign one out — from that computer, from **Account & usage** in the app, or from **Plans & billing** (your account page on the website); both list every device with its last use.

## Plans

- **Free** starts the first time you sign in **from the desktop app**: schematic, PCB layout, 3D, DRC and DFM, SPICE and fabrication output, with no time limit. It has no AI Copilot, no MCP, and no High-Speed Workbench or Power Analyzer — those are not shown on Free.
- **Max** and **Pro** add the AI Copilot — on a monthly AI credit (see [AI Credit and Your Data](../ai/models-and-credits.md)) — MCP ([Use WireFrame from your own agent](../ai/mcp.md)), the High-Speed Workbench and the Power Analyzer, and more devices; **Enterprise** is by agreement.
- There is no trial.

Prices and amounts are on the [pricing page](https://wireframe.com.vn/pricing). A plan's end date is counted on WireFrame's clock, not your computer's.

## Working offline

After signing in, the app works without a network. It confirms your plan with WireFrame at least every **14 days**; within that time nothing needs to be online except the AI Copilot (which needs its model provider) and online library downloads.

## Usage statistics

WireFrame can send usage statistics — feature names, counts, session length, the version and the operating system — to help decide what to build next. They never contain project contents, file names, part numbers or AI prompts. Turn them off in **Preferences → Updates** (**Usage statistics**), or from the account page on the website.

## Updates

**Check for updates** in the account menu, or **Preferences → Updates → Check now**, looks for a newer release; **Help → Download Latest Version** opens the download page.

<!-- wf:before-release -->
Installers for Windows, macOS on Apple Silicon and Linux are on [wireframe.com.vn/download](https://wireframe.com.vn/download) and on [GitHub Releases](https://github.com/CaSauCoin/WireFrame_Product/releases).
<!-- wf:after-release -->
Installers for Windows, macOS on Apple Silicon and Linux are on [wireframe.com.vn/download](https://wireframe.com.vn/download). Releases before 2.0.1 are on [GitHub Releases](https://github.com/CaSauCoin/WireFrame_Product/releases).
<!-- wf:end-release -->

## Report a problem or ask for a feature

**Help → Report a Bug...** and **Help → Request a Feature...** open a form inside the app that sends your report with the app's version and your operating system. You can also open an issue on [GitHub](https://github.com/CaSauCoin/WireFrame_Product/issues). Leave out private project files, keys and customer data.

## See also

- [Install](../installation.md)
- [FAQ & troubleshooting](../faq.md)
- [AI Credit and Your Data](../ai/models-and-credits.md)
