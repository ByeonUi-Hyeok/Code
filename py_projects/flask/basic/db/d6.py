import pymysql as my


# d6.py 목적
# 함수화, 기능 테스트

# 함수선언
def selectUsers ():             # 함수선언 == 함수명 == selectUsers 
    connection = None


    try :                    
        connection = my.connect( host       = 'localhost',     
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

        cursor.execute( sql, ('admin', '1') )  

        row = cursor.fetchone()
        print( row )    

    except Exception as e:
        print('접속오류', e)

    finally :
        
    
        if connection:  
            connection.close()
        else:
            print('에러나서 종료못함 ')

if __name__ == '__main__' : 
    app.run( debug=True )

# 기능 테스트
selectUsers()