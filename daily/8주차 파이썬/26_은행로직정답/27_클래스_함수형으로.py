import accountfunc as af
import pickle

# account_list =[]
# account_count=0

f = open('account.pickle','rb')
account_list = pickle.load(f)
account_count =len(account_list)
print(account_count)
while True:
    display = '''
    1. 계좌개설
    2. 입금
    3. 출금
    4. 입출금내역
    5. 총계좌수출력
    6. 전체계좌리스트
    7. 종료
    >>> '''
    menu = input(display)
    if menu == '1':
        name = input('이름 >>> ')
        balance = int(input('입금금액 >>>'))
        a = af.acc_init(name,balance,account_count)
        account_list.append(a[0])
        account_count=a[1]
        print('계좌가 개설되었습니다.')
        print(a[0])
    elif menu == '2':
        num = input('계좌번호입력 >>> ')
        check = 0
        for acc in account_list:
            if acc['account_number'] == num:
                check = 1
                amount = int(input("입금금액 >> "))
                af.deposit(acc,amount)
                print(acc)
        if check == 0:
            print('계좌번호가 없습니다.')
    elif menu == '3':
        num = input('계좌번호 >>> ')
        check = 0
        for acc in account_list:
            if acc['account_number'] == num:
                check = 1
                amount = int(input('출금금액 >>> '))
                af.withdraw(acc,amount)
        if check == 0:
            print('계좌번호가 없습니다.')
    elif menu == '4':
        num = input('계좌번호 >>> ')
        check = 0
        for acc in account_list:
            if acc['account_number'] == num:
                check = 1
                for data in acc['total_log']:
                    print('{} : {}'.format(data[0],data[1]))
        if check == 0:
            print('계좌번호가 없습니다.')        
    elif menu == '5':
        af.get_account_num(account_count)
    elif menu =='6':
        for acc in account_list:
            print(acc)
    elif menu == '7':
        print('프로그램을 종료합니다.!')
        break

f = open('account.pickle','wb')
pickle.dump(account_list,f)