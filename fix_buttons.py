import os, glob

root_dir = r'c:\Users\Shalani A\Documents\Shalan\Client Projects(September)\Home_Water_Damage_Flood_Restoration_Company'
files = [os.path.join(root_dir, 'index.html')] + glob.glob(os.path.join(root_dir, 'pages', '*.html'))

old_class = 'class="p-2 rounded-full text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"'
new_class = 'class="w-10 h-10 flex flex-shrink-0 items-center justify-center border-2 border-secondary-900 dark:border-white rounded-full text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"'

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We only want to replace this class for themeToggle and rtlToggle buttons.
    # The simplest is to just replace the exact string since it's only used for these two buttons in the header
    new_content = content.replace(old_class, new_class)
    
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(fpath)}")
