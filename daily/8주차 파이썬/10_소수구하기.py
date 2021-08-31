while True:
    a = input('1보다 큰수를 입력하세요 >>>')
    if a == '':
       break
    if not(a.isdecimal()):
       break
    a = int(a)
    b = 0
    for i in range(2,a):
        if a%i == 0:
            b = 1
    if b == 0:
        print('소수')
    else:
        print('소수아님')
