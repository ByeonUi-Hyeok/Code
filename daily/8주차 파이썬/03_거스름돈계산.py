price = int(input("물건가격 >> "))
money = int(input("받은 돈 >> "))

change = money-price

if change  > 0:
    print("다음과 같이 거슬러 주세요")
    m1 = change//10000
    m2 = (change-10000*m1)//5000
    m3 = (change-10000*m1-5000*m2)//1000
    m4 = (change-10000*m1-5000*m2-1000*m3)//500
    m5 = (change-10000*m1-5000*m2-1000*m3-500*m4)//100
    m6 = (change-10000*m1-5000*m2-1000*m3-500*m4-100*m5)//50
    m7 = (change-10000*m1-5000*m2-1000*m3-500*m4-100*m5-50*m6)//10
    print("만원권{}장,오천원권{}장,천원권{}장,오백원{}개,백원{}개,십원{}개".format(m1,m2,m3,m4,m5,m6,m7))
