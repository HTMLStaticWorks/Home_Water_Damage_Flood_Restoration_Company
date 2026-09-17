import os, glob

root_dir = r'c:\Users\Shalani A\Documents\Shalan\Client Projects(September)\Home_Water_Damage_Flood_Restoration_Company'
files = [os.path.join(root_dir, 'index.html')] + glob.glob(os.path.join(root_dir, 'pages', '*.html'))

old_span = '<span class="text-sm">Sign Up</span>'
new_span = '<span class="text-sm whitespace-nowrap">Sign Up</span>'

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(old_span, new_span)
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(fpath)}")
