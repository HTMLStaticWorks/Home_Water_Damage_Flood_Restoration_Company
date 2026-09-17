import bs4
with open('index.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')
grid = soup.find('div', class_='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 relative')
if grid:
    children = grid.find_all(recursive=False)
    for i, child in enumerate(children):
        print(f"Child {i+1}: {child.name} - class: {child.get('class')}")
else:
    print("Grid not found")
