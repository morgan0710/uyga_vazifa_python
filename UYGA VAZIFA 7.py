# oila = {}
# oila['oila'] = 'Otamning'
# oila['ismi'] = 'Dilshod'
# oila['yil'] = 1978
# oila['viloyat'] = 'Xorazm'
# print(f"{oila['oila']}, ismi {oila['ismi']}, {oila['yil']}-yilda, {oila['viloyat']} viloyatida tug`ilgan")
# oila['oila'] = 'Onamning'
# oila['ismi'] = 'Rayhon'
# oila['yil'] = 1988
# oila['viloyat'] = 'Qoraqalpog`iston'
# print(f"{oila['oila']}, ismi {oila['ismi']}, {oila['yil']}-yilda, {oila['viloyat']} Respubilkasi tug`ilgan")
# oila['oila'] = 'Opamning'
# oila['ismi'] = 'Gulirano'
# oila['yil'] = 2009
# oila['viloyat'] = 'Xorazm'
# print(f"{oila['oila']}, ismi {oila['ismi']}, {oila['yil']}-yilda, {oila['viloyat']} viloyatida tug`ilgan")
# oila['oila'] = 'Singlimning'
# oila['ismi'] = 'Malika'
# oila['yil'] = 2022
# oila['viloyat'] = 'Xorazm'
# print(f"{oila['oila']}, ismi {oila['ismi']}, {oila['yil']}-yilda, {oila['viloyat']} viloyatida tug`ilgan")

# oila = {}
# oila['ismi'] = 'Otamning'
# oila['taom'] = 'osh'
# print(f"{oila['ismi']} sevimli taomi {oila['taom']}")
# oila['ismi'] = 'Onamning'
# oila['taom'] = 'Somsa'
# print(f"{oila['ismi']} sevimli taomi {oila['taom']}")
# oila['ismi'] = 'Singlimning'
# oila['taom'] = 'kabob'
# print(f"{oila['ismi']} sevimli taomi {oila['taom']}")

py_lugat = {
    'integer': 'Butun son',
    'float': "O'nlik son",
    'string': 'Matn',
    'if': 'Agar',
    'else': 'Aks holda',
    'boolean': 'Mantiqiy qiymat',
    'list': "Ro'yxat",
    'dictionary': "Lug'at",
    'tuple': "O'zgarmas ro'yxat",
    'for': 'Sikl (uchun)'
}

kalit = input('Kalit so`z kiriting: ').lower()
tarjima = py_lugat.get(kalit)
if tarjima:
    print(tarjima)
else:
    print('Bunda so`z mavjud emas')

kalit = input('Kalit so`z kiriting: ').lower()
if kalit in py_lugat:
    print(f"{kalit.title()} so`zi {py_lugat[kalit]} deb tarjima qilinadi")
else:
    print("Bunday so`z mavjud emas")