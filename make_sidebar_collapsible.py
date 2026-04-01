import os, re

new_css = """
  <style>
    /* Collapsible Sidebar System */
    :root { --sidebar-w: 188px; }
    body.sidebar-collapsed { --sidebar-w: 72px; }
    @media (max-width: 1023px) {
        :root { --sidebar-w: 0px; }
        body.sidebar-collapsed { --sidebar-w: 0px; }
    }
    #sidebar { width: var(--sidebar-w) !important; transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
    main { margin-left: var(--sidebar-w) !important; transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
    
    body.sidebar-collapsed .nav-text { opacity: 0; pointer-events: none; width: 0; overflow: hidden; display: none; }
    body.sidebar-collapsed .sidebar-banners-area { display: none; }
    body.sidebar-collapsed .sidebar-link { justify-content: center !important; padding-left: 0 !important; padding-right: 0 !important; }
    body.sidebar-collapsed .sidebar-link .nav-icon { margin-right: 0 !important; }
    body.sidebar-collapsed .sidebar-logo-area { justify-content: center !important; padding-left: 0 !important; padding-right: 0 !important; }
  </style>
"""

files = ['index.html', 'game-info.html', 'character.html', 'shop.html']

for fn in files:
    if not os.path.exists(fn): continue
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject CSS if not there
    if "/* Collapsible Sidebar System */" not in content:
        content = content.replace("</head>", new_css + "</head>")
        
    # 2. Add toggle logic to the top left button (game_other_btn_n.png)
    # Finding the button that contains this image and adding onclick
    button_regex = r'(<button[^>]*?)>'
    # We want to specifically target the button around game_other_btn_n.png
    # But since it's hard to target without risking others, we'll replace the exact block structure in aside:
    content = content.replace(
        '<button class="w-[32px] h-[32px] hover:brightness-125 transition focus:outline-none flex-shrink-0">',
        '<button class="w-[32px] h-[32px] hover:brightness-125 transition focus:outline-none flex-shrink-0" onclick="document.body.classList.toggle(\\\'sidebar-collapsed\\\')">'
    )
    # For safety, remove any double escaping Python might have done
    content = content.replace("\\'", "'")
    
    # Also add the sidebar-logo-area class to the header row so padding can be adjusted via CSS
    content = content.replace(
        '<div class="flex items-center gap-2 px-4 pt-4 pb-3 border-b border-indigo-500/20">',
        '<div class="sidebar-logo-area flex items-center gap-2 px-4 pt-4 pb-3 border-b border-indigo-500/20">'
    )

    # 3. Modify spanning text in navigation to have .nav-text class
    # The links look like: ...<img src="..." alt="" class="nav-icon"><span>Home</span></a>
    content = re.sub(r'(<img[^>]*class="nav-icon[^>]*>)\s*<span(?: class="[^"]*")?>(.*?)</span>', r'\1<span class="nav-text">\2</span>', content)

    # 4. Modify the bottom banners div to hide it
    content = content.replace(
        '<div class="px-2 pb-4 space-y-2">',
        '<div class="px-2 pb-4 space-y-2 sidebar-banners-area">'
    )

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)

print("Collapse functionality injected!")
