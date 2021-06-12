

from flask import Flask, request, render_template, redirect

from db import selectUsers 
# 패키지 ==> __init__.py를 가르킨다.
# 그렇기때문에 db만적어도 끌어쓸수 잇나보당?
# 파이썬 3.3 이하에서는 패키지 사용시 필수, 현재는 옵션
#from은 내껏처럼 쓰는거고
        # ex == selectUsers() == 내장함수는이렇게쓰고

#import는 남의것처럼 ( xxx.(점)찍고사용해야함) ex: 
        # ex ==  별칭.selectUsers() == 외장함수는 이렇게쓴다.

app = Flask(__name__)
@app.route('/')
def home() :
    return '<h1>홈페이지 (로그인에 성공하셨습니다.)</h1>'


@app.route('/login', methods=['GET', 'POST'])  

def login() :
    
    # 분기
    if request.method == 'GET' :                  
        return render_template( 'login.html')   
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