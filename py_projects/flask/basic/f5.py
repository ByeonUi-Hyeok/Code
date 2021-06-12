'''
상황1.클라이언트가 서버측에 페이지를 요청할때(브라우저에 주소치고 엔터치고) 데이터를 전달하고 싶다.
   - method(메소드) 방식은  == Get방식 사용
       - 데이터를 전달하지 않아도 일반적인 모든 페이지는 GET 방식으로 페이지를 요청한다
       - == DEFAULT 값 == GET == 아무런 표시도 없으면 모두다 GET 
       - 다른방식으로 (EX:POST, PUT, HEAD. DELETE 등) 메소드 방식을 사용하고 싶으면 무조건 명시적으로 표시해야함.
       - 형식
           - 주소형식 == 주소(URL) 뒤에 ?키=값&키=값 ( 모든 웹 프로그램 공통의 룰/문법/약속 )
       - 클라이언트가 서버측으로 데이터를 전달할 때 어떤 방식이건 간에 무조건 request라는 객체를 타고 서버에 전달된다.
           - 정보를 구하려면 request 를 구해라
'''

from flask import Flask, request
# from flask import Flask
# from flask import request
# flask/Flask와 flask/request 임포트 

# 기본 홈화면 127.0.0.1:5000
app = Flask(__name__)
@app.route('/')
def home() :
    return '<h1>127.0.0.1 포트 5000</h1>'

# 로그인 페이지 127.0.0.1:5000/login
# 데이터를 전달 할것이다. 그 방식(형식)은 아래와 같을것이다.
# 127.0.0.1:5000/login?uid=guest&name=게스트 
# uid=guest&name=게스트 입력 / 키=값&키=값

'''
@app.route('/login')                           
def login() :
    # step 1. 클라이언트가 보낸 데이터를 추출
    uid  = request.args.get('uid' )           # uid=guest&name=게스트 에서 uid의 value값 guest 추출
    name = request.args.get('name')           # uid=guest&name=게스트 에서 name의 value값 게스트 추출
    return f'<h1> 로그인페이지\n\r id = {uid} name = {name} </h1>' # 
    # 그러나 클라이언트가 데이터를 보내지 않았다면 none값으로 출력한다.
    # 값을 검사해서 none값이면 오지 못하게 해야한다.
    # 둘 중 한개라도 값이없다면
'''

@app.route('/login')                           
def login() :
    # step 1. 클라이언트가 보낸 데이터를 추출
    uid  = request.args.get('uid' )           # uid=guest&name=게스트 에서 uid의 value값 guest 추출
    name = request.args.get('name')           # uid=guest&name=게스트 에서 name의 value값 게스트 추출
    print(uid, name)                          # print는 터미널로 출력  // return은 클라이언트 브라우저로 출력
    # 클라이언트가 데이터를 안보냈다 -> 값 검사 => 둘 중 한개라도 값이 없다면
    #(uid != None and name != None) == (uid == None or name == None) == (not uid or not name)
    if not uid or not name:   # 부정상황을 잡는 조건식 / not 변수는 값이 있으면 =True / 없으면 False
        return '''
            <script>
                alert("아이디나 이름이 누락되었습니다.")
            </script>
        '''


    else: # 정상값 
        return f'<h1> 로그인페이지\n\r id = {uid} name = {name} </h1>' 


if __name__ == '__main__' : 
    app.run( debug=True )