import random
print('Привет! Это игра висельница, у тебя есть семь попыток отгадать слово, иначе человечек повесится.')
print('    ___________')
print('              |')
print('              |')
print('              |')
print('              |')
print('             _|_')
words = ['яблоко', 'инструмент', 'лестница', 'чай', 'пакет', 'настройки', 'лиса', 'стакан', 'кровать', 'чебурек', 'человек', 'программа', 'пробел', 'цифра', 'число', 'клавиша', 'бассейн', 'велосипед', 'питон', 'исскуство', 'кружка']
viselec = 0
slovo = random.choice(words)
shifr =  [] #зашифровоное слово
for i in range(0, len(slovo)):
   shifr.append(i)
print(*shifr)
while shifr != slovo:
    bukva = input() #ввод
   
    if bukva in shifr:
      countine
      print('такая буква уже найдена! напиши другую.')
      
    if len(bukva) > 1:
      bukva = bukva[0]
#проверка на дурака

    if bukva in slovo:
      for i in range(0, len(slovo)):
         shifr.append(i)
    for i in shifr:
      if slovo[i] == bukva:
         shifr[i] = bukva #питон ругается на это почему то при вводе второй буквы

    else:
       if viselec == 0:
          print('    ___________')
          print('    |         |')
          print('              |')
          print('              |')
          print('              |')
          print('             _|_')
       elif viselec == 1:
          print('    ___________')
          print('    |         |')
          print('   😃         |')
          print('              |')
          print('              |')
          print('             _|_')
       elif viselec == 2:
          print('    ___________')
          print('    |         |')
          print('   😃         |')
          print('    |         |')
          print('              |')
          print('             _|_')
       elif viselec == 3:
          print('    ___________')
          print('    |         |')
          print('   😃         |')
          print('    |\        |')
          print('              |')
          print('             _|_')
       elif viselec == 4:
          print('    ___________')
          print('    |         |')
          print('   😃         |')
          print('   /|\        |')
          print('              |')
          print('             _|_')
       elif viselec == 5:
          print('    ___________')
          print('    |         |')
          print('   😃         |')
          print('   /|\        |')
          print('     \        |')
          print('             _|_')
       elif viselec == 6:
          print('    ___________')
          print('    |         |')
          print('   😃         |')
          print('   /|\        |')
          print('   / \        |')
          print('             _|_')
          #конец игры висельницы
          break
          print('КОНЕЦ ИГРЫ! ты проиграл')
       viselec += 1
