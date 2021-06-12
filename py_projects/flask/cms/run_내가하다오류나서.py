'''
    - 서버측 코드 및 HTML 내부에서 URL을 하드코딩하지 않는다.
    - URL 변경시 하드코딩된 모든 부분을 다 교체해야 한다.
    - url_for()함수 사용해야함 == url_for('URL과 같이 세팅된 함수명') == 차후에 URL로 대체
        - URL이 변경되더라도 함수명은 안바뀐다는 전제를 가짐
    - url_for('home') == url_for('home')
'''

from flask import Flask, request, render_template, redirect, session, url_for


from db import selectUsers 




app = Flask(__name__)

app.secret_key = 'hash value'          
         

@app.route('/')
def home() :
 
    if not 'uid' in session :                     
        return redirect(url_for('login'))                   
 

    return render_template('index.html', title='랜더템플릿으로보냄')           
    # ㄴ 랜더링시 데이터를 키 = 값 형태로 자유롭게, 개수도 마음대로 해서 전달 가능 

@app.route('/logout')
def logout():
        if 'uid' in session :    
            session.pop('uid', None)             #로그아웃하면 아이디날리고       
        if 'uid' in session :    
            session.pop('name', None)            # 로그아웃하면 이름날리고
            return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])  
def login() :
    
    # 분기
    if request.method == 'GET' :                  
        return render_template('login-v2.html')   
    else :     
        uid = request.form.get('uid')       
        upw = request.form.get('upw')       
        print( uid, upw )

        row = selectUsers( uid, upw )
        

       
        if row :     
            session[ 'uid' ] = uid
            # 회원정보중 회원의 이름을 세션에 저장한다.
            session[ 'uid' ] = row [ 'name' ]
            

            
            return redirect(url_for('home'))     
        else :
          
           return 

    
if __name__ == '__main__' : 
    app.run( debug=True )