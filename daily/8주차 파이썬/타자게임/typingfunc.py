import json,pickle,time,random
from operator import itemgetter

def loadandsave(dir,mode,item=''):
    with open(dir,mode) as f:
        if mode == 'r':
            item = json.load(f)
            print(item)
        elif mode == 'rb':
            item = pickle.load(f)
            print(item)
        elif mode == 'w':
            json.dump(item,f)
        elif mode == 'wb':
            pickle.dump(item,f)
    return item

def wordinput(word):
    mode = 1
    while mode:
        mode = input('추가할 단어 입력 >>> ')
        if mode:
            word.append(mode)
    print(word)
    return word

def game(word,rank):
    n = 1
    q = random.choice(word)
    input('시작!(enter)')
    start = time.time()
    while n<=5:
        print('{}번'.format(n))
        print(q)
        x = input()
        if q==x:
            print('통과!!')
            n +=1
            q = random.choice(word)
        else:
            print('오타! 다시도전!')
    end = time.time()
    print('걸린시간 : {:.0f}초'.format(end-start))
    name = input('이름을 입력하세요 >>> ')
    rank[name] = end-start
    print(rank)
    return rank

def ranklist(rank):
    rank_list = sorted(rank.items(),key=itemgetter(1))
    for index,item in enumerate(rank_list):
        print('{}등 {} {:.1f}'.format(index+1,item[0],item[1]))