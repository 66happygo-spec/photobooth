# 外埔長青學院 專屬拍貼機 - ANTIGRAVITY.md

## 專案入口
- 專案名稱：外埔長青學院結業典禮拍貼機 (Photobooth Web App)
- 專案用途：供結業典禮現場長輩、學員使用 iPad / 平板拍照留念，支援倒數計時、3 款主題相框選擇、4x6 吋高畫質合成，並產生 QR Code 供家屬手機下載電子相片。
- 主要工作目錄：`d:\Work\拍貼機`
- 部署目標：GitHub Pages (靜態前端)
- 雲端圖床：Cloudinary (美國加州雲端媒體服務，Unsigned Upload Preset 模式)
- 預設 branch：`main`

## 技術架構決策
1. **純前端 Web 應用**：HTML5 + Tailwind CSS + 原生 JavaScript，無需自建後端伺服器。
2. **iPad / 觸控最佳化**：大按鈕、清晰提示、直覺式防呆流程，支援 Safari「加入主畫面」全螢幕模式。
3. **高解析度 Canvas 合成**：相片格式為標準 4x6 吋（3:2 橫式比例，1800 x 1200 px）。
4. **雲端 QR Code 轉發**：合成完成後自動上傳至圖床並產生公開 URL QR Code；同時於 iPad 本地觸發備份存檔。

## 工作規則
- 回應使用繁體中文（台灣）。
- 涉及檔案操作時回報完整產出位置。
- 開工時讀取本檔、交接日誌 (`handoff.md`)，並檢查 Git 狀態。
- 收工時更新交接日誌，檢查 diff 後只精準提交相關檔案。
- 不把每日流水帳寫進本檔。

## 安全原則
- 不要 commit API key、token、密碼、私密憑證（例如 ImgBB API key 需提供設定介面或環境設定引導）。
- 不要 commit 個人私密資料。
- 不要使用無差別 `git add .`。
