import random
print('Привет! Это игра висельница, у тебя есть семь попыток отгадать слово, иначе человечек повесится.')
print('    ___________')
print('              |')
print('              |')
print('              |')
print('              |')
print('             _|_')
words = open("russian_nouns.txt", "r").read().split("\n")
viselec = 0
slovo = random.choice(words)
shifr =  [] #зашифровоное слово
for i in range(0, len(slovo)):
   shifr.append(i)
while shifr != slovo:
    bukva = input() #ввод
    
    if bukva in shifr:
      countine
      print('такая буква уже найдена! напиши другую.')
      
    if len(bukva) > 1:
      bukva = bukva[0]
#проверка на дурака

    if bukva in slovo:
      

    else:
      if viselec = 0:
       print('    ___________')
       print('    |         |')
       print('              |')
       print('              |')
       print('              |')
       print('             _|_')
    elif viselec = 1:
       print('    ___________')
       print('    |         |')
       print('   😃         |')
       print('              |')
       print('              |')
       print('             _|_')
      elif viselec = 2:
       print('    ___________')
       print('    |         |')
       print('   😃         |')
       print('    |         |')
       print('              |')
       print('             _|_')
      elif viselec = 3:
       print('    ___________')
       print('    |         |')
       print('   😃         |')
       print('    |\        |')
       print('              |')
       print('             _|_')
      elif viselec = 4:
       print('    ___________')
       print('    |         |')
       print('   😃         |')
       print('   /|\        |')
       print('              |')
       print('             _|_')
      eif viselec = 5:
       print('    ___________')
       print('    |         |')
       print('   😃         |')
       print('   /|\        |')
       print('     \        |')
       print('             _|_')
      elif viselec = 6:
       print('    ___________')
       print('    |         |')
       print('   😃         |')
       print('   /|\        |')
       print('   / \        |')
       print('             _|_')
       #конец игры висельницы
       break
       print('КОНЕЦ ИГРЫ! ты проиграл')






#пример

slovo = 'привет'
shifr = []
bukva = 'в'
t = 1234567890
for i in range(0, len(slovo)):
    shifr.append(i)
print(*shifr)
for i in shifr:
    if int(i) in int(t):
        if slovo[i] == bukva:
            shifr[i] = slovo[i]

print(shifr)
