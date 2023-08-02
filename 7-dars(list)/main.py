# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['Zumrad', 'Murod', 'Ulugbek']

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
ism = ismlar.pop(0)
print("Salom " + ism)
ism = ismlar.pop(0)
print("Hayr " + ism)

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [5 , 11 , -6 , 225.5]

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
print(sonlar[0] + sonlar[2])
sonlar[0] = 7
sonlar[3] = sonlar[3] + 0.5
print(sonlar)

# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ['Imom Buxoriy', 'Ibn Sino', 'Termiziy']
z_shaxslar = ['Mishariy Alafasi', 'Zakir Nayk', 'Elon Mask', 'Anvar Narzullayev']

# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
print(f'Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan, zamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan suxbat qurushni istar edim')

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends = []
friends.append('Madina')
friends.append('Gulnora')
friends.append('Raxima')
friends.append('Sevara')
friends.append('Gulzoda')
print(friends)

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.
friends.remove('Madina')
friends.remove('Sevara')
print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append('Soliha')
print(friends)
friends.insert(0, 'Sumayya')
friends.insert(3, 'Xadicha')
print(friends)

# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(3))
print(mehmonlar)