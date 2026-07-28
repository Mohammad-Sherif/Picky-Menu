import json
import codecs
import re

def translate_desc(text):
    if not text:
        return text
    
    # Exact phrase translations first
    phrases = {
        "Double Ristretto": "دبل ريستريتو",
        "Double Shot Espresso": "دبل شوت اسبريسو",
        "Double Espresso": "دبل اسبريسو",
        "Microfoam Milk": "رغوة حليب خفيفة",
        "Steamed Milk": "حليب مبخر",
        "Condensed Milk": "حليب مكثف",
        "Hot Water": "ماء ساخن",
        "White Mocha Sauce": "صوص وايت موكا",
        "Mocha Sauce": "صوص موكا",
        "Vanilla Syrup": "سيرب فانيليا",
        "Caramel Drizzle": "صوص كراميل",
        "Caramel Sauce": "صوص كراميل",
        "Matcha Powder": "بودرة ماتشا",
        "Fresh Mint": "نعناع فريش",
        "Sparkling Water": "مياه غازية",
        "Strawberry Puree": "بيوريه فراولة",
        "Mango Puree": "بيوريه مانجو",
        "Ice Cream": "آيس كريم",
        "Whipped Cream": "كريمة مخفوقة",
        "Chocolate Chips": "رقائق شوكولاتة",
        "Brown Sugar": "سكر بني"
    }
    
    ar_text = text
    # Replace phrases ignoring case
    for en_phrase, ar_phrase in phrases.items():
        ar_text = re.sub(re.escape(en_phrase), ar_phrase, ar_text, flags=re.IGNORECASE)
        
    # Word by word translations for anything missed
    words_map = {
        "Espresso": "اسبريسو",
        "Milk": "حليب",
        "Ice": "ثلج",
        "Water": "ماء",
        "Caramel": "كراميل",
        "Vanilla": "فانيليا",
        "Chocolate": "شوكولاتة",
        "Strawberry": "فراولة",
        "Mango": "مانجو",
        "Lemon": "ليمون",
        "Mint": "نعناع",
        "Soda": "صودا",
        "Syrup": "سيرب",
        "Sauce": "صوص",
        "Fresh": "طازج",
        "Sweet": "محلى",
        "Tea": "شاي",
        "Green": "أخضر",
        "Black": "أسود",
        "Boba": "بوبا",
        "Tapioca Pearls": "لآلئ التابيوكا",
        "Pearls": "لآلئ",
        "And": "و"
    }
    
    # Split by non-word chars but keep delimiters to reconstruct
    # A simpler way is to just replace whole words
    for en_word, ar_word in words_map.items():
        # \b doesn't work perfectly if there's already arabic, but we only have English left hopefully
        ar_text = re.sub(r'\b' + re.escape(en_word) + r'\b', ar_word, ar_text, flags=re.IGNORECASE)
    
    # Clean up commas and spaces
    ar_text = ar_text.replace(" ,", "،").replace(",", "،")
    
    return ar_text


with codecs.open('data.js', 'r', 'utf-8') as f:
    content = f.read()

json_str = content.replace('const menuData = ', '').strip()
if json_str.endswith(';'):
    json_str = json_str[:-1]

data = json.loads(json_str)

for item in data['items']:
    # Keep the english description untouched, only translate description_ar
    item['description_ar'] = translate_desc(item['description'])

with codecs.open('data.js', 'w', 'utf-8') as f:
    f.write(f"const menuData = {json.dumps(data, indent=4, ensure_ascii=False)};")

print("Translated descriptions nicely!")
