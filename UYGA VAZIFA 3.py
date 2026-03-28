ism = ('Behruz', 'Akmal', 'Bekzod')
print(ism[0], 'bugun o`ynisanmi')
print(ism[1], 'ertang o`ynisanmi')
print(ism[2], 'o`ynisanmi')

sonlar = [10, 5, 2.5, 100]
sonlar[0] = sonlar[0] + sonlar[1]
sonlar[1] = 3.14
sonlar[2] = sonlar[2] / 2
print(sonlar)

t_shaxslar = ['Jaloliddin Manguberdi', 'Amir Temur']
z_shaxslar = ['Gabe Newell', 'Bill Gates']
t_shaxs = t_shaxslar.pop(0)
z_shaxs = z_shaxslar.pop(0)
print('Men tarixiy shaxslardan', (t_shaxs), 'bilan, zamonaviy shaxslardan esa', (z_shaxs), 'bilan suhbat qilishni istar edim')
 #('Behruz', 'Akmal', 'Bekzod', 'Sanjar', 'Boboxon')
friends = []
friends.append('Behruz')
friends.append('Akmal')
friends.append('Bekzod')
friends.append('Sanjar')
friends.append('Boboxon')

friends.remove('Sanjar')

friends.insert(0, 'Anvar')
friends.insert(2, 'Lola')
friends.append('Zafar') 

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))

print("Kelgan mehmonlar:", mehmonlar)