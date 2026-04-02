
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
