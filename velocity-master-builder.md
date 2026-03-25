---
name: velocity-master-builder
description: VELOCITY X 網站的「全局通用建站規範」。強制鎖死全站的 Navbar、Footer、深色背景、Tailwind 設定與賽車風格特效，確保所有生成的 HTML 頁面擁有 100% 的視覺一致性。
---

# VELOCITY X 全局頁面建置規範 (Master Builder)

當使用者要求建立「任何 VELOCITY X 的網頁」時，請嚴格遵守以下佈局與視覺規範，並直接輸出完整的 HTML 程式碼。

- ## 1. 核心環境與動態導覽列 (Core Environment & Dynamic Navbar)
  所有生成的頁面，必須具備以下固定不變的風格，但內容需根據目標網址動態生成：
  
  - **Head 與 Body 設定**：(保留你的 Outfit, Teko 字體與 Tailwind Config 變數設定，Body 使用 bg-v-dark 等設定)。
  - **動態導覽列 (Dynamic Navbar) 渲染規則：**
    必須保留 VELOCITY X 的傾斜 V 字 Logo 與深色半透明背景 (`backdrop-blur-md bg-v-dark/80 border-b border-white/5`)。
    **針對選單內容：** 請讀取【階段一】盤點出的「選單樹狀圖」，並嚴格使用 Tailwind 的 `group` 和 `group-hover` 轉換為賽車風格的下拉選單。
    
    **下拉選單 (Dropdown) 強制 HTML 結構：**
    ```html
    <div class="relative group inline-block">
        <button class="px-3 py-2 text-sm font-semibold tracking-wider uppercase text-white group-hover:text-v-red transition-colors">
            [動態填入主選單名稱]
        </button>
        <div class="absolute left-0 mt-0 hidden group-hover:block w-48 bg-v-gray border border-v-red/30 shadow-neon-red z-50">
            <a href="#" class="block px-4 py-3 text-sm text-gray-300 hover:bg-v-red hover:text-white transition-all">[動態填入次選單 1]</a>
            <a href="#" class="block px-4 py-3 text-sm text-gray-300 hover:bg-v-red hover:text-white transition-all">[動態填入次選單 2]</a>
        </div>
    </div>

## 2. 通用 UI 元件規範 (Component System)
在頁面的「動態內容區塊」中，無論生成什麼內容，只要遇到以下元素，必須套用指定樣式：
- **大標題 (Headings)**：必須使用 `font-speed font-black italic tracking-tighter uppercase`，並適度搭配 `text-transparent bg-clip-text bg-gradient-to-r from-white to-gray-400` 或 `text-white`。
- **標題裝飾線**：區塊標題旁可加上 `<span class="w-2 h-12 bg-v-red inline-block transform skew-x-[-15deg]"></span>`。
- **主要按鈕 (Primary CTA)**：必須呼叫 `style.css` 的斜角按鈕。
  結構：`<button class="action-btn text-white bg-v-red px-8 py-2.5 font-bold tracking-widest uppercase hover:bg-v-red-glow transition-all"><span class="btn-text">按鈕文字</span></button>`。
- **次要按鈕 (Secondary CTA)**：使用邊框樣式 `border border-v-red text-v-red hover:bg-v-red hover:text-white`，同樣保持直角或微小圓角。
- **通用卡片 (Cards)**：背景使用 `bg-v-gray`，邊框 `border-white/5`。懸停時必須觸發 `hover:border-v-red/50 hover:shadow-neon-red transition-all duration-300` 與 `hover:-translate-y-1`。

## 3. 動態內容區塊處理 (Content Injection)
- **頁首 (Subpage Hero)**：除非使用者特別要求全螢幕，否則二級頁首高度設定為 `py-16` 到 `py-24`。背景預設使用 `bg-v-dark` 搭配 `.abstract-pattern` 類別，或深色漸層 `bg-gradient-to-b from-v-gray to-v-dark`。
- **內文排版**：一般段落文字請使用 `font-sans` (Outfit 字體)，顏色使用 `text-gray-400`，行高設定為 `leading-relaxed`。

## 4. 嚴格禁止行為 (Anti-Patterns)
- **禁止**使用標準圓角 (`rounded-lg`, `rounded-xl`, `rounded-full`) 於卡片或內容區塊。VELOCITY X 的風格是尖銳、具速度感的，請使用直角 (`rounded-none`) 或極小圓角 (`rounded-sm`)。
- **禁止**使用預設字體、Inter 或 Arial。數字與大標題強制使用 `font-speed` (Teko)。
- **禁止**使用藍色、綠色、紫色等非品牌色漸層。全站高光與強調色僅限於 `v-red` (#E3001B) 與白色。 



- ## 5. 網址內容轉換與防偷懶規範 (Zero Omissions & Anti-Hallucination)
  當使用者提供一個目標網址 (URL) 要求進行風格轉換時，必須嚴格遵守「1:1 完整映射」原則：
  - **禁止無中生有 (No Hallucination)：** 絕對不允許自行發明原網址沒有的假字、假選單或假產品。
  - **零刪減，禁止偷懶 (Zero Omissions) - 極度重要：** 原網址有多少個區塊、多少張卡片、多少段文字，就必須 **100% 完整對應生成**。絕對不允許擅自省略、縮短內文，也「絕對禁止」在程式碼中使用 `` 或 `...` 帶過。
  - **結構對應 (Mapping)：** - 原網站的每一段敘述 (Paragraphs) 都要無損填入 VELOCITY X 的字體規範中。
    - 原網站的每一個列表項目或網格卡片，都必須一個不漏地轉換為 VELOCITY X 的卡片結構。 

## 6 . 圖片視覺 DNA 與生成規範 (Image Visual DNA & Generation Strategy)
為了確保全站圖片與「賽車暗黑風格」100% 契合，無論是抄圖或生圖，必須遵循以下視覺規範：

- **核心視覺風格：** Cinematic（電影感）、High-Contrast（高對比）、Dynamic Motion（動態感）。
- **光影與色彩：** 以深色為主調，強調「霓虹紅光 (#E3001B)」的反射與點綴。背景應有適度的 Motion Blur（動態模糊）或 Cyberpunk（賽博龐克）城市的流光。
- **生圖模式 (AI Generation)：** 若原網站無合適圖片，必須根據內文撰寫極為具體的圖片生成 Prompt。Prompt 必須包含：`[內文核心內容]` + `dark cyberpunk environment` + `red neon lighting streaks` + `motion blur` + `ultra-realistic, cinematic, 8k resolution, Unreal Engine 5 render`。
- **抄圖模式 (Image Scraping)：** 盡可能保留原網站圖片的真實內容（如遊戲角色），但在 HTML 中必須為該圖片加上 `filter: brightness(0.8) contrast(1.2)` 等 CSS 特效，使其融入暗黑風格，絕對禁止直接貼上亮白底色的原始圖片。