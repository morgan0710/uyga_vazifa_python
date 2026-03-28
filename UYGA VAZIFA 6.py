pochtalar = ['user1@gmail.com', 'user2yahoo.com', 'user3@outlook.com']
for email in pochtalar:
    if '@' not in email:
        print(f'Noto`g`ri email: {email}')

parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]

for parol in parollar:
    if len(parol) < 8:
        print(f"{parol} - Juda qisqa")
    elif parol.isalnum() and parol.isalpha():
        print(f"{parol} - Kuchsiz parol")
    else:
        print(f"{parol} - Kuchli parol")

haroratlar = [20, 22, 19, 24, 25, 23, 21]
ortacha = sum(haroratlar) / len(haroratlar)
print(f"Haftalik o'rtacha harorat: {ortacha:.1f}")
for harorat in haroratlar:
    if harorat >= 22:
        print(f'{harorat} °c Iliq kun')
    else:
        print(f'{harorat} °c Salqin kun')

taomlar = ["Osh", "Shashlik", "Manti", "Lag'mon"]
buyurtma = input("Nima buyurasiz? ").capitalize()
found = False
for taom in taomlar:
    if taom == buyurtma:
        found = True
        break
if found:
    print("Buyurtmangiz qabul qilindi")
else:
    print("Kechirasiz, bunday taom yo'q")
