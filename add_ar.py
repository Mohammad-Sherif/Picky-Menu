import json
import codecs

# Read data.js
with codecs.open('data.js', 'r', 'utf-8') as f:
    content = f.read()

# Extract json
json_str = content.replace('const menuData = ', '').strip()
if json_str.endswith(';'):
    json_str = json_str[:-1]

data = json.loads(json_str)

# Common category translations
cat_trans = {
    "Espresso Bar (Hot)": "اسبريسو بار (ساخن)",
    "Iced Coffee": "قهوة مثلجة",
    "Refresher Boba": "ريفرشر بوبا",
    "Signature Boba": "سجنتشر بوبا",
    "Boba - Fruit Tea": "بوبا - شاي فواكه",
    "Boba - Milk Tea": "بوبا - شاي حليب",
    "Matcha": "ماتشا",
    "Mojito": "موهيتو",
    "Frappe": "فرابيه",
    "Milkshakes": "ميلك شيك",
    "Fresh Juice": "عصير فريش",
    "Smoothies": "سموذي",
    "Non-Coffee Hot": "مشروبات ساخنة (بدون قهوة)",
    "Soft Drinks": "مشروبات غازية",
    "Add-ons": "إضافات"
}

for cat in data['categories']:
    cat['name_ar'] = cat_trans.get(cat['name'], cat['name'])

for item in data['items']:
    item['name_ar'] = item['name']
    item['description_ar'] = item['description']

with codecs.open('data.js', 'w', 'utf-8') as f:
    f.write(f"const menuData = {json.dumps(data, indent=4, ensure_ascii=False)};")

print("Added ar fields to data.js")
