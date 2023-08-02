# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting
# (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring
# Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
otam = {'ism': 'Rustam', 't_yili': '1956', 't_joyi': 'Qoraqalpogiston'}
onam = {'ism': 'Zulayho', 't_yili': '1960', 't_joyi': 'Qoraqalpogiston'}
akam = {'ism': 'Sherzod', 't_yili': '1988', 't_joyi': 'Qoraqalpogiston'}
opam = {'ism': 'Munira', 't_yili': '1982', 't_joyi': 'Qoraqalpogiston'}
print(f"Otamning ismi {otam['ism']},{otam['t_yili']}-yilda,{otam['t_joyi']}da tug'ulgan")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
taomlar = {
    'zumrad': 'osh',
    'murod': 'kabob',
    'ulugbek': 'somsa',
    'ded': 'shorva',
    'zuxra': 'dolma'
    }
print(f"Zumradning sevimli taomi {taomlar['zumrad']}")
print(f"Murodning sevimli taomi {taomlar['murod']}")
print(f"Dedning sevimli taomi {taomlar['ded']}")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
python_dic = {
    'string': 'matn',
    'if': 'agar',
    'for': 'uchun',
    'integer': 'butun son',
    'true': 'rost',
    'false': 'yolg\'on',
    'float': 'kasr son',
    'error': 'xato',
    'in': 'ichida',
    'or': 'yoki'
    }
print(python_dic)
print(python_dic['if'])

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
soz = input('Kalit so\'z kiriting: ')
if soz == 'in':
    print(python_dic['in'])
elif soz == 'string':
    print(python_dic['string'])
elif soz == 'if':
    print(python_dic['if'])
elif soz == 'for':
    print(python_dic['for'])
elif soz == 'integer':
    print(python_dic['integer'])
elif soz == 'true':
    print(python_dic['true'])
elif soz == 'false':
    print(python_dic['false'])
elif soz == 'error':
    print(python_dic['error'])
elif soz == 'or':
    print(python_dic['or'])
elif soz == 'float':
    print(python_dic['float'])
else:
    print('Mavjud emas!')
