# Release Media Production

Use this production standard for every **Image needed**, **Video needed**, and **Diagram replacement needed** brief in this guideline. The brief at each insertion point defines the subject and exact UI state; this page defines how to prepare, capture, finish, and approve it.

## Prepare one clean release workspace

1. Install the same WireFrame build named by the release guideline.
2. Create a fictional sample project under a neutral path such as `Demo/WireFrameRelease`.
3. Use public component data and public manufacturer datasheets only.
4. Remove API keys, email addresses, customer names, usernames, machine names, notifications, and unrelated applications from view.
5. Reset the app to the dark release theme, 100% UI scale, and a clean panel layout.
6. Set the display to at least 1920 × 1080 and disable operating-system notifications.
7. Prepare the start state before recording. Do not make viewers wait through project loading, typing long prompts, AI latency, or file conversion unless progress is the subject of the clip.

## Produce a UI image

Follow these steps in order for every image brief:

1. **Build the state.** Open the page, panel, menu, result, or selected object named in the local brief. Use exactly the requested labels and example state.
2. **Clean the frame.** Close unrelated panels, move the pointer away from important text, remove transient tooltips, and verify that no private data is visible.
3. **Compose the shot.** Keep the requested control and its result in the same frame when possible. Use whitespace to establish hierarchy; do not crop window titles, selected objects, warnings, or primary actions.
4. **Capture at native resolution.** Take a PNG screenshot without browser scaling or lossy compression. Capture the full window first, then crop nondestructively.
5. **Finish carefully.** Straighten the crop, balance exposure only if needed, and add no more than three subtle callouts. Never redraw UI, replace labels, fabricate results, or use a generative model to alter engineering content.
6. **Export.** Use sRGB PNG. Prefer the dimensions in the local brief; otherwise use 1400–1600 px width for a full workspace and 900–1200 px for a focused dialog.
7. **Approve.** At 100% zoom, confirm that labels are readable, the intended state is unambiguous, release branding is current, and no secret or private path remains.

## Produce a UI video

Every local video brief names the action sequence. Turn that sequence into this five-shot timeline:

1. **Opening state — 1–2 seconds.** Show the prepared starting panel or canvas without moving the pointer. The viewer must understand where the action begins.
2. **Locate the control — 1–2 seconds.** Move the pointer in one smooth path to the named menu, object, or button. Pause briefly before clicking.
3. **Perform the workflow — main duration.** Execute the actions in the exact order written in the local brief. Show one click at a time, keep menus open long enough to read, and remove waiting time with a clean cut rather than speeding through the interface.
4. **Show the result — 2–3 seconds.** Stop moving the pointer. Keep the changed object, refreshed status, validation result, or destination panel visible long enough to inspect.
5. **End cleanly — 1 second.** Finish on the result rather than fading to a blank frame. Do not add an outro unless the release campaign supplies one.

### Recording settings

- Record at 1920 × 1080, 30 fps, with the application at 100% scale.
- Show a restrained click highlight; do not use a large cursor trail.
- Record without microphone audio. Add narration and captions only after the visual cut is approved.
- Use hard cuts for waiting periods. Do not fake AI, import, simulation, or validation speed.
- Keep zoom and panning deliberate. Avoid handheld-style motion, animated backgrounds, and decorative transitions.
- Export an H.264 MP4 for delivery and keep the lossless or high-bitrate master. WebM may be generated for the website afterward.
- Target 8–18 seconds for one interaction and 20–35 seconds for a multi-stage validation workflow, unless the local brief specifies otherwise.

### Captions and callouts

1. Write a single outcome-led title, no more than eight words.
2. Add a short action caption only when the UI label is too small at the final embed size.
3. Place captions outside the active control and keep each on screen for at least 1.5 seconds.
4. Use the release accent color for one highlight at a time.
5. Do not claim that AI output, a route, an imported library, or a generated component is approved unless the clip visibly shows its verification gate.

## Produce a workflow diagram

1. Copy the exact stages from the local diagram brief.
2. Give each stage one short verb-led label and one consistent shape.
3. Arrange the flow left to right for desktop pages; wrap only when the diagram would otherwise become unreadable.
4. Show review gates as distinct checkpoints and loop failures back to the relevant correction stage.
5. Build the diagram in Figma, Canva, or another vector tool. Do not use ASCII art, Mermaid screenshots, or generated text inside an AI image.
6. Export SVG for the site and a 2× PNG fallback. Verify every label manually.

## AI-assisted finishing boundary

AI may help remove a neutral background, balance contrast, generate a clean title card, transcribe narration, or suggest captions. AI must not change component values, pin names, pad numbers, net names, warning states, measurements, file names, menu labels, or validation results. Keep the original capture and compare it with the finished asset before approval.

## Final release check

- The asset follows its local brief in the correct order.
- All visible UI comes from the current release build.
- Pointer movement and cuts are calm and intentional.
- Text remains readable at the documentation embed size.
- No credentials, private paths, customer data, or proprietary datasheet content appears.
- The final frame proves the stated outcome.
- Source capture, editable project, and final export are archived together.
