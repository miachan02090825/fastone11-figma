---
name: velocity-url-converter
description: 專門用於將外部網址 (URL) 內容無損轉換為 VELOCITY X 賽車暗黑風格的自動化工作流。內建「強制內容盤點」、「選單樹狀圖提取」與「防偷懶機制」，確保零幻覺、零刪減。
---

# 外部網址轉換工作流 (URL to VELOCITY X)

當使用者提供一個目標網址 (URL) 並要求轉換風格時，請嚴格按照以下三個階段執行。**絕對不可跳過階段一直接寫程式碼。**

## 【階段一：通用內容盤點與選單樹狀圖 (Universal Content Inventory & Menu Tree)】
在撰寫 HTML 前，請先讀取目標網址，並在對話中以條列方式輸出以下盤點報告：

**1. 導覽列層級 (Navbar Menu Tree)：**
請掃描原網址的頂部導覽列，並精準畫出選單的樹狀結構（包含所有隱藏的下拉式次選單）。
*範例格式：*
- 主選單 A
  - 次選單 A-1
  - 次選單 A-2
- 主選單 B (無次選單)

**2. 內容區塊盤點 (Content Blocks)：**
請將原網址的主體內容拆解為區塊，並計算數量。
*範例格式：*
- Hero 區塊：1 個 (標題: XXX)
- 特色/服務卡片：共 X 張
- 最新消息/公告清單：共 X 條

**3. 微小狀態與圖片盤點 (Micro-Copy & Images) - 極度重要：**
- 狀態文字：強制捕捉活動時間、得獎名單公佈狀態（如「待公布」）、注意事項等微小字體。
- 圖片來源：記錄每張圖片的用途與絕對網址 (URL)，若無則簡短描述其內容。

**4. 全域雜訊過濾 (Global Noise Filtering)：**
請自動過濾掉不屬於網頁主體的雜訊，例如：Cookie 同意橫幅 (Cookie Banners)、浮動廣告 (Floating Ads)、回到頂部按鈕等。

*⚠️ 警告：這是一個強制的思考鏈過程，你必須先印出這份盤點清單（特別是完整的選單樹狀圖），確認無誤後才能進入階段二。*

## 【階段二：1:1 完整程式碼生成與圖片實作 (Full HTML & Image Implementation)】
完成盤點後，請根據 `@velocity-master-builder.md` 的視覺規範寫成 HTML。
必須遵守以下原則：
- **動態導覽列 (Dynamic Navbar)：** 將盤點到的「選單樹狀圖」套用至 Tailwind `group-hover` 下拉選單結構中，完美實作賽車風格 Navbar。
- **零刪減 (Zero Omissions)：** 階段一盤點到的所有內容、卡片、狀態文字，必須一個不漏地寫入 HTML。絕對禁止使用 `` 或 `...` 敷衍。
- **零幻覺 (No Hallucination)：** 只准使用盤點到的真實文字與數據。
- **圖片處理 (Image Strategy)：** 優先使用抓取到的真實圖片 URL，並加上 `brightness-90 contrast-110` 等暗黑濾鏡。若原站無圖，請在 HTML 註解中撰寫具體的生圖 Prompt。

## 【階段三：大量重複元件的智能渲染 (Data-Driven Rendering)】
當盤點到數量龐大的重複性元件（例如超過 8 個以上的遊戲卡片、新聞清單）時，為避免超出字數限制導致斷尾：
1. **禁止硬刻 HTML：** 絕對不允許在 HTML 中重複撰寫數十次相同的卡片結構。
2. **建立資料集 (Data Array)：** 將所有真實資料整理為 JavaScript 陣列 (Array of Objects)，並放置於頁面底部的 `<script>` 標籤中。
3. **JS 動態生成：** 在 HTML 中保留一個空容器（如 `<div id="games-grid"></div>`），透過簡短的 JS 迴圈將資料動態渲染為 VELOCITY X 的卡片結構。 