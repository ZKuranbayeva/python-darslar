son = float(input("Juft son kiriting: "))
if son%2==0:
    print("Raxmat.")
else:
    print("Bu son juft emas.")

yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18 and yosh>4:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f'{x}<{y}')
else:
    print(f"{x}>{y}")

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")


mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
for mahsulot in mavjud_emas:
  print(mahsulot)


users = ['alisher1983', 'aziza', 'yasina' 'umar']

login = input("Yangi login tanlang: ")
if login in users:
      print('Login band, yangi login tanalng!')
else:
      print("Xush kelibsiz!")