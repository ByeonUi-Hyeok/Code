import funcpassword as pass1

while True:
    password = input('사용할 암호 입력 >>> ')
    if len(password) == 4:
        result = pass1.check(password)
        if result:
            print("사용할수 있는 암호입니다.")
        else:
            print('사용할수없는 암호입니다.')
    else:
        print("암호의 길이는 4글자 입니다.")