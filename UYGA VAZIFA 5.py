foydalanuvchilar = ['ali', 'behruz', 'mirzo', 'bekzod', 'boboxon']
yangi_login = input('Yangi login tanlang: ')
if yangi_login in foydalanuvchilar:
    print('Login band, yangi login tanlang!')
else:
    print(f'Xush kelibsiz!')

son = int(input("Istalgan butun son kiriting: "))
for i in range(2, 11):
    if son % i == 0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")

son = int(input('Juft son kiriting: '))
if son % 2 == 0:
   print("Rahmat!")
else:
   print("Bu son juft emas.")

yosh = int(input('Yoshingizni kiriting: '))
if yosh <= 4 or yosh >= 60:
   pul = 0
elif yosh <= 18:
   pul = 10000
else:
   pul = 20000

if pul == 0:
   print('Kirish bepul')
else:
   print(f'Kirish {pul} so`m ')

son1 = float(input('Birinchi sonni kiriting: '))
son2 = float(input('Ikkinchi sonni kiriting: '))
if son1 < son2:
   print(f'{son1} < {son2}')
elif son1 > son2:
   print(f'{son1} > {son2}')
else:
   print(f'{son1} = {son2}')