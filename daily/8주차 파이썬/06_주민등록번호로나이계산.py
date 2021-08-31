from datetime import datetime

ssn = input("주민등록번호 >>> ")

if ssn[7] in ['1','2']:
    year = int("19"+ ssn[:2])
elif ssn[7] in ['3','4']:
    year = int("20"+ssn[:2])

month = int(ssn[2:4])
day = int(ssn[4:6])

c_year = datetime.today().year
c_month = datetime.today().month
c_day = datetime.today().day

today = c_year * 10000 + c_month * 100 + c_day
birthday = year * 10000 + month * 100 + day

age = (today - birthday) // 10000

print('나이는 만{}세입니다.'.format(age))
