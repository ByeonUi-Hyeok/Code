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
        customer['name'] = input('이름을 입력하세요 >>> ')
        while True:
            customer['gender'] = input('성별입력하세요(M/m,F/f) >>> ').upper()
            if customer['gender'] in ('M','F'):
                break

        while True:
            ftm = re.compile('^[a-z][a-z0-9]{4,}@([a-z]{2,6}.)+[a-z]{2,3}$')
            while True:
                customer['email']=input('이메일을 입력하세요 >>> ')
                if ftm.search(customer['email']):
                    break
                else:
                    print('@을 포함하여 정확한 이메일을 입력하세요')
            check = 0 
            for i in custlist:
                if i['email'] == customer['email']:
                    check = 1
            if check == 0:
                break
            print("중복되는 이메일이 있습니다.")
        while True:
            customer['birthyear'] = input('출생년도 4자리를 입력해주세요 >>> ')
            if len(customer['birthyear'])==4 and customer['birthyear'].isdigit():
                break
        custlist.append(customer)
        page = len(custlist)-1
        print(customer)
        print(custlist)
        print(page)

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

