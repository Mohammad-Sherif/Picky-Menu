import json
import codecs
import re

def elegant_translate(text):
    if not text:
        return text
    
    # Exact matches for common items
    exact_matches = {
        "Flat White": "فلات وايت",
        "Cappuccino": "كابوتشينو",
        "Latte": "لاتيه",
        "Spanish Latte": "سبانيش لاتيه",
        "Mocha": "موكا",
        "White Mocha": "وايت موكا",
        "Cortado": "كورتادو",
        "Americano": "أمريكانو",
        "Espresso": "اسبريسو",
        "Double Espresso": "دبل اسبريسو",
        "Iced Latte": "آيس لاتيه",
        "Iced Spanish Latte": "آيس سبانيش لاتيه",
        "Iced Caramel Macchiato": "آيس كراميل ميكياتو",
        "Matcha": "ماتشا",
        "Matcha Latte": "ماتشا لاتيه"
    }
    
    if text in exact_matches:
        return exact_matches[text]
    
    # Word by word replacement for others
    replacements = {
        "Iced": "آيس",
        "Hot": "ساخن",
        "Caramel": "كراميل",
        "Vanilla": "فانيليا",
        "Hazelnut": "بندق",
        "Pistachio": "فستق",
        "Lotus": "لوتس",
        "Oreo": "أوريو",
        "Chocolate": "شوكولاتة",
        "Macchiato": "ميكياتو",
        "Frappe": "فرابيه",
        "Boba": "بوبا",
        "Signature": "سجنتشر",
        "Refresher": "ريفريشر",
        "Milk Tea": "شاي بحليب",
        "Fruit Tea": "شاي فواكه",
        "Passion Fruit": "باشن فروت",
        "Peach": "خوخ",
        "Watermelon": "بطيخ",
        "Strawberry": "فراولة",
        "Blueberry": "توت أزرق",
        "Berry": "توت",
        "Mango": "مانجو",
        "Lemon": "ليمون",
        "Mint": "نعناع",
        "Mojito": "موهيتو",
        "Milkshake": "ميلك شيك",
        "Fresh Juice": "عصير فريش",
        "Orange": "برتقال",
        "Tea": "شاي",
        "Green Tea": "شاي أخضر",
        "Mocha": "موكا",
        "White": "وايت",
        "Dark": "دارك",
        "Latte": "لاتيه",
        "Espresso": "اسبريسو",
        "Apple": "تفاح",
        "Pineapple": "أناناس",
        "Kiwi": "كيوي",
        "Pomegranate": "رمان",
        "Classic": "كلاسيك",
        "Mix": "ميكس"
    }
    
    words = text.split()
    translated_words = []
    for w in words:
        # Check ignoring case
        match = None
        for k, v in replacements.items():
            if w.lower() == k.lower():
                match = v
                break
        if match:
            translated_words.append(match)
        else:
            translated_words.append(w)
            
    # Reorder some adjectives in Arabic (e.g., Iced Latte -> آيس لاتيه is fine, but Strawberry Milkshake -> ميلك شيك فراولة)
    ar_text = " ".join(translated_words)
    ar_text = ar_text.replace("ميلك شيك فراولة", "ميلك شيك فراولة") # Already fine if we just translate words for most cafe drinks
    
    # Specific reorders
    ar_text = re.sub(r'فراولة (موهيتو|ميلك شيك|فرابيه)', r'\1 فراولة', ar_text)
    ar_text = re.sub(r'مانجو (موهيتو|ميلك شيك|فرابيه|عصير فريش)', r'\1 مانجو', ar_text)
    ar_text = re.sub(r'لوتس (فرابيه|ميلك شيك)', r'\1 لوتس', ar_text)
    ar_text = re.sub(r'كراميل (فرابيه|ميكياتو)', r'\1 كراميل', ar_text)
    ar_text = re.sub(r'آيس (.*)', r'آيس \1', ar_text) # Iced stays at the beginning usually in cafe lingo
    
    return ar_text


with codecs.open('data.js', 'r', 'utf-8') as f:
    content = f.read()

json_str = content.replace('const menuData = ', '').strip()
if json_str.endswith(';'):
    json_str = json_str[:-1]

data = json.loads(json_str)

for item in data['items']:
    item['name_ar'] = elegant_translate(item['name'])

with codecs.open('data.js', 'w', 'utf-8') as f:
    f.write(f"const menuData = {json.dumps(data, indent=4, ensure_ascii=False)};")

print("Translated names nicely!")
