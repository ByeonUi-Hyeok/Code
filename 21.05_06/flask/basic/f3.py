'''
    - 라우트 추가
        - 라우팅 처리를 수행하는 함수의 이름은 고유해야 한다(중복x)
        - 같은 URL이 중복되게 정의 되어 있다면 먼저 정의된 라우트 함수가 처리된다
        - 프로젝트 초기에 스토리보드가 완성되고 페이지가 정의되면 각페이지에 해당하는 url을 정의하고 각 페이지를 기본적으로 구성한다.
    - url 이해
'''

from flask import Flask

app = Flask(__name__)


# http://127.0.0.1:5000/
@app.route('/')
def home() :
    return '<h1> True </h1>'            

'''
@app.route('/')                                라우팅 처리를 수행하는 함수의 이름은 고유해야한다. 
def home() :                                   위에도 함수주소 home이 있다
    return '<h1>홈페이지1128</h1>'             같은 함수이름를 2개 넣으면 아래와같이 에러가난다
                                              AssertionError: View function mapping is overwriting an existing endpoint function: home  

@app.route('/')
def test1() :
    return '<h1> False </h1>'               # 그러나 같은 내용이라도 함수의 이름의 이름이 다르면서버는 구동된다.
                                            # 그러나 라우팅 주소가 같다.
                                            # 이렇게 주소가 같은 (URL이 중복되게 정의되어 있다면) 먼저 정의된 라우트 함수가 적용된다.  
                                            # 그러나 에러는 나지 않음 주소가같다고해서
처음 구성할때는 이렇게 페이지부터 쭉 만들고 시작한다.
'''

# http://127.0.0.1:5000/users/login
@app.route('/users/login')
def login() :
    return '<h1> 로그인페이지 </h1>'

# http://127.0.0.1:5000/main/service
@app.route('/main/service')
def service() :
    return '<h1> 서비스 메인 페이지 </h1>'

if __name__ == '__main__' : 
    app.run( debug=True )


