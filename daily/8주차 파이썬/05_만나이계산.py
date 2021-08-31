from datetime import datetime

name = input("이름은 >>> ")
birthday = input("생년월일(예:yyyymmdd) >>>")

b_year = int(birthday[:4])
b_month = int(birthday[4:6])
b_day = int(birthday[6:])

print("{} {} {}".format(b_year,b_month,b_day))

b_year = int(birthday)//10000
b_month = int(birthday) % 10000 // 100
b_day = int(birthday) % 100

print("{} {} {}".format(b_year,b_month,b_day))

c_year = datetime.today().year
c_month = datetime.today().month
c_day = datetime.today().day

today = c_year*10000 + c_month * 100 + c_day
birthday = b_year*10000 + b_month *100 + b_day
print("{} {}".format(today,birthday))
age = (today-birthday)//10000
print('{}님의 만 나이는 {}세입니다.'.format(name,age))
