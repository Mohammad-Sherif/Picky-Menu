import re
import json

file_path = r'C:\Users\Mohammad\.gemini\antigravity\brain\59b2d4a7-d193-4689-b8e8-e2f9d44c3830\.system_generated\steps\4\content.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract Categories
cat_pattern = re.compile(r'<a href="#(category-\d+)"[^>]*>\s*([^<]+)\s*</a>')
categories = cat_pattern.findall(content)
cats = []
for cat_id, cat_name in categories:
    cat_name = cat_name.strip()
    if not any(c['id'] == cat_id for c in cats):
        cats.append({"id": cat_id, "name": cat_name})

menu_items = []

# Split by category sections
sections = re.split(r'<div id="(category-\d+)" class="category-section">', content)

for i in range(1, len(sections), 2):
    cat_id = sections[i]
    section_html = sections[i+1]
    
    # Check if this cat_id is one of our categories
    if not any(c['id'] == cat_id for c in cats):
        continue
    
    # Extract items within this section
    item_blocks = section_html.split('<div class="food-box"')[1:]
    for block in item_blocks:
        block = '<div class="food-box"' + block
        
        # Image
        img_match = re.search(r'<img[^>]*src="([^"]+)"', block)
        img = img_match.group(1) if img_match else ""
        if "lazy.png" in img or img == "":
            img_match2 = re.search(r'data-src="([^"]+)"', block)
            if img_match2:
                img = img_match2.group(1)
        
        # Name
        name_match = re.search(r'<h3>\s*(.*?)\s*</h3>', block, re.DOTALL)
        name = name_match.group(1).strip() if name_match else ""
        name = re.sub(r'<[^>]+>', '', name).strip()
        
        # Description
        desc_match = re.search(r'<div class="food-desc"[^>]*>\s*(.*?)\s*</div>', block, re.DOTALL)
        desc = desc_match.group(1).strip() if desc_match else ""
        desc = re.sub(r'<[^>]+>', '', desc).strip()
        
        # Price
        price_match = re.search(r'<span class="price"[^>]*>\s*(.*?)\s*</span>', block, re.DOTALL)
        price = price_match.group(1).strip() if price_match else ""
        price = re.sub(r'<[^>]+>', '', price).strip()
        
        if name:
            menu_items.append({
                "category_id": cat_id,
                "name": name,
                "description": desc,
                "price": price,
                "image": img
            })

data = {
    "categories": cats,
    "items": menu_items
}

with open(r'C:\Users\Mohammad\Documents\antigravity\gallant-darwin\data.js', 'w', encoding='utf-8') as f:
    f.write(f"const menuData = {json.dumps(data, indent=4, ensure_ascii=False)};")

print(f"Extracted {len(cats)} categories and {len(menu_items)} items.")
