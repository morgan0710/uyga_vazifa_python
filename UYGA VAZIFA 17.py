import datetime as dt

bugun = dt.date.today()

for i in range(10):
    farq = dt.timedelta(days=i * 14)
    kelgusi_sana = bugun + farq
    
    print(f"-sana: {kelgusi_sana}")

bugun = dt.date.today()
ramazon = dt.date(2027,3,8)
farq = ramazon-bugun
print(farq)
print(f"Ramazonga {farq.days} kun qoldi")

bugun = dt.date.today()
qurbon_hayit = dt.date(2026,5,27)
farq = qurbon_hayit-bugun
print(farq)
print(f"Qurbon hayitga {farq.days} kun qoldi")

tugilgan_kun = dt.date(2010,12,7)
print(tugilgan_kun)

import re

andoza = r"^\+998\d{9}$" 

tel = "+998947161007"

if re.match(andoza, tel):
    print("to`g`ri")
else:
    print('Xato')

