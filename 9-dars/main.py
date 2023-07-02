# ismlar = ['Ulugbek', 'Murod', 'Zumrad', 'Ali', 'Vali']
# for n in ismlar:
#     print('Xayrli kun', n)
# print(f"Kod 5 marta takrorlandi")
#
# toq_sonlar = list(range(11, 100, 2))
# print(toq_sonlar)
# for i in toq_sonlar:
#     print(i**3)

# kinolar = []
# print('5 ta sevimli filmlaringiz nomini kiriting: ')
# for n in range(5):
#     kinolar.append(input(f'{n+1}-filmingiz nomi: '))
#
# print(kinolar)


names = []
print('BUgun nechta kishi bilan suxbat qildingiz?')
soni = int(input())
for n in range(soni):
    names.append(input(f'{n+1}-suhbat qilgan odamingiz kim edi:'))

print(names)
