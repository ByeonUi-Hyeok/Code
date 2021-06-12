import pymysql as my


# d7.py 목적
# 회원이면 dict형태로 전달
# 비회원이면 None으로 전달

# d7이면 쿼리만 수행하고 결과만 돌려준다 / 그 의미는 판단하지않는다 == 그의미는 f6가 판단한다.
# MVC 모델로 웹, M:모델/디비, V:뷰/화면/화면, C:비즈니스로직/커맨드

# 함수선언
def selectUsers ( uid, upw ):             # 함수 입력받는 인자를 uid upw로 선언 
    row        = None              # 쿼리결과 == 초기값 =None 부여
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

        cursor.execute( sql, (uid, upw) )  

        row = cursor.fetchone()
        # print( row )    

    except Exception as e:
        print('접속오류', e)

    finally :
        
    
        if connection:  
            connection.close()
        else:
            print('에러나서 종료못함 ')
    return row

if __name__ == '__main__' : 
    
    # 회원 테스트
    row = selectUsers('guest', '1')
    print( '회원조회결과:', row )

    # 비회원 테스트(회원이 아님, 비번이 틀림, 아이디 틀림 등)
    row = selectUsers('guest2', '1')
    print( '회원조회결과:', row )


# 기능 테스트
# selectUsers()
