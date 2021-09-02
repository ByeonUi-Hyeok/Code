import re,sys
custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong12@gmail.com', 'birthyear': '2000'},
          {'name': '박나리', 'gender': 'F', 'email': 'park12@gmail.com', 'birthyear': '2001'},
          {'name': '김철수', 'gender': 'M', 'email': 'kim12@gmail.com', 'birthyear': '2010'},
          {'name': '이유리', 'gender': 'F', 'email': 'lee012@gmail.com', 'birthyear': '2003'} ]
page = len(custlist)-1

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
        if page >= 0:
            print('현재 페이지는 {}페이지 입니다.'.format(page+1))
            print(custlist[page])
        else:
            print('입력된 정보가 없습니다.')

    elif choice == 'P':
        if page <= 0:
            print('첫페이지 입니다.')
        else:
            page -= 1
            print('현재 페이지는 {}페이지 입니다.'.format(page+1))
        print(custlist[page])

    elif choice == 'N':
        if page >= len(custlist)-1:
            print('마지막 페이지입니다.')
        else:
            page += 1
            print('현재 페이지는 {}페이지 입니다.'.format(page+1))
        print(custlist[page])

    elif choice == 'U': #수정시 이메일 체크 name,gender,birthday 중 하나 선택해서 수정
        while True:
            email = input('수정하시려는 고객 정보의 email을 입력하세요 >>> ')
            idx = -1 
            for i in range(len(custlist)):
                if custlist[i]['email'] == email:
                    idx=i
                    break
            if idx == -1:
                print('등록된 데이타가 없습니다.')
                break

            selector = input('''
            다음중 수정할 항목을 선택하세요
            (name,gender,birthday(종료:enter))
             ''')
            if selector in('name','gender','birthday'):
                custlist[idx][selector] = input('수정할 {}을 입력하세요 '.format(selector))
            elif selector  == '':
                print('입력종료!')
            else:
                print('존재하지 않는 정보입니다.')
            page = idx
            break    
            
    elif choice == 'D':
        email = input('삭제하시려는 고객 정보의 email을 입력하세요 >>> ')
        idx = -1
        for i in range(len(custlist)):
            if custlist[i]['email'] == email:
                idx = i
                print("{}님의 고객 정보를 삭제합니다.".format(custlist[i]['name']))
                del custlist[i]
                page = idx -1
                break
        if idx == -1:
            print('등록되지 않은 정보입니다.')
        print(custlist)

    elif choice == 'Q':
        sys.exit()
    else:
        print('메뉴를 잘못 입력하셨습니다.')

