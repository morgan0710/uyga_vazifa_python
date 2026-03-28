tx = input("Istalgan soni kiriting:")
kvd = int(tx)**2
print(str(tx), "ning kvadrati", str(kvd), "ga teng")
kub = int(tx)**3
print(str(tx), "ning kubi", str(kub), "ga teng")

t_yil = input("Yoshingiz nicha:")
yosh = 2020 - int(t_yil)
print("Siz", str(yosh), "da tug`ilgansiz.")

txt = input("Birinchi soni kiriting:")
txt2 = input("Ikkinchi soni kiriting:")
qoshish = int(txt) + int(txt2)
print(str(txt), "+", str(txt2), "=", str(qoshish))
ayirish = int(txt) - int(txt2)
print(str(txt), "-", str(txt2), "=", str(ayirish))
kopaytirish = int(txt) * int(txt2)
print(str(txt), "*", str(txt2), "=", str(kopaytirish))
bolish = int(txt) / int(txt2)
print(str(txt), "/", str(txt2), "=", str(bolish))