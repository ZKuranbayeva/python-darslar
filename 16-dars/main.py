# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang.
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

shaxs0 = {
    'ism': 'Toxir Malik',
    'tyil': '1946',
    'tjoy': 'Toshkent',
    'vafoti': '2019',
    'asarlar': ['Alvido bolalik', 'Shaytanat']
}

shaxs1 = {
    'ism': 'Tog\'ay Murod',
    'tyil': '1948',
    'tjoy': 'Surxandaryo',
    'vafoti': '2003',
    'asarlar': ['Otamda qolgan dalalar', 'Yulduzlar mangu yonadi']
}

shaxs2 = {
    'ism': 'Lev Tolstoy',
    'tyil': '1828',
    'tjoy': 'Rossiya',
    'vafoti': '1910',
    'asarlar': ['Urush va tinchlik', 'Anna Karenina']
}

shaxs3 = {
    'ism': 'Ernest Heminguey',
    'tyil': '1899',
    'tjoy': 'AQSH',
    'vafoti': '1961',
    'asarlar': ['Chol va dengiz', 'To\'qchilik va yo\'qchilik']
}

shaxslar = [shaxs0, shaxs1, shaxs2,shaxs3]
for shaxs in shaxslar:
    print(f"{shaxs['ism']} {shaxs['tyil']}-yilda, "
          f"{shaxs['tjoy']}da tug'ulgan."
          f"{shaxs['vafoti']}-yilda vafot etgan")

# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning
# ismi va uning asarlarini konsolga chiqaring.
for shaxs in shaxslar:
    print(f"\n{shaxs['ism']}ning mashxur asarlari:")
    for asar in shaxs['asarlar']:
        print(asar)

# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit,
# uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
dostlar = {
    'Sevara': ['Qish sanatasi', 'Sevgi iztirobi', 'Kuz ertagi'],
    'Gulnora': ['Terminator', 'Jeyms Bond', 'Qasoskorlar'],
    'Raxima': ['Forest Gamp', 'Gladiator', 'Cho\'qintirgan ota']
}
for dost, filmlar in dostlar.items():
    print(f"\n{dost}ning sevimli kino va seriallari:")
    for film in filmlar:
        print(film)

# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
# Har bir davlat haqida ma'lumotni konsolga chiqaring.
davlatlar = {
    'AQSH':{'poytaxti': 'Washington',
            'aholisi': '320 mln',
            'pul birligi': 'dollar'},
    'Yaponiya': {'poytaxti': 'Tokio',
                'aholisi': '127 mln',
                 'pul birligi': 'iyena'},
    'Rossiya': {'poytaxti': 'Moskva',
                'aholisi': '146 mln',
                 'pul birligi': 'rubl'}
}
for davlat, info in davlatlar.items():
    print(f"\n{davlat.title()}ning poytaxti {info['poytaxti']}."
          f"Aholi soni {info['aholisi']} va pul birligi "
          f"{info['pul birligi'].title()}")

# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan
# davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida
# ma'lumot yo'q" degan xabarni chiqaring.
davlat = input('\nDavlat nomini kiriting: ')
if davlat in davlatlar:
    print(f"\n{davlat.title()}ning poytaxti {info['poytaxti']}."
          f"Aholi soni {info['aholisi']} va pul birligi "
          f"{info['pul birligi'].title()}")
else:
    print('Bizda bu davlat haqida ma\'lumot yo\'q!')