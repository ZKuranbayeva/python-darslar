# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
buyurtmalar = []
n = 1
while True:
    savol = f"{n}-buyurtmangizni kiriting: "
    buyurtma = input(savol)
    buyurtmalar.append(buyurtma)
    talrorlash = input("Yana buyurtma qo'shasizmi? (ha\yo'q)")
    n+=1
    if talrorlash != 'ha':
        break

print(buyurtmalar)


# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
#  Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
bozorlik = {}
ishora = True
while ishora:
    mahsulotlar = input("Mahsulotlarni kiriting: ")
    narxlar = input(f"{mahsulotlar.title()}ning narxini kiriting: ")
    bozorlik[mahsulotlar] = int(narxlar)
    javob = input("Yana mahsuloat qo'shasizmi?(ha\yo'q)")
    if javob == "yo'q":
        ishora = False
for mahsulotlar, narxlar in bozorlik.items():
    print(f"{mahsulotlar.title()} {narxlar} so'm")

# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi
# mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa
# mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
e_bozor ={
    'olma': '200',
    'anjir': '300',
    'shaftoli': '400',
    'uzum': '200',
    'choy': '100',
    'non': '100'
}

buyurtmalar0 = ['anjir', 'suv', 'somsa', 'sut']
while buyurtmalar0:
    buyurtma0 = buyurtmalar0.pop()
    if buyurtma0 in e_bozor.keys():
        narx = e_bozor[buyurtma0]
        print(f"{buyurtma0.title()} - {narx} so'm")
    else:
        print(f"Bizda {buyurtma0} yo'q")

