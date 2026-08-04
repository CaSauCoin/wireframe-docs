# wireframe-docs — Agent Guide

> Entry point cho mọi coding agent.
## Codebase store — đọc trước khi quét repo

Toàn bộ index / RAG / KG / cache / memory nằm ở `wireframe-codebase/` (thư mục
anh em với repo này). Dùng `wfc` — stdlib Python, chạy được ở bất kỳ đâu, kể cả
trong git worktree, không cần cài gì:

```bash
wfc search "trace routing"        # tìm file + symbol trên cả 4 repo
wfc search "thư viện linh kiện"   # tiếng Việt cũng được
wfc symbol SelectionManager       # file nào định nghĩa
wfc deps Common/Manager/Document.hpp   # đổi file này thì vỡ chỗ nào
wfc recall                        # quyết định đã chốt
wfc notes                         # ghi chú agent trước để lại
wfc note "..." -f <file>          # để lại phát hiện cho agent sau
```

Đường dẫn: `../wireframe-codebase/bin/wfc`
(hoặc `ln -s .../wireframe-codebase/bin/wfc ~/.local/bin/wfc`)

**Quy tắc:** `wfc search` trước, mở tối đa 5 file từ kết quả. Không grep cả repo.
Nếu được harness dispatch, `BRIEF.md` đã chứa sẵn phần liên quan — đọc và làm luôn.

Chi tiết: `../wireframe-codebase/AGENTS.md`
