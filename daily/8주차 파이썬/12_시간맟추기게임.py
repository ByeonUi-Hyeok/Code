import time
# print(time.time())

time_diff = []
count = 0
while True:
    count += 1
    menu = input(str(count)+"번째 시도 : 시작!(종료:Q)")
    if menu.upper() == 'Q':
        break
    start = time.time()
    input("5초 후에 엔터를 입력하세요")
    end = time.time()
    time_diff.append(end-start)

#print(time_diff)
if not len(time_diff) == 0:
    print("기록한 시간 : ",time_diff)
    time_diff1 = [ data - 5 for data in time_diff] 
    result = list(map(abs,time_diff1))
    print("시간차이 : ",result)
    index = result.index(min(result))
    print("최종선택한 시간 : ",result[index])
else:
    print('저장된 정보가 없습니다.')

print("프로그램 종료!")