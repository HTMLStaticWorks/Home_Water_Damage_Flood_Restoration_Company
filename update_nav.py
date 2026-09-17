import os, glob, re

root_dir = r'c:\Users\Shalani A\Documents\Shalan\Client Projects(September)\Home_Water_Damage_Flood_Restoration_Company'

files = [os.path.join(root_dir, 'index.html')] + glob.glob(os.path.join(root_dir, 'pages', '*.html'))

def get_nav_items(is_index):
    prefix = 'pages/' if is_index else ''
    home_path = 'index.html' if is_index else '../index.html'
    return [
        ('Home', home_path),
        ('Home 2', prefix + 'home-2.html' if is_index else 'home-2.html'),
        ('About', prefix + 'about.html' if is_index else 'about.html'),
        ('Services', prefix + 'services.html' if is_index else 'services.html'),
        ('Insurance', prefix + 'insurance.html' if is_index else 'insurance.html'),
        ('Contact', prefix + 'contact.html' if is_index else 'contact.html'),
        ('Dashboard', prefix + 'dashboard.html' if is_index else 'dashboard.html'),
    ]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    fname = os.path.basename(fpath)
    is_index = fname == 'index.html'
    
    items = get_nav_items(is_index)
    
    # Desktop Nav
    desktop_nav = '<nav class="hidden xl:flex items-center gap-2">\n'
    for label, url in items:
        # Determine if this item is active
        # The logic: if the url is a basename (like about.html), check against fname.
        # if the url is index.html or ../index.html, check if fname is index.html
        if url.endswith(fname):
            active = True
        elif url == '../index.html' and fname == 'index.html': # Should not happen
            active = True
        else:
            active = False
            
        if active:
            cls = 'bg-primary-50 dark:bg-primary-900/20 text-primary-600 px-4 py-2 rounded-lg font-medium transition-colors'
        else:
            cls = 'px-4 py-2 text-gray-600 dark:text-gray-300 font-medium transition-colors hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg hover:text-primary-600 dark:hover:text-primary-400'
        
        desktop_nav += f'                    <a href="{url}" class="{cls}">{label}</a>\n'
    desktop_nav += '                </nav>'

    # Mobile Nav
    mobile_nav = ''
    for label, url in items:
        if url.endswith(fname):
            cls = 'block px-3 py-3 text-primary-600 font-medium bg-primary-50 dark:bg-primary-900/20 rounded-lg'
        else:
            cls = 'block px-3 py-3 text-gray-600 dark:text-gray-300 font-medium rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800'
        mobile_nav += f'                <a href="{url}" class="{cls}">{label}</a>\n'

    # Replace desktop nav
    content = re.sub(r'<nav class="hidden xl:flex items-center gap-8">.*?</nav>', desktop_nav, content, flags=re.DOTALL)
    
    # Replace mobile nav
    content = re.sub(r'(<div class="px-4 pt-2 pb-6 space-y-1 shadow-xl">\s*)\n.*?(<!-- Mobile Utility Row)', r'\1\n' + mobile_nav + r'\n                \2', content, flags=re.DOTALL)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Updated {fname}')
