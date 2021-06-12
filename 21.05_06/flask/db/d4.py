import pymysql as my

connection = None

try :                    
    connection = my.connect( host        = 'localhost',     
                             user        = 'root',          
                             password    = '1234',          
                             database    = 'python_db',
                             cursorclass = my.cursors.DictCursor ) # Dictursor == 커서의 인자?를 딕셔너리로
                                                                   # 즉 결과물이 딕셔너리형태로 나온다.
                                                                   # 넣지않는다면== default 값은 tuple로 나온다.
    cursor = connection.cursor()
    #cursor = connection.cursor( my.cursors.DictCursor )
    #위에서 cursorclass쓰지 않고 커서에다가 집어넣어도 결과물이 딕셔너리로 나온다.
    sql   = '''
                SELECT
                        *
                FROM
                        users_tbl
                WHERE
                        uid='guest'
                AND
                        upw='1'; ''' 
                        # 코드의 문제점 == uid, upw가 하드코딩 되어있다.(고정되어있다.)
                        # sql에서 뽑아서 쿼리 수행시 인자로 전달되게 수정해야한다.
    cursor.execute( sql )
    row = cursor.fetchone()
    print( row['name'] ) # Dictcusor로 인자를 딕셔너리로 바꿨기 때문에 db의 컬럼이 순서가 바뀌어도 상관없다.
                         # 딕셔너리 밸류값 뽑아내는법 변수['키'] 
    

except Exception as e:
    print('접속오류', e)

finally :
    
    if connection:  
        connection.close()
    else:
        print('에러나서 종료못함 ')
