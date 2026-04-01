import re

with open('player-information.html', 'r', encoding='utf-8') as f:
    p_content = f.read()

with open('character.html', 'r', encoding='utf-8') as f:
    c_content = f.read()

# Extract the modal content
match_ui = re.search(r'<!-- Mobile-first App Container.*?>(.*?)<!-- Tab Switching Logic -->', p_content, re.DOTALL)
if match_ui:
    ui_html = match_ui.group(1)
    
# Extract JS/CSS
match_js = re.search(r'<!-- Tab Switching Logic -->(.*?)</body>', p_content, re.DOTALL)
js_css = match_js.group(1).strip() if match_js else ""

# Prepare new right panel:
new_right = f'''<!-- ====== RIGHT PANEL ====== -->
        <div class="hidden lg:flex w-[390px] flex-col bg-[#1b1d42] border-l border-white/5 shadow-2xl flex-shrink-0 relative overflow-hidden h-[calc(100vh-60px)]">
          {ui_html}
        </div>'''

# Clean up classes on inner containers
new_right = new_right.replace('max-w-[390px]', '')
new_right = new_right.replace('rounded-[24px]', '')
new_right = new_right.replace('shadow-[0_20px_50px_rgba(0,0,0,0.5)]', '')
new_right = new_right.replace('h-[844px]', 'h-full')

# Remove the back button (since it is a sidebar now)
new_right = re.sub(r'<!-- Back / Close Button.*?</a>', '', new_right, flags=re.DOTALL)

# Locate the right panel in character.html and replace it
# From <!-- ====== RIGHT PANEL (Details / Gacha / Skins / Stats) ====== -->
# to </div><!-- /content -->
pattern = r'<!-- ====== RIGHT PANEL \(Details / Gacha / Skins / Stats\) ====== -->.*?</div>\s*</div><!-- /content -->'
replacement = new_right + '\n\n      </div><!-- /content -->'
c_new = re.sub(pattern, replacement, c_content, flags=re.DOTALL)

# Also append JS/CSS
if 'function switchTab' not in c_new:
    c_new = c_new.replace('</body>', js_css + '\n</body>')

with open('character.html', 'w', encoding='utf-8') as f:
    f.write(c_new)

print('Success!')
