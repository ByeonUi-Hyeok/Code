import datetime

datetime.datetime.today()

from datetime import datetime

current_year = datetime.today().year
# print(type(current_year))
# print(current_year)

print('현재년도는 {}년 입니다.'.format(current_year))
name = input("이름은 >>> ")
birth = int(input("출생년도 >>> "))
age = current_year-birth
print('{}님의 나이는 {}세 입니다.'.format(name,age))