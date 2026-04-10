class Avto:
    def __init__(self, model, rang, korobka, narh, kilometr=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = kilometr

    def get_info(self):
        return f"{self.rang} {self.model}, {self.korobka} korobka, narhi: {self.narh}$, yurgan masofasi: {self.kilometr} km."

    def update_km(self, km):
        if km >= 0:
            self.kilometr += km
        else:
            print("Kilometrni kamaytirib bo'lmaydi!")

class Avtosalon:
    def __init__(self, salon_nomi, manzili):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.avtomobillar = []

    def add_avto(self, avto):
        self.avtomobillar.append(avto)

    def get_avtos_info(self):
        info = f"{self.salon_nomi} salonidagi avtomobillar:\n"
        for avto in self.avtomobillar:
            info += avto.get_info() + "\n"
        return info

avto1 = Avto("Gentra", "Qora", "Mexanika", 12000)
avto2 = Avto("Malibu", "Oq", "Avtomat", 30000, kilometr=500)

salon = Avtosalon("Mega Auto", "Toshkent sh.")
salon.add_avto(avto1)
salon.add_avto(avto2)

avto1.update_km(150)
print(salon.get_avtos_info())

print(f"Avto obyekt xususiyatlari: {avto1.__dict__}")
print(f"Avto klass metodlari: {dir(avto1)}")
print(f"String metodlari: {dir(str)}")
