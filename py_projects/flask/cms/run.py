'''
    - 서버측 코드, html 내부에서 URL을 하드코딩하지 않는다
    - url 변경시 하드코딩된 모든 부분을 다 교체해야 한다        
    - url_for('url와 같이 세팅된 함수명') => 차후에 URL로 대체        
        - url이 변경되더라도, 함수명은 않바뀐다 (전제)
    - url_for('home') => url_for('home')
    jsonify  =제이슨 응답하게하는함수
'''
# from cms.db import selectBbs
# from cms.db import selectkeyword
from flask import Flask, request, render_template, redirect, session, url_for, jsonify
import db

app = Flask(__name__)
app.secret_key = 'sdfgwegwed25rtetzrxfgrt'

@app.route('/')
def home():   
    if not 'uid' in session:
        return redirect(url_for('login'))
    # 렌더링시 데이터를 키=값 형태로 자유롭게, 개수도 마음대로 해서 전달가능
    return render_template( 'index.html', title='AI-2' )

@app.route('/logout')
def logout():    
    if 'uid' in session:
        session.pop('uid', None)    
    if 'name' in session:
        session.pop('name', None)    
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template( 'login-v2.html' )
    else:
        uid = request.form.get('uid')
        upw = request.form.get('upw')        
        row = db.selectUsers( uid, upw )        
        if row:            
            session['uid'] = uid
            # 회원정보중 회원의 이름을 세션에 저장한다
            session['name'] = row['name']
            return redirect(url_for('home'))
        else:            
            return '''
                <script>
                    // 경고창
                    alert("로그인 실패. 다시 시도하세요")
                    // 이전페이지로 이동
                    history.back()
                </script>
            '''

# 게시판페이지
@app.route('/bbs')
def bbs():
    return render_template('bbs.html', bbs=db.selectBbs(), title='AI-2' )

# 검색
@app.route('/search')
def search():
    # 검색어 획득
    keyword = request.args.get( 'q' )
    # 쿼리결과획득
    rows = db.selectkeyword( keyword )
    
    if not rows :
        rows = [] # 결과없음을 json으로 바꿀수있는 구조로 변경( 빈 리스트)
    
    # 응답 > json이 응답해야한다
    return jsonify( rows )

if __name__ == '__main__':
    app.run( debug=True )