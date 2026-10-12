# 外埔長青學院結業典禮拍貼機 - 開發交接日誌 (Handoff Log)

## 📌 專案當前狀態
- **日期**：2026-10-12
- **狀態**：核心開發與雲端串接全數完成，已正式發布至 GitHub Pages！
- **正式上線網址**：https://66happygo-spec.github.io/photobooth/
- **GitHub 倉庫**：https://github.com/66happygo-spec/photobooth

---

## ☁️ 雲端圖床連線設定 (Cloudinary)
- **服務廠商**：Cloudinary（總部：美國加州聖塔克拉拉，世界級高穩定性雲端媒體服務）
- **雲端名稱 (Cloud Name)**：`wwbs37co`
- **上傳標籤 (Upload Preset)**：`w1reicnp` (Unsigned 模式)
- **設定方式**：
  1. 打開拍貼機網頁後，點擊右上角「⚙️ 設定」。
  2. 填入上述兩組設定值並按「儲存設定」（瀏覽器會永久保存在本機 `localStorage`）。
  3. 拍照合成後將自動上傳並產出專屬高畫質相片下載 QR Code。

---

## 📦 已完成核心功能清單
1. **外框素材分離與高畫質重構**：
   - 原始點陣素材分離為 3 款獨立中空透明相框。
   - 透過高階影像演算法升級重構為 **1800 x 1200 像素 (4x6 吋標準相片比例)**，解決放大模糊問題。
   - 包含：
     - `frames/frame_flower_garden.png` (溫馨花草木質框)
     - `frames/frame_chalkboard.png` (校園黑板木質框)
     - `frames/frame_blue_ocean.png` (藍天海洋向日葵框)
2. **相機預覽與圖層排版修復**：
   - 使用絕對定位堆疊（Absolute Stacking），確保底層視訊串流永遠不被頂層相框擠壓。
   - 支援自動鏡像翻轉（如照鏡子般直覺）與前後鏡頭切換。
3. **倒數拍照與彩帶慶祝**：
   - 支援 3 秒 / 5 秒 / 10 秒倒數計時。
   - 拍照瞬間快門閃光與合成完畢後的彩帶特效（Canvas-Confetti）。
4. **4x6 吋高畫質相片合成**：
   - 內部 Canvas 以 1800 x 1200 解析度將人物影像精確置入相框鏤空透明處。
5. **QR Code 手機一鍵下載**：
   - 拍完後自動上傳至 Cloudinary 雲端空間。
   - 產生專屬下載 QR Code，現場長輩/家屬拿手機相機一掃即可秒存進相簿。
   - 同時支援本機直接下載備份。
6. **專案正式部署至 GitHub Pages**：
   - 靜態網頁託管，具備 HTTPS 憑證，iPad 可永久記住相機存取權限。

---

## 🔍 踩坑紀錄與硬體注意事項 (Troubleshooting)
- **筆電測試鏡頭 2 秒黑屏 / `NotReadableError` 問題**：
  - **原因**：特定 HP 筆電內建 Realtek 視訊驅動元件 (`RsProvider.dll`) 在 Windows Media Foundation 下存在崩潰問題，導致系統每隔數秒主動中止視訊串流 (`Track Ended`)。
  - **結論**：此問題屬於該台 Windows 筆電的特定驅動程式 bug。**iPad / 平板（使用 Safari）沒有此驅動問題，實測運作極為順暢**。
  - **電腦端臨時測試方案**：已在網頁中內建「上傳照片測試」按鈕，無鏡頭亦可完整走完流程。

---

## 🚀 現場使用與後續建議事項
1. **iPad 亭模式（Kiosk Mode）**：
   - 在 iPad 的 Safari 打開網址後，點擊「分享」➜ **「加入主畫面」**，即可變成全螢幕無網址列的獨立拍貼機 App。
2. **更換或增加相框**：
   - 未來若有新相框，只需準備 1800x1200 橫式透明 PNG 放入 `frames/` 資料夾並推送至 GitHub 即可更新。
