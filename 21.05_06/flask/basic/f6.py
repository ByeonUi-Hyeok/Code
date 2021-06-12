'''
상황1.클라이언트가 서버측에 페이지를 요청할때(브라우저에 주소치고 엔터치고) 데이터를 전달하고 싶다.
   - method(메소드) 방식은  == POST방식 사용
       - 데이터를 숨겨서 서버로 전달한다.
       - 보안에 우수, 대량의 데이터 전송 가능 

'''

from flask import Flask, request, render_template
# from flask import Flask
# from flask import request
# from flask import render_template
#    - render_template API 소개
#        - render_template( 'xx.html' )
#        - html은 디자이너가 작업하는 내용이다. 웹 프로그래밍 영역에서 분리해서 관리한다.
#        - 위의 용도로 도입이 되었고, py 파일이 커지는 부분 방지, html은 py 파일 입장에서는 리소스일뿐이다.
#            - html이 바뀐다고 서버를 재가동 할 것인가?
#            - 위의 이유로 분리해야 하고 이를 지원하는 것이 render_template이다
#        - html을 읽어서 추가된 데이터가 있다면 버무려서 최종 html으로 생성하여 응답한다.(정확히 응답은 return이하고 그 재료를 얘가만듦)
#        - 서버 사이드 랜더링을 수행하기 위한 필수 조건 == 탬플릿 엔진이 필요
#            - 탬플릿엔진으로 JinJa(신사)를 사용한다. == flask를 설치하면 JinJa가 자동으로 같이 설치된다.
#               - 템플릿엔진 == html을 해석하고, 데이터를 버무려서 동적으로 다시 html 생성하는 도구
#        - /templates
#           ㄴ login.html( templates 하위에)
# flask/Flask, flask/request, flask/render_template 임포트 

# f6.py에서 ./db/d6.py를 가져와서 d6.py에 정의된 selectUsers()를 사용하고자 한다.
'''
형식
from 패키지. 패키지..... 모듈 import 변수, 함수, 클래스, *
from 패키지. 패키지..... 패키지 import 변수, 함수, 클래스, *
import 패키지. 패키지..... 모듈 as 별칭
import 패키지. 패키지..... 패키지 as 별칭
패키지 == 디렉토리(db)
모듈 == 파일(d6.py)
별칭.함수()
from은 내껏처럼 쓰는거고
        # ex == selectUsers() == 내장함수는이렇게쓰고

import는 남의것처럼 ( xxx.(점)찍고사용해야함) ex: 
        # ex ==  별칭.selectUsers() == 외장함수는 이렇게쓴다.
 
from은 실행되고있는 파일기준 같은 폴더 내에 있어야함.
(즉 f6와 db는 같은 디렉터리(basic)내에 있기때문에 )
from db.d6 import selectUsers 
== 같은 디렉터리 내에있는 db(패키지==디렉터리).모듈(파일==d6.py) import 함수(d6에서 정의된 selectUsers 함수)
내가 xx.py를 구동하는 곳이 entry포인트이다.
그곳에서 import 경로를 따진다.
d6는 다른 폴더 내에 있으므로
db폴더를 f6와 같은 basic 폴더로 옮겨야 사용 가능하다.
''' 
from db.d7 import selectUsers 
# 이렇게 임포트만 해도 바로 함수가 실행되버림
# from 패키지.도뮬 improt 함수 형태임
# from 패키지 import 함수

 # db/__init.py에서
 # from db import selectUsers
 #패키지 ==> __init__.py를 가르킨다.?
 #파이썬 3.3 이하에서는 패키지 사용시 필수, 현재는 옵션

'''
if __name__ == '__main__' : 
    app.run( debug=True )

그렇기 때문에 d6에다가 내가 실행했을때만 실행되게 위의 코드를 추가하면 임포트해도 바로실행되지 않는다.
'''



# 기본 홈화면 127.0.0.1:5000
app = Flask(__name__)
@app.route('/')
def home() :
    return '<h1>127.0.0.1 포트 5000</h1>'

'''
@app.route('/login')
def login() :
    return render_template( 'login.html' )

위와같은 코드로 실행하면 에러 발생함.
결과 : jinja2.exceptions.TemplateNotFound: login.html
원인1. login.html을 만들지 않음
원인2. 적절한 곳에 login.html을 놓아야한다.
해결1. templates 하위에 빈 login.html만 만들어도 오류는 안뜨네..
/templates
ㄴ login.html( templates 하위에)
 위의 login.html은 클라이언트 사이드이다.
 결국 login.html을 코딩한다는 것은 클라이언트 사이드 코딩한다는 것이다.
 login.html 파일을 수정해도 basic밑에 서버 터미널이 반응하지않는다. 
 == 서버쪽 수정해야 서버터미널이 반응한다. 결국 login.html는 클라이언트 사이드다
'''    
'''
@app.route('/login')
def login() :
    return render_template( 'login.html' )

if __name__ == '__main__' : 
    app.run( debug=True )
# 현재는 GET만 허가되었다.
# POST까지 허가 요청한다면 == 추가코드 필요
# 404 Not Found(해당페이지는 없다) 표시가 뜨면 주소가 틀렸거나 정의되지 않았을때 뜬다.

'''
# @app.route('/login')                          # 아무것도 안적음(DEFAULT = GET) GET만 허가한 방식
@app.route('/login', methods=['GET', 'POST'])  #== methods 에 get과 post를 허가했기에 둘다 허가함
                                               # 해당 url이 어떤 방식으로 오는 것을 허가할지 결정할 때 사용

def login() :
    # 하나의 URL에서 GET방식과 POST방식을 모두 자원하고 싶다. == resful 방식 : URL을 최소로 사용할 수 있다.
    
    # 분기
    if request.method == 'GET' :                   # 모든 요청은 request를 타고온다 그렇기에 requst.method를 get과 비교해서 맞으면
                                                # 얘는 아까 뽑을때 args인가씀
        return render_template( 'login.html')   
    else :     # get이 아닌 모든방식 == 여기서는 POST
        
        #해야할 것
        #1. 전달된 데이터 추출 : ID, pw 추출
        uid = request.form.get('uid')        # 아까 html에서 form태그 전송했기때문에 from uid는 거기 input 옵션을 uid로 지정해서 보냈음
        upw = request.form.get('upw')        # 아까 html에서 form태그 전송했기때문에 from uid는 거기 input 옵션을 upw로 지정해서 보냈음
        print( uid, upw )
        # print는 서버 프롬프트에만 응답.
        # 그렇기 때문에 클라이언트에서 아이디 비번 입력하면 터미널에만 출력하고 클라이언트에는 무응답.(리턴을 안짯기때문)
        return 'post 방식으로 서버에 잘 전달 됐음' # 이건 클라이언트에만 응답됨


        #2. 아이디 비번 가지고 데이터베이스에 쿼리를 수행 (사전에 이미 가입이 되어야 있어야 한다.)
        #   == d1 ~
        #3. 수행결과를 받는다.
        #4. 회원이면 == 서비스 페이지 이동
        #5. 회원 아니면 ==> 아이디 혹은 비번이 틀립니다.  ==> 회원가입 유도 재로그인 유도
        
        








if __name__ == '__main__' : 
    app.run( debug=True )