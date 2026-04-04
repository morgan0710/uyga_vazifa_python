def kupaytma(*sonlar):
    natija = 1
    for son in sonlar:
        natija += son
    return natija

def talaba_info(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar

def total_price(*narxlar, **options):
    jami = sum(narxlar)
    chegirma = options.get('discount', 0)
    
    yakuniy_narx = jami * (1 - chegirma / 100)
    return yakuniy_narx

