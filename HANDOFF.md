# HANDOFF — đang làm lại docs, blog và video

Bản đầy đủ nằm trong repo WireFrame, nhánh `docs/rebuild`:
`doc_builder/HANDOFF.md` (đọc file đó trước). Tóm tắt phần thuộc repo này:

- `boards.yaml` — danh mục board thật (commit được ghim, license, vai trò
  showcase/guide/blog). Lấy + import: `python3 -m doc_builder boards . --fetch`
  (chạy từ repo WireFrame, đường dẫn tới repo này). Ghi công: `--credits`.
- `CONTENT_PLAN.md` — trang nào dùng board nào, video nào, thứ tự làm.
- Việc tiếp theo ở đây: đổi `project:` mặc định trong `.wf-docs.yaml` và 59 slot
  còn chụp trên 7805 sang `board:<id>`, chụp lại, viết sâu từng trang; kiểm
  không còn chữ tiếng Việt / đường dẫn máy trong ảnh; `docs-verify`, `mkdocs build`.
- `samples/ne555-blinker/ai_design_plan.json` còn đường dẫn tuyệt đối của máy
  (lỗi app, đã có task riêng) — đừng sửa tay file đó.
