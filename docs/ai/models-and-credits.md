---
description: Choose who pays for WireFrame's AI Copilot — your plan's WireFrame credit or your own key at OpenRouter, DeepSeek or Google AI — pick the design and fast models, and see exactly what is sent where.
---

# Models, Credit and Your Data

The AI Copilot needs a language model. In WireFrame you decide **who pays for it** — your plan's WireFrame credit, or your own account at a model provider — and which models do the work. This page covers the settings, the plans, and what leaves your computer.

Open the settings with **Preferences ▸ AI Assistant**, or the **⋮** menu of the AI Copilot panel ▸ **AI settings…**.

## Who pays for the AI

The first card asks one question: **Pay with**

| Choice | Who is billed | What you need |
|---|---|---|
| **WireFrame credit** | Your plan's AI credit | Nothing — sign in to WireFrame |
| **OpenRouter** | Your OpenRouter account (one key for Gemini, Claude, GPT and many others) | An OpenRouter API key |
| **DeepSeek** | Your DeepSeek account | A DeepSeek API key |
| **Google AI** | Your Google AI Studio account | A Google AI API key |

**With WireFrame credit**, the card shows **Credit left**. One credit is **$0.01 of model use**; it renews with your plan each month. **Refresh** asks again. If your plan has no AI credit, the card says so: choose a provider and use your own key.

**With your own key**, paste it in **API key**, then **Save & test**; the **Connection** line says whether it works. **Get a key at …** names the provider's page. The provider bills you directly; WireFrame's AI service forwards the key with each request and **does not store it**. **Clear key** removes it from this computer.

Each provider keeps its **own** key, so switching between them never sends one company's key to another. If the choice and the saved key disagree — a provider chosen with no key yet, or an old configuration pointing somewhere the service does not forward to — WireFrame refuses the request **before anything leaves the computer** and tells you what to fix, rather than billing the wrong party.

## Models

| Field | Used for |
|---|---|
| **Design model** | Planning the BOM and the netlist, repairing findings, generating library parts, reviewing a board — the model that decides circuits |
| **Fast model** | Routing your request, naming, requirement research, board questions — classification and summaries |

On WireFrame credit the pickers offer the models the credit funds; a model that is not funded is flagged and fixed in one click. With your own key, any model your provider serves can be chosen.

## Plans and the AI

| Plan | AI Copilot |
|---|---|
| **Free** | Every design tool, with no time limit — no AI Copilot, with or without your own key |
| **Plus**, **Pro** | The AI Copilot on a monthly WireFrame credit — or on your own key — and more devices |
| **Enterprise** | By agreement |

Current prices, credit amounts and device counts are on the [pricing page](https://wireframe.com.vn/pricing). There is no trial: the AI Copilot comes with a paid plan. The design tools — schematic, PCB, 3D, checks, simulation and fabrication export — never depend on the AI or on a paid plan.

## What is sent, and where

- **Your projects stay on your computer.** WireFrame has no cloud copy of your design.
- A Copilot request carries **only what that request needs**: your message, and the part of the design it is about — a block, a net, the BOM rows in question, a datasheet page.
- Requests go through **WireFrame's AI service**, which adds WireFrame's instructions, checks your plan and spending limits, and forwards the request to the model provider. It records which model and which task were used, and what it cost — **not** the contents of your messages or your design.
- The **model provider** — the one behind the WireFrame credit, or the one whose key you gave — processes the request under its own terms.
- The design tools work **offline**. The app confirms your plan with WireFrame at least every 14 days; until then it keeps working without a network.

!!! warning "Keys are secrets"
    Do not put an API key in a screenshot, a shared project, a bug report or a configuration you send someone. If one leaks, revoke it at the provider.

## Troubleshooting

| You see | What to do |
|---|---|
| *Your plan has no AI credit* | Choose OpenRouter, DeepSeek or Google AI and paste your own key — or upgrade to Plus or Pro |
| *Choose who pays above; until you do, AI requests stop on this computer* | An old configuration points at an endpoint the service does not forward to. Pick a choice in **Pay with** |
| *… rejected this key* | The key is wrong, revoked or out of balance at the provider. Make a new one there |
| A model returns empty answers | Pick another model in **Models**; on credit, use one the picker marks as funded |

## See also

- [AI Copilot overview](index.md)
- [Copilot commands](commands.md)
- [FAQ](../faq.md)
