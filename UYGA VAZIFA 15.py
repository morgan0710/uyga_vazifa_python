        
faylnomi = 'matn.txt'
with open(faylnomi, 'r') as fayl:
    matn = fayl.read()

print(matn)

with open('pi_million_digits.txt', 'r') as fayl:
    pi = fayl.read()

pi = pi.replace('.', '').replace('\n', '')

sana = "12072010"

if sana in pi:
    print('matnda uchraydi')
else:
    print('matnda yo`q')