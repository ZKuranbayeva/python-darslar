# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for
# tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
python_dic = {
    'in': 'ichida',
    'if': 'agar',
    'and': 'va',
    'float': 'kasr son',
    'boolen': 'mantiqiy qiymat',
    'integer': 'butun son',
    'or': 'yoki',
    'for': 'uchun',
    'remove': 'o\'chirish',
    'key': 'kalit'
}

for key, value in sorted(python_dic.items()):
    print(f'{key.title()} - {value.capitalize()}')


# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida,
# alifbo ketma-ketligida konsolga chiqaring.
davlatlar = {
    'italiya': 'rim',
    'fransiya': 'parij',
    'rossiya': 'moskva',
    'turkiya': 'anqara',
    'eron': 'tehron'
}

print('Dunyo davlatlari:')
for davlat, poytaxt in sorted(davlatlar.items()):
    print(davlat.upper())

print('Davlatlarning poytaxtlari:')
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.'
#  Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
dav_user = input('Istalgan davlatni kiriting: ')
if dav_user.lower() == 'italiya':
    print(f"Bu davlatning poytaxti {davlatlar['italiya']}")
elif dav_user.lower() == 'fransiya':
    print(f"Bu davlatning poytaxti {davlatlar['fransiya']}")
elif dav_user.lower() == 'rossiya':
    print(f"Bu davlatning poytaxti {davlatlar['rossiya']}")
elif dav_user.lower() == 'turkiya':
    print(f"Bu davlatning poytaxti {davlatlar['turkiya']}")
elif dav_user.lower() == 'eron':
    print(f"Bu davlatning poytaxti {davlatlar['eron']}")
else:
    print('Bunday davlat lug\'atda mavjud emas')

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma
# berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating,
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
menu = {
    'osh': '20000',
    'kabob': '15000',
    'somsa': '8000',
    'manti': '5000',
    'lagmon': '25000',
    'choy': '3000',
    'cola': '12000',
    'non': '5000',
    'salat': '10000',
    'coffee': '10000'
}
buyurtmalar = []
buyurtmalar.append(input('Birinchi taomni kiriting: '))
buyurtmalar.append(input('Ikkinchi taomni kiriting: '))
buyurtmalar.append(input('Uchinchi taomni kiriting: '))
for taom in menu:
    if taom in buyurtmalar:
        print(f"{taom.title()} {menu[taom]} so'm")


for taom  in buyurtmalar:
    if taom not in menu:
        print(f"Bizda {taom.title()} yo'q")

