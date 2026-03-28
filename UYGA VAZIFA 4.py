davlatlar = ['Uzbekiston', 'Rassiya', 'AQSH', 'Qozag`iston', 'Qirg`iziston', 'Belarusiya', 'Polsha', 'Meksika', 'Braziliya', 'Avg`aniston', 'Pokiston', 'Eron', 'Iroq', 'Siriya', 'Turkiya', 'Savudiy Arabistoni', 'Misr', 'Izroyil', 'Falastin', 'Germaniya', 'Fransiya', 'Buyuk Britaniya', 'Islandiya', 'Shvetsiya', 'Gretsiya', 'Qanada', 'Indiya', 'Xitoy']
print(davlatlar)

print("sorted() qaytargan ro`yxat:", sorted(davlatlar))
print("sorted() qaytargan ro`yxat:", sorted(davlatlar, reverse=True))
print('Asl ro`yxat o`zgarmas qoldi:', davlatlar)

davlatlar.reverse()
print(davlatlar)

davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

txt = list(range(12,1201, 2))
print(txt)
jami = sum(txt)
print("Jami:", jami)
Katta = max(txt)
Kichik = min(txt)
print("Eng katta va eng kichik son o'rtasidagi ayirmani:", Katta - Kichik)
print(print("Elementlar soni:", len(txt)))
print('Ro`hatni boshi:', txt[:20], 'Ro`yhatni oxiri:', txt[-20:])

taomlar = ['Somsa', 'osh', 'shashlik', 'shorva', 'qozon kabob']
nonushta = taomlar[:]
nonushta.append('non')
nonushta.append('go`ma barak')
print('Taomlar:', taomlar)
print('Nonushta:', nonushta)
#nonushta[0] = 'qaymoq va non'
nonushta = tuple(nonushta)
