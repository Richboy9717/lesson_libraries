import datetime as dt

hozir = dt.datetime.now().time()
bugun = dt.date.today()
#
ertaga = dt.date(2021,9,3)
# farq = ertaga - bugun
# print(bugun)
# print(ertaga)
# print(farq)

# from pprint import pprint
# import json

# file = 'bemor.json'
# with open(file) as f:
#     b = json.load(f)
# pprint(b)

# Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring

# two_nextweek = dt.date(2021,9,16)
#
# for day in list(range(1,11)):
#     two_nextweek = dt.date(2021, 9, 16+day)
#
#     print(two_nextweek)

# Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring

# ramazon = dt.date(2022,4,3)
# xayit = dt.date(2022,5,3)
# ramazon_farq = ramazon-bugun
# xayit_farq = xayit-bugun
# print(f'Ramazonga {ramazon_farq.days} kun qoldi!')
# print(f'\nXayitga {xayit_farq.days} kun qoldi!')

# Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing

# brithday = dt.date(1997,11,17)
# farq_year = bugun.year-brithday.year
# oy,kun = bugun.month-brithday.month,bugun.day-brithday.day
# print(f'Tug\'ilgan kuningizdan beri {farq_year} yil,{oy} oy va {kun} kun o\'tdi')

# Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring

import re

# andoza_phone = '^\+[1-9]\d{1,14}$'
#
# while True:
#     raqam = input('Telefon raqamingizni kiriting: ')
#     if re.match(andoza_phone,raqam):
#         print('Raqamingiz qabul qilindi!')
#         break
#     else:
#         print('Xato kiritdingiz,qayta urinib ko\'ring (namuna: +9989xxxxxxxx)')

from pprint import pprint

matn = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI """
# matn += "Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"
m = 'https://youtu.be/vsxJPRLXpgI'
andoz = "https?: \ / \ / (www \.)? [- a-zA-Z0-9 @:% ._ \ + ~ # =] {1,256} \. [a-zA-Z0-9 ()] { 1.6} \ b ([- a-zA-Z0-9 ()! @:% _ \ +. ~ #? & \ / \ / =] *)"

pr = re.findall(andoz,m)
print(pr)