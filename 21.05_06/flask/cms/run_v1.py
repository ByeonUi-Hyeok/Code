# 세션 : 접속자 정보를 서버측에서 관리  // 서버측 메모리 사용, 자원리스크가 있음.
#         -- 데이터베이스 형태, NO-SQL형태로 서드파트제품(혹은 패키지)들을 사용하여 처리
#         -- 과정 : 세션 생성(로그인성공시) > 세션 체크(홈페이지, 세션을 가진자만 진입ok) > 세션 해제(로그아웃시)
# 쿠키 : 접속자의 브라우저에 정보를 저장하여 사용자를 특정하는 장치
#         -- 아이디 기억 / 기타 데이터 저장

from flask import Flask, request, render_template, redirect, session
#session < 사용자 정보를 서버측에 저장하겠다.

from db import selectUsers 
# 패키지 ==> __init__.py를 가르킨다.
# 그렇기때문에 db만적어도 끌어쓸수 잇나보당?
# 파이썬 3.3 이하에서는 패키지 사용시 필수, 현재는 옵션
#from은 내껏처럼 쓰는거고
        # ex == selectUsers() == 내장함수는이렇게쓰고

#import는 남의것처럼 ( xxx.(점)찍고사용해야함) ex: 
        # ex ==  별칭.selectUsers() == 외장함수는 이렇게쓴다.

app = Flask(__name__)
# 세션 관련 작업 - 세션키 저장
app.secret_key = '1234567890a'          # 원래 해시값 사용.
         

@app.route('/')
def home() :
    return render_template('index.html')  
# 이렇게 코드 실행하니 나오긴하지만 화면이 다깨져서나옴
# 크롬 기준 ctrl shift j 랑 i 눌리면 정보들 나옴
# ctrl shift j 누르면 오류목록나옴 404 == 페이지없음 
# index.html의 헤더태그를 연다
# 10라인 <link 태그의 http은 상관안해도됨
# 그러나 상대경로"plugin~~ 이런것은 맞춰줘야함
# 그래서 컨트롤f 보면 href="plugins/ 를 찾고
# 컨트롤 h로 href="static/ 로 바꾼다.
# 저장하고 새로고침후 아까 사이트로가서 컨 쉬 j 눌러서보면 오류가 줄어든것을 알수있다.
# 그래서 다시 찾아보니 href="dist/ 가있어 href="static/ 로바꾼 후 저장후 사이트를가보면 더 줄어들었다#
#여기까지 헤더 끝
#바디 태그열어서
#1478 라인 보면src="plugins/ 을 hresrc="static/plugins/
#1510 src="dist/ 을 src="static/dist 로바꾼다

#이렇게하면 전반적으로 맞는데 이미지가 문제다.
#오류 8개로줄엇다
# 그다음 .jpg 파일이문제니까 경로맞춰준다. static/

@app.route('/login', methods=['GET', 'POST'])  

def login() :
    
    # 분기
    if request.method == 'GET' :                  
        return render_template('login-v2.html')   
    else :     
        uid = request.form.get('uid')       
        upw = request.form.get('upw')       
        print( uid, upw )
        #2. 아이디 비번 가지고 데이터베이스에 쿼리를 수행 (사전에 이미 가입이 되어야 있어야 한다.)
        #3. 수행결과를 받는다.
        row = selectUsers( uid, upw )
        

        # if 조건식 :
        #     pass 
        # else :
        #     pass
        # 틀잡을때는 저렇게 일단 잡고

        if row :     # row 는 None 이나 딕셔너리로 온다
            #4. 회원이면 == 서비스 페이지 이동 == 리다이렉트 == 쓰려면 redirect 모듈 임포트해야함.
            return redirect('/')     # 127.0.0.1:5000/ 으로 이동한다.        
        else :
            #5. 회원 아니면 ==> 아이디 혹은 비번이 틀립니다.  ==> 회원가입 유도 재로그인 유도 == 로그인화면으로 리턴
           return '''
                        <script>
                            alert("로그인 실패. 다시시도하시오")  // 경고창
                            // 다시 이전페이지로 이동
                            history.back()            // JS코드 == 돌아간다는 코드
                        </script> '''

    
if __name__ == '__main__' : 
    app.run( debug=True )