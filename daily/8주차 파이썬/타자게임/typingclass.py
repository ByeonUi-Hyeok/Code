import json,pickle,time,random
from operator import itemgetter
import os,sys

class TypingGame:
    word = ['cat','dog','fox','monkey', 'mouse','panda','frog','snake','wolf']  # 문제리스트 작성
    dir = os.path.dirname(__file__)
    rank = {}

    def loadandsave(self,dir,mode,item=''):
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

    def wordinput(self,word):
        mode = 1
        while mode:
            mode = input('추가할 단어 입력 >>> ')
            if mode:
                word.append(mode)
        print(word)
        return word

    def game(self,word,rank):
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

    def ranklist(self,rank):
        rank_list = sorted(rank.items(),key=itemgetter(1))
        for index,item in enumerate(rank_list):
            print('{}등 {} {:.1f}'.format(index+1,item[0],item[1]))

    def menuDisplay(self):
        display = '''
1.문제추가 2.문제저장 3.문제읽기 4.타자게임 5.등수리스트 6.종료 
선택 >>> '''     
        menu = input(display)
        if menu=='1':
            TypingGame.word = self.wordinput(TypingGame.word)
        elif menu=='2':
            self.loadandsave(TypingGame.dir+'/word.json','w',TypingGame.word)
        elif menu == '3':
            TypingGame.word = self.loadandsave(TypingGame.dir+'/word.json','r')
        elif menu == '4':
            TypingGame.rank = self.game(TypingGame.word,TypingGame.rank)
        elif menu == '5':
            self.ranklist(TypingGame.rank)
        elif menu == '6':
            self.loadandsave(TypingGame.dir+'/rank.pickle','wb',TypingGame.rank)
            print('프로그램을 종료합니다.!')
            sys.exit()
        else:
            print('메뉴를 잘못입력하셨습니다.')

    def __init__(self):
        TypingGame.rank = self.loadandsave(TypingGame.dir+'/rank.pickle','rb')
        while True:
            self.menuDisplay()


TypingGame()