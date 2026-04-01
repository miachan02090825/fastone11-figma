const fs = require('fs');

const pHTML = fs.readFileSync('player-information.html', 'utf8');
const cHTML = fs.readFileSync('character.html', 'utf8');

// 1. Extract HTML
const uiMatch = pHTML.match(/<!-- Mobile-first App Container.*?>([\s\S]*?)<!-- Tab Switching Logic -->/);
if(!uiMatch) {
    console.error("UI match failed");
    process.exit(1);
}
const uiHTML = uiMatch[1];

// 2. Extract Scripts/Styles
const jsMatch = pHTML.match(/<!-- Tab Switching Logic -->([\s\S]*?)<\/body>/);
const jsCSS = jsMatch ? jsMatch[1].trim() : "";

// 3. Prepare replacement right panel
let newRight = `<!-- ====== RIGHT PANEL (Details / Gacha / Skins / Stats) ====== -->
        <div class="hidden lg:flex w-[390px] xl:w-[410px] flex-col bg-[#1b1d42] border-l border-white/5 shadow-2xl flex-shrink-0 relative overflow-hidden h-[calc(100vh-60px)]">
          ${uiHTML}
        </div>`;

newRight = newRight.replace(/max-w-\[390px\]/g, '');
newRight = newRight.replace(/rounded-\[24px\]/g, '');
newRight = newRight.replace(/shadow-\[0_20px_50px_rgba\(0,0,0,0\.5\)\]/g, '');
newRight = newRight.replace(/h-\[844px\]/g, 'h-full');
newRight = newRight.replace(/<!-- Back \/ Close Button[\s\S]*?<\/a>/, '');

// 4. Replace in character.html
const startTag = '<!-- ====== RIGHT PANEL (Details / Gacha / Skins / Stats) ====== -->';
const endTag = '</div><!-- /content -->';

const startIndex = cHTML.indexOf(startTag);
const endIndex = cHTML.lastIndexOf(endTag);

if (startIndex === -1 || endIndex === -1) {
    console.error("Right panel markers not found in character.html", startIndex, endIndex);
    process.exit(1);
}

let cNew = cHTML.substring(0, startIndex) + newRight + "\n\n      " + cHTML.substring(endIndex);

// 5. Append JS/CSS
if (!cNew.includes('function switchTab')) {
    cNew = cNew.replace('</body>', jsCSS + '\n</body>');
}

fs.writeFileSync('character.html', cNew, 'utf8');
console.log("Success Node.js replacement!");
