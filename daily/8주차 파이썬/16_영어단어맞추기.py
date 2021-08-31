import random

words = {"꽃":"flower", "나비":"butterfly", "학교":"school", "자동차":"car", "비행기":"airplane"}
count = 0 
while True:
   quiz = random.choice(list(words.keys()))
   answer = input('문제 : '+ quiz + '->')
   if answer == '':
       print('{}문제 맞추셨습니다. \n프로그램을 종료합니다.'.format(count))
       break
   elif words[quiz] == answer:
       count += 1
       print('정답!!')
   else:
       print('오답!')