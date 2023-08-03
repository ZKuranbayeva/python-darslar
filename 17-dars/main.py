# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# kitoblar = ''
# savol = 'Sevimli kitibingiz nomini kiriting: '
# savol += "(dasturni to\'xtatish uchun 'stop' deb yozing)"
# while kitoblar != 'stop':
#     kitoblar = input(savol)
#     if kitoblar != 'stop':
#         print(kitoblar)
# print('Dastur tugadi')

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65
# gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va
# chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# savol1 = 'Yoshingizni kiriting: '
# savol1 += "(dasturni to'xtatish uchun 'exir' yoki 'quit' deb yozing)"
# while True:
#      qiymat = input(savol1)
#      if qiymat == 'exit' or qiymat == 'quit':
#          break
#      yosh = int(qiymat)
#      if yosh < 7:
#          narx = 2000
#      elif yosh >= 7 and yosh < 18:
#          narx = 3000
#      elif yosh >= 18 and yosh < 65:
#          narx = 10000
#      else:
#          narx = 0
#
#      if narx == 0:
#          print('Chipta bepul')
#      else:
#          print(f'Chipta narxi {narx} so\'m')
# print('Dastur tugadi')


# Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda.
# Xatolarni to'g'rilay olasizmi?

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    son = float(qiymat)
    if son < 0:
        continue
    else:
        ildiz = (son)**(0.5)
        print(f"{son} ning ildizi {ildiz} ga teng")
print("Dastur tugadi")