a = int(input('Juft son kiriting: '))
if a % 2 == 0:
    print('Raxmat')
else:
    print('Bu son juft emas!')


# yosh = int(input('Yoshingizni kiriting: '))
# if yosh < 5 or yosh > 59:
#     print('Sizga chipta bepul')
# elif yosh < 18:
#     print('CHipta narxi 10 000 so\'m')
# elif yosh > 17:
#     print('CHipta narxi 20 000 so\'m')


# b = int(input('Birinchi sonni kiriting: '))
# c = int(input('Ikkinchi sonni kiriting: '))
# if b > c:
#     print(f'{b} > {c}')
# elif  b < c:
#     print(f'{b} < {c}')
# elif  b == c:
#     print(f'{b} = {c}')


# mahsulotlar = ['olma', 'uzum', 'anor', 'behi', 'anjir', 'shaftoli', 'gilos', 'qulpnay', 'mandarin', 'banan']
# savat = []
# print('Savatga 5 ta mahsulot kiriting')
# savat.append(input('Savatga 1- mahsulotni qo\'shing:'))
# savat.append(input('Savatga 2- mahsulotni qo\'shing:'))
# savat.append(input('Savatga 3- mahsulotni qo\'shing:'))
# savat.append(input('Savatga 4- mahsulotni qo\'shing:'))
# savat.append(input('Savatga 5- mahsulotni qo\'shing:'))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f'{mahsulot} do\'konimizda bor!')
#     else:
#         print(f'{mahsulot} do\'konimizda yo\'q!')


# Kamchiligi bor
# mahsulotlar = ['olma', 'uzum', 'anor', 'behi', 'anjir', 'shaftoli', 'gilos', 'qulpnay', 'mandarin', 'banan']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# print('Savatga 5 ta mahsulot kiriting')
# savat.append(input('Birinchi mahsulotni kiriting: '))
# savat.append(input('Ikkinchi mahsulotni kiriting: '))
# savat.append(input('Uchinchi mahsulotni kiriting: '))
# savat.append(input('Tortinchi mahsulotni kiriting: '))
# savat.append(input('Beshinchi mahsulotni kiriting: '))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar and len(mavjud_emas) == 0:
#         bor_mahsulotlar.append(mahsulot)
#         print('bor')
#     elif mahsulot not in mahsulotlar:
#         mavjud_emas.append(mahsulot)
# print('yoq')
#
# print(bor_mahsulotlar)
# print(mavjud_emas)


# foydalanuvchilar = ['ulugbek', 'zumrad', 'murod', 'asqar', 'zebo']
# login = input('Login tanlang: ')
# if login in foydalanuvchilar:
#     print('Login band, yangi login tanlang!')
# else:
#     print('Xush kelibsiz!')


# a = int(input("IStalgan butun son kiriting: "))
# sonlar = list(range(2,11))
# for son in sonlar:
#     if a % son  == 0:
#         print(f"{a} soni {son} ga qoldiqsiz bo\'linadi")
#     elif a % son != 0:
#         print(f"{a} soni {son} ga qoldiqsiz bo\'linmaydi")
