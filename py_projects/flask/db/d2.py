import pymysql as my

connection = None # 변수를 선언 == 메모리에 상주
# 초기값을 셋팅할때 판단이 잘 안되면 None으로 셋팅한다.
try :                                                          # 예외 처리문 시작
    # 접속이 정상이라면 연결객체가 셋팅되고 연결실패나면 오류가 나서
    # 값에 세팅하는 코드가 수행되지 않으므로 원래의 값인 None을 들고 있게된다.          
    connection = my.connect( host        = 'localhost',     
                             user        = 'root',          
                             password    = '1234',          
                             database    = 'python_db',     
                            )
# try안의 connection = 뒤의 코드에서 아이디나 비번 이런것들이 에러나면 변수에 저장되지않고 바로 예외처리로 간다
# 그렇기때문에 변수에 값을 치환하는 코드가 수행되지 않으므로 오류가 발생한다.

except Exception as e:
    print('접속오류', e)

finally :
    # 접속이 되었을 때만(조건) 연결을 종료해야한다.
    if connection:   # == if connection == True / if 뒤에 변수를 넣으면 값있으면 True / 없으면 False 
        connection.close()
    print('종료')


'''
외부에서 db를 불러오는것도 일종의 외부 I/O를 끍어오는 것이기 때문에 with문을 사용하는것이 좋지만
나중에 with문을 사용하기때문에 겹치면 좋지않기 때문에 예외처리문을 사용한다.

'''
