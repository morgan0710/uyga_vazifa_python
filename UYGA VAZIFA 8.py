python = {
    "Boolean": "Mantiqiy qiymat (True yoki False)",
    "Float": "O'nlik son (haqiqiy sonlar)",
    "For": "Biror amalni qayta-qayta bajarish tsikli",
    "If": "Shartlarni tekshirish operatori",
    "Integer": "Butun son",
    "String": "Matnli ma'lumot turi",
    "List": "Tartiblangan elementlar ro'yxati",
    "Dictionary": "Kalit-qiymat juftligidan iborat to'plam",
    "Tuple": "O'zgarmas elementlar ro'yxati",
    "Variable": "Ma'lumotlarni saqlash uchun ajratilgan nom (o'zgaruvchi)"
}
for kalit in sorted(python.keys()):
    print(f"{kalit} - {python[kalit]}")

# Davlatlar va poytaxtlar lug'atini tuzamiz
davlatlar = {
    "AQSH": "Washington D.C.",
    "Italiya": "Rim",
    "Malayziya": "Kuala-Lumpur",
    "O'zbekiston": "Toshkent",
    "Qirg'iziston": "Bishkek",
    "Qozog'iston": "Nursulton",
    "Rossiya": "Moskva",
    "Singapur": "Singapur",
    "Tojikiston": "Dushanbe"
}

for davlat in sorted(davlatlar.keys()):
    print(davlat)

print("-" * 20)

for poytaxt in sorted(davlatlar.values()):
    print(poytaxt)

davlatlar = {
    "O'zbekiston": "Toshkent",
    "AQSh": "Washington D.C.",
    "Rossiya": "Moskva",
    "Germaniya": "Berlin",
    "Yaponiya": "Tokio",
    "Italiya": "Rim"
}

txt = input("Qaysi davlatning poytaxtini bilishni istaysiz?: ").lower()
tx = davlatlar.get(txt)

if tx:
    print(f"{txt}ning poytaxti {tx} shahri")
else:
    print("Kechirasiz, bizda bu haqida ma'lumot yo'q")

menu = {
    "osh": 20000,
    "non": 4000,
    "shashlik": 15000,
    "somsa": 6000,
    "lag'mon": 18000,
    "sho'rva": 16000,
    "manti": 12000,
    "choy": 3000,
    "salat": 5000,
    "muzqaymoq": 10000
}

print("3 ta taom buyurtma bering.")
buyurtmalar = []

for i in range(3):
    taom = input(f"{i+1}-taom: ").lower()
    buyurtmalar.append(taom)

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.capitalize()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")
