from googletrans import Translator

tarjimon = Translator()

# matn = 'Python bu - eng yaxshi dasturlash tili'
# tarjima = tarjimon.translate(matn,dest='ru')
# print(tarjima.origin)
# print(tarjima.text)
# print(tarjima.src)

while True:
    text = input('Matnni kiriting (dasturdan chiqish uchun "q" deb yozing) : ')
    if text == 'q':
        print('Dastur to\'xtatildi!')
        break
    else:
        tarjima = tarjimon.translate(text,src='uz',dest='en')
        print(tarjima.text.title())