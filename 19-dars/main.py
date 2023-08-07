# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
def ism_yosh_sora(ism, yosh, joriy_yil=2023):
    """Foydalanuvchi ismi va yoshini so'rab,
    uning tug'ilgan yilini hisoblaydigan funksiya"""
    print(f"Salom {ism.title()} siz {joriy_yil-yosh}-yilda tug'ulgansiz")

ism = input("Ismingizni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))
ism_yosh_sora(ism, yosh)


# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
def kv_kub_hisobla(son):
    """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati {son**2}.  "
          f"{son} ning kubi {son**3}")
son = int(input("Ixtiyoriy son kiriting: "))
kv_kub_hisobla(son)


# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def juft_toq_aniqla(son1):
    """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son1 % 2 == 0:
        print("Juft son")
    else:
        print("Toq son")
son1 = int(input("Ixtiyoriy son kiriting: "))
juft_toq_aniqla(son1)

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def kattasini_aniqla(num1, num2):
    """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya"""
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    elif num1 == num2:
        print('Sonlar teng!')
num1 = int(input("Birinchi sonni kiriting: "))
num2 = int(input("Ikkinchi sonni kiriting: "))
kattasini_aniqla(num1, num2)


# Foydalanuvchidan x va y sonlarini olib, x ning y darajasini konsolga chiqaruvchi funksiya yozing.
def darajaga_kotar(x, y):
    """Foydalanuvchidan x va y sonlarini olib, x ning y darajasini konsolga chiqaruvchi funksiya"""
    print(x**y)

x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
darajaga_kotar(x, y)

# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
darajaga_kotar(x, y=2)

# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi
# funksiya yozing. Natijalarni konsolga chiqaring.
def qoldiqsiz_bolin(num):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga
     qoldiqsiz bo'linishini tekshiruvchi funksiya"""
    for a in range(2, 11):
        if num % a == 0:
            print(f"{num} {a} ga qoldiqsiz bo'linadi")

num = int(input("Ixtiyoriy son kiriting: "))
qoldiqsiz_bolin(num)
