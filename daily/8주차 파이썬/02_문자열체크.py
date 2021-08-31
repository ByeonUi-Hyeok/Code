email = input("email을 입력하세요 >> ")
if email[-6:] == '@co.kr':
    print("포함합니다.")
else:
    print("포함하지 않습니다.")