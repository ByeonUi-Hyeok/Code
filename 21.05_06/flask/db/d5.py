import pymysql as my

connection = None

try :                    
    connection = my.connect( host        = 'localhost',     
                             user        = 'root',          
                             password    = '1234',          
                             database    = 'python_db',
                             cursorclass = my.cursors.DictCursor ) 
    cursor = connection.cursor()
    sql   = '''
                SELECT
                        *
                FROM
                        users_tbl
                WHERE
                        uid = %s
                AND
                        upw = %s 
                        ''' 
                        # 코드의 문제점 == uid, upw가 하드코딩 되어있다.(고정되어있다.)
                        # sql에서 뽑아서 쿼리 수행시 인자로 전달되게 수정해야한다.

    cursor.execute( sql, ('admin', '1') )  # 쿼리를 수행할때 파라미터를 전달 할 수 있다.
                                           # 이 때 전달되는 값은 ''을 자동으로 붙여준다. 형식은 기본적으로 tuple 사용한다.
                                           # 위의 %s에 대응하는 것이고,
                                           # 기존의 코드로는 uid ='admin' // upw = '1' 이 같은 결과를 수행한다.
                                           # 코드 문제점 == 이 코드 역시 id pw 가 하드코딩되어있다. == 함수로 바꾸자. == d6.py


    row = cursor.fetchone()
    print( row )    

except Exception as e:
    print('접속오류', e)

finally :
    
    if connection:  
        connection.close()
    else:
        print('에러나서 종료못함 ')
