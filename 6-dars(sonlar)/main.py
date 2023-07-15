# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
a = int(input('Istalgan sonni kiriting: '))
kvadrat = a**2
kub = a**3
print(f"{a} ning kvadrati {kvadrat} ga teng")
print(f"{a} ning kubi {kub} ga teng")

# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
hozir = 2023
yosh = int(input('Yoshingizni kiriting: '))
tugulgan_yil = hozir - yosh
print(f'Siz {tugulgan_yil} yilda tug\'ulgansiz')

# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
b = int(input("Birinchi sonni kiriting: "))
c = int(input("Ikkinchi sonni kiriting: "))
sum = b + c
ayirma = b - c
kopaytma = b * c
bolinma = b / c
print(f"{b} + {c} = {sum}")
print(f"{b} - {c} = {ayirma}")
print(f"{b} * {c} = {kopaytma}")
print(f"{b} / {c} = {bolinma}")