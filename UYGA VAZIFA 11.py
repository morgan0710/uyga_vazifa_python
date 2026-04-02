def mijoz_malumotlari(ism, familiya, tugilgan_yil, tugilgan_joy, email=None, tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {
        'ism': ism,
        'familiya': familiya,
        'yosh': 2024 - tugilgan_yil,
        'tugilgan_joy': tugilgan_joy,
        'email': email,
        'telefon': tel
    }
    return mijoz

print(mijoz_malumotlari("Ali", "Valiyev", 1995, "Toshkent", email="ali@mail.com"))

mijozlar = []
while True:
    print("\nMijoz ma'lumotlarini kiriting:")
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    t_yil = int(input("Tug'ilgan yili: "))
    t_joy = input("Tug'ilgan joyi: ")
    email = input("Email (ixtiyoriy): ")
    tel = input("Telefon (ixtiyoriy): ")
    
    mijozlar.append(mijoz_malumotlari(ism, familiya, t_yil, t_joy, email, tel))
       
    javob = input("Yana mijoz qo'shasizmi? (ha/yo'q): ")
    if javob.lower() != 'ha':
        break

print("\nRo'yxatdagi mijozlar:")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}, "
          f"{mijoz['yosh']} yoshda, tel: {mijoz['telefon']}")

def kattasini_top(x, y, z):
    """Uchta sondan eng kattasini qaytaruvchi funksiya"""
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z

print(f"Eng katta son: {kattasini_top(15, 28, 10)}")

def aylana_malumotlari(radius, pi=3.14159):
    """Aylana haqidagi ma'lumotlarni hisoblovchi funksiya"""
    aylana = {
        'radius': radius,
        'diametr': 2 * radius,
        'perimetr': 2 * pi * radius,
        'yuzi': pi * (radius ** 2)
    }
    return aylana

print(aylana_malumotlari(5))

def tub_sonlar_top(min_son, max_son):
    """Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya"""
    tub_sonlar = []
    for n in range(min_son, max_son + 1):
        if n < 2:
            continue
        tub = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                tub = False
                break
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar

print(f"Tub sonlar: {tub_sonlar_top(1, 20)}")

def fibonachchi_chiqar(n):
    """N ta Fibonachchi sonidan iborat ro'yxat qaytaruvchi funksiya"""
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1] + sonlar[x-2])
    return sonlar

# Sinab ko'rish:
miqdor = int(input("Nechta Fibonachchi soni kerak? "))
print(fibonachchi_chiqar(miqdor))
