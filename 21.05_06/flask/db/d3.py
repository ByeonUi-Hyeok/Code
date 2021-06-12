import pymysql as my

connection = None
# 예외처리를 사용함으로써 셧다운을 방지할 수 있다. 
# 예외처리문은 제일 큰 틀에서 제작한다.
try :                    
    connection = my.connect( host        = 'localhost',     
                             user        = 'root',          
                             password    = '1234',          
                             database    = 'python_db',     
                            )
    # 쿼리 수행
    # 1. 커서 획득
    cursor = connection.cursor()
    # 2. SQL 생성 (db 조회할것이기때문에 db가 알아 들을 수 있는 언어로 전송 해야함)
    sql   = '''
                SELECT
                        *
                FROM
                        users_tbl
                WHERE
                        uid='guest'
                AND
                        upw='1'; ''' 
    # 3. SQL 실행 (명령실행 ==> DB로가서 ==> 실행)
    cursor.execute( sql )
    
    # 4. 결과 패치(리턴) 위에서 바로 받는게아니라 따로 해놓는것은 비동기기때문에 상대방이 바로줄지 1초뒤에줄지 모르기 때문이다.
    row = cursor.fetchone()
    
    # 5. 결과확인
    print( row )
    # row에서 이름만 나오게 하고 싶다면? 
    # == row는 튜플 == 튜플은 순서가있음 == 인덱스 == 이름은 인덱스 3에있음 == 인덱스사용법 == 변수[인덱스]
    # 문제점 : 독립적이지 않음 == 테이블의 컬럼 순서가 바뀌면 코드도 바뀌어야 한다.
    # 문제점 해결 방법 : 순서 의존성을 제거하면 된다. == 딕셔너리로 결과물이 오면 해결된다.
    print( row[3] )

except Exception as e:
    print('접속오류', e)

finally :
    
    if connection:  
        connection.close()
    else:
        print('에러나서 종료못함 ')
