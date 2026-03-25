---
name: universal-website-cloner
description: 將外部網址、文件或設計稿無損轉換，並「自動分析與克隆原站視覺風格」的自動化工作流。內建「視覺風格提取」、「Awwwards 級高級排版」、「完美 RWD」、「圖標徹底抹殺（滿版實相化）」與「具備世界觀的強制生圖」，確保設計極致還原、視覺豐富度最大化。
---

# 萬用網頁內容與風格克隆工作流 (Universal Style Cloner)

當使用者提供目標網址、上傳文件或 Figma 截圖時，請嚴格按照以下三個階段執行。**絕對不可跳過階段一。**

## 【階段一：視覺風格提取與內容盤點 (Style Analysis & Inventory)】
在撰寫 HTML 前，請先仔細讀取目標內容，輸出以下兩大份額的盤點報告：

**【A. 視覺 DNA 提取 (Visual Style DNA)】- 極度重要**
請分析原網站（或根據文件屬性推演）的設計語彙，定義以下 UI 規範：
1. **主輔色調 (Colors)**：提取 Primary Color、Secondary Color 與背景色系（提供 Tailwind 近似色碼）。
2. **字體風格 (Typography)**：判斷是無襯線體、襯線體還是圓體？
3. **按鈕與形狀 (Shapes)**：直角、小圓角還是全圓角？是否有陰影？
4. **整體氛圍 (Vibe)**：例如「極簡科技風」、「華麗電競風」、「活潑卡通風」。
5. **微距佈局與遮罩 (Micro-Layouts & Overlays)：** 仔細觀察卡片與 Banner 內部細節。是否有漸層遮罩 (Gradient Overlays) 疊加在圖片上？是否有絕對定位 (Absolute Positioning) 的懸浮按鈕、Tag 標籤或頭像 (Avatar)？

**【B. 網站架構與內容盤點 (Content Inventory)】**
1. **網站架構樹狀圖 (Site Map)：** 規劃需要拆分幾個獨立 HTML 頁面及檔名。
2. **導覽列層級：** 精準畫出選單的樹狀結構（含下拉式次選單）。
3. **內容與微小狀態盤點：** 列出每個頁面的區塊與數量，強制捕捉「活動時間」、「待公布」等微小狀態文字。
4. **全域雜訊過濾：** 自動過濾掉 Cookie 橫幅或浮動廣告。

*⚠️ 警告：這是一個強制的思考鏈過程，你必須先印出這份包含「視覺 DNA」與「內容架構」的清單，確認無誤後才能進入階段二。*

## 【階段二：自適應程式碼生成與高級排版 (Adaptive HTML & Premium Layout)】
完成盤點後，請**完全拋棄預設風格**，嚴格根據提取出的「視覺 DNA」撰寫 Tailwind HTML。

- **動態 Tailwind Config：** 在 `<head>` 中寫入對應的 `tailwind.config`，將主色調與輔助色變數化。
- **完美 RWD 與行動優先 (Mobile-First Responsiveness)：** 全站必須具備 100% 的響應式設計。預設採用手機版單欄佈局 (`flex-col`, `grid-cols-1`)，在平板或桌面版才切換為多欄。導覽列在手機版必須轉換為漢堡選單結構。標題大小與區塊間距必須隨螢幕縮放（例如 `text-4xl md:text-8xl`），確保手機端瀏覽不擁擠。
- **高級排版指令 (Premium Design Directives) - 拒絕廉價套版感：**
  - 絕對禁止全站只使用無聊的置中對齊或標準等寬網格。
  - 強制混用「便當盒佈局 (Bento Box)」、「圖文不對稱排版」。
  - 創造極致的字體對比（超大標題搭配緊湊字距，優雅內文搭配寬鬆行高），並維持區塊間的大量留白呼吸感 (`py-24` 以上)。
  - 善用毛玻璃特效 (`backdrop-blur-xl`) 與微互動（平滑懸停放大、位移）。
- **極致還原內部佈局 (Pixel-Perfect Inner Layouts)：** 絕對禁止將複雜的圖文卡片簡化為單純的 `<img>`。遇到如 Banner、個人資訊卡等區塊，必須精準使用 Tailwind 的 `relative` 與 `absolute` 進行絕對定位，並搭配 `bg-gradient-to-*` 製作漸層遮罩，完美還原設計稿中的文字疊加、懸浮按鈕與特殊 Icon 排版。
- **獨立檔案輸出與正確路由：** 為每一個頁面建立獨立 Code Block，確保 Navbar 連結 (`href`) 精準指向本地檔名。
- **來源語系絕對保留 (Source Language Preservation)：** 盤點內容 100% 寫入 HTML，禁止使用 ``。導覽列 (Navbar)、按鈕文字與所有介面標題，必須 100% 忠實呈現來源文件/網址的「原始語言」。絕對禁止 AI 在非英文來源的情況下，擅自套用預設的英文模板單字（如 Home, News, About）。
- **全面實相化與「色塊圖標」強制消滅 (Absolute Icon Elimination & Full-Cover Image Cards) -【極度重要】：**
  為了確保視覺豐富度，**必須全面禁止使用任何圖標（Iconography）與純色塊卡片**。
  1. **破壞原色塊佈局：** 發現原網站或設計稿中，有使用「純背景色塊 + 置中小圖標/Emoji」來代表遊戲、活動或分類的卡片佈局時，**絕對禁止照抄這種 HTML 結構**（禁止使用內含 SVG 或 FontAwesome 的純色 div）。
  2. **強制轉換為滿版圖卡 (Full-Cover Image Cards)：** 你必須將這些卡片的結構，強制改寫為「滿版真實圖片作為背景」的卡片（使用 `<img class="w-full h-full object-cover absolute inset-0">`）。而原本卡片上的文字或標籤，請使用絕對定位 (`absolute`) 加上漸層遮罩 (`bg-gradient-to-t`) 疊加在圖片上方。
  3. **世界觀推演與連鎖生圖 (Global Context Deduction)：** 若需自行生圖，**絕對禁止「望文生義」**（如看到 Shop 就畫實體店面），必須根據整個網站的【產業屬性與世界觀】推演。在 HTML 寫完後，你必須立即無條件調用繪圖工具 (`image_gen`)，將原本枯燥的「圖標概念」轉化為真實的、符合世界觀的高畫質場景圖片（例如將「紅色背景+賽車圖標」轉化為「3D 賽車在霓虹賽道奔馳的超高畫質真實場景圖片」）來作為該卡片的滿版背景。

## 【階段三：大量重複元件的智能渲染 (Data-Driven Rendering)】
當單一頁面內有超過 8 個以上的重複性元件時：
1. **禁止硬刻 HTML。**
2. **建立資料集 (Data Array)：** 將真實資料整理為 JavaScript 陣列，放置於 `<script>` 標籤中。
3. **JS 動態生成：** 在 HTML 中保留空容器，透過 JS 迴圈動態渲染出符合原站風格的卡片結構。 