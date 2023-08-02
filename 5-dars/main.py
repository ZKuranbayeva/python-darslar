# Quyidagi o'zgaruvchilarni yarating:
kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
kocha = input("Ko'cha nomini kiriting: ")
mahalla = input("Mahalla nomini kiriting: ")
tuman = input("Tuman nomini kiriting: ")
viloyat = input("Viloyat nomini kiriting: ")
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")

# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
manzil = (f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
print(manzil.title())
print(manzil.capitalize())
print(manzil.lower())
print(manzil.upper())