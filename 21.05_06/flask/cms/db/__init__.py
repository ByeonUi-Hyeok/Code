import pymysql as my

# MVC 모델로 웹, M:모델/디비, V:뷰/화면/화면, C:비즈니스로직/커맨드
# d7은 쿼리만 수행하고, 결과만 돌려준다. 그 의미는 판단하지 않는다
# 함수화, 기능 테스트
# 회원이면 dict 형태로 전달(리턴)
# 회원아니면 None으로 전달(리턴)
def selectUsers( uid, upw ):
    row        = None # 쿼리 결과
    connection = None
    try:
        connection = my.connect(host       = 'localhost',
                                user       = 'root',     
                                password   = '1234',     
                                database   = 'python_db',                            
                                cursorclass= my.cursors.DictCursor                       
                                )     
        cursor = connection.cursor()    
        sql    = '''
            SELECT 
                * 
            FROM 
                users_tbl
            WHERE 
                uid=%s
            AND 
                upw=%s;
        '''    
        # %s => '값'
        cursor.execute( sql, ( uid, upw ) )    
        row = cursor.fetchone()       
        cursor.close()                # with문 안쓰면 꼭꺼야함
        #print( row )
    except Exception as e:
        print('접속오류', e)
    finally:
        if connection:
            connection.close()
        print('종료')
    # 결과 리턴
    return row


# 게시판 목록 가져오기
def selectBbs( pageNo=1, pageAmt=10 ): # 기본값을 지정해서 인자 선언안하면 기본값그대로 가져가게..
    '''
        selectBbs : 게시판 목록 가져오는 함수, news_tbl 테이블 조회
        pageNo    : 페이지 번호, 1, 2, 3등등. 기본값 1
        pageAmt   : 페이지당 몇개의 목록을 보여줄것인가. 기본값 10

    코멘트 설명적으려면 함수내 '''''' 이다.
    selectBbs : 게시판 목록 가져오는 함수, news_tbl 테이블조회
    pageNo : 게시판 번호 (1,2,3..) 기본값 1
    pageAmt : 
    
    일반문을 wtih문 별칭 받아줄때?
    with connection.cursor() as cursor : << 이런식으로쓰면 cursor만 쓰면된다.
    cursor.close() 위에함수에 넣어야함.'''
    rows       = None # 쿼리 결과
    connection = None
    try:
        connection = my.connect(host       = 'localhost',
                                user       = 'root',     
                                password   = '1234',     
                                database   = 'python_db',                            
                                cursorclass= my.cursors.DictCursor                       
                                )     
        with connection.cursor() as cursor:   
            # 경우에 따라서는 파라미터는 문자열 포멧팅으로 해결할수 있다
            sql    = f'SELECT * FROM news_tbl ORDER BY id DESC LIMIT { (pageNo-1)*pageAmt }, { pageAmt };'            
            cursor.execute( sql )    
            rows   = cursor.fetchall()
    except Exception as e:
        print('접속오류', e)
    finally:
        if connection:
            connection.close()
        print('종료')
    # 결과 리턴
    return rows

# 검색

def selectkeyword( keyword ): 
    '''
    selectkeyword : 검색어를 가지고 뉴스테이블에서 검색하여 결과를 가져오는 함수
    keyword : 키워드 
    '''

    rows       = None # 쿼리 결과
    connection = None
    try:
        connection = my.connect(host       = 'localhost',
                                user       = 'root',     
                                password   = '1234',     
                                database   = 'python_db',                            
                                cursorclass= my.cursors.DictCursor                       
                                )     
        with connection.cursor() as cursor:   

            sql    = f"SELECT * FROM news_tbl WHERE title LIKE '%{ keyword }%'"     
            cursor.execute( sql )    
            rows   = cursor.fetchall()
    except Exception as e:
        print('접속오류', e)
    finally:
        if connection:
            connection.close()
        print('종료')
    # 결과 리턴
    return rows



if __name__ == '__main__':
    # 회원 테스트 
    row = selectUsers( 'guest', '1' )
    print( '회원조회결과:', row )
    # 비회원 테스트 (회원이 아님, 비번이 틀림, 아이디 틀림)
    row = selectUsers( 'guest', '2' )
    print( '회원조회결과:', row )




