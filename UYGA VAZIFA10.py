while True:
    rang = input("Svetofor qaysi rangda? ").lower()
    if rang in ['qizil', 'sariq', 'yashil']:
        print("rahmat, to'g'ri keladi")
        break
    else:
        print("bu xato rang, qayta so'rang")

import random

tasodifiy_son = random.randint(1,10)
taxmin = 0

while taxmin != tasodifiy_son:
    taxmin = int(input("1 dan 10 gacha son kiriting: "))
    if taxmin != tasodifiy_son:
        print("Noto'g'ri, qayta urinib ko'ring")
    else:
        print("Tabriklaymiz, siz topdingiz!")

do_stlar = []
ismlar = ""

while ismlar != 'stop':
    ismlar = input("Do'stingizning ismini kiriting (to'xtash uchun 'stop' deb yozing): ").lower()
    if ismlar != 'stop':
        do_stlar.append(ismlar.capitalize())

print("Sizning do'stlaringiz ro'yxati:", do_stlar)

kurs = 12600
summa = ""

while summa != 'exit':
    summa = input("Summani kiriting (chiqish uchun 'exit' deb yozing): ").lower()
    
    if summa != 'exit':
        try:
            so_m = float(summa)
            dollar = so_m / kurs
            print(f"{so_m} so'm = {dollar:.2f} USD")
        except ValueError:
            print("Iltimos, faqat son kiriting yoki 'exit' deb yozing.")

print("Dastur tugadi.")
