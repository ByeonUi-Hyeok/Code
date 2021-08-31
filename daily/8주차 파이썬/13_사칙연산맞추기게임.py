import random,time
from operator import itemgetter

rank=[['aaa', 4, 9.919916868209839],['bbb', 4, 8.919916868209839],['ccc', 3, 5.919916868209839]]

def multisort(xs,specs):
    for key,reverse in reversed(specs):
        xs.sort(key=itemgetter(key),reverse=reverse)
    return xs

while True:
    if 'Q' == input("종료(Q),계속(Enter)").upper():
        break
    count = 0
    oper = ['+','-','*','/']
    start = time.time()
    for x in range(1,6):
        x = random.randint(1,50)
        y = random.randint(1,50)
        op = random.choice(oper)
        quiz = str(x) + op + str(y)
        print(x,'번: ',quiz,"=")
        print(eval(quiz))
        c = input('정답은 = ')
        if c=='' and not c.isdecimal():
            c=0
        c = int(c)
        if int(eval(quiz)) == c:
            print('정답!!')
            count += 1
        else:
            print("오답!!")
    end = time.time()
    print('걸린시간 : ',end-start,'초')
    print(count,'개 맞음')
    name = input('이름은 >>> ')
    rank.append([name,count,end-start])
print(rank)
r = multisort(list(rank),((1,True),(2,False)))
for i,item in enumerate(r):
    print('{}등 {} {} {}'.format(i+1,item[0],item[1],item[2]))
    if i == 2:
        break