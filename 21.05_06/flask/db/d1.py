# 파이썬에서 mysql계열의 DB를 엑세스 하여서 쿼리를 수행하는 모듈을 준비한다.
# 최종 산출물 == uid, upw를 입력받아서 쿼리를 수행하고 그 결과를 돌려주는(리턴) 함수
# 디비를 연결하고 해제하는 부분은 통상 풀링, ORM 방식으로 처리(동시접속) == 고급 설정 부분
# 위의 고급설정 부분을 하는 것이 정석인데, 여기서는 심플하게 함수내에서 모두 해결하겠다.

# 설치
# pip install pymysql
# https://pypi.org/project
# 에서 pymysql 검색
import pymysql as my

# 1. 데이터 베이스 접속 정보 구성 및 접속
# Connect to the database
connection = my.connect( host        = 'localhost',     # 데이터베이스의 주소 == localhost == 127.0.0.1
                         user        = 'root',          # 데이터베이스 접속할 때의 사용자 계정명
                         password    = '1234',          # 사용자 계정의 비밀번호
                         database    = 'python_db',     # 데이터베이스 명
                         #port       = 3306,            # 포트는 3306 / 기본포트 3360이기때문에 명시하지않아도 defualt 값됨.
                         )
                         #cursorclass = pymysql.cursors.DictCursor

# 2. 접속 종료
connection.close()

