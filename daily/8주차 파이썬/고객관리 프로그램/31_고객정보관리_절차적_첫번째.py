import re,sys
custlist=[]
page = -1

while True:
    display= '''
I - 고객정보 입력
C - 현재 고객정보 조회
P - 이전 고객정보 조회
N - 다음 고객정보 조회
U - 고객 정보 수정
D - 고객 정보 삭제
Q - 프로그램 종료
메뉴를 선택하세요 >>> '''
    choice = input(display).upper()
    if choice == 'I':
        customer = {'name':'','gender':'','email':'','birthyear':''}

    elif choice == 'C':
        pass
    elif choice == 'P':
        pass
    elif choice == 'N':
        pass
    elif choice == 'U':
        pass
    elif choice == 'D':
        pass
    elif choice == 'Q':
        sys.exit()
    else:
        print('메뉴를 잘못 입력하셨습니다.')

