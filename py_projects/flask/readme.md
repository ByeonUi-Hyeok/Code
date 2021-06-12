# 파이썬 기반 웹 프로그래밍

## 목적
     - 파이썬을 이용한 s/w개발 능력향상
     - 파이널 프로젝트의 산출물에 사용하는 기술
     - 모든 플랫폼에 사용되는 범용적인 웹 환경을 파이썬을 이용해서 개발

## 과목
     - 파이썬

     - 웹 서비스 구성요소 (포지션?)
        - 클라이언트 사이드
            - ***구성요소***
                - html5 : 구조, 콘텐츠, 뼈대역할
                - css3  : 디자인, 프레젠테이션, 레이아웃, css selector, 애니메이션, 반응형UI구성 등 인터렉티브
                    - 부트스트랩 기반 탬플릿들을 활용하여서 UI 구성
                - javascript(ECMA 2020, 브라우저마다 지원여부가 달라짐) 
                    - 이벤트 처리, ajax 처리, 통신처리, DOM 조작(화면 동적 구성)
                    - 사용자와 브라우저간의 인터렉션(상호작용) 담당
                    - jQuery 사용 (자바스크립트를 좀더 간결하게 사용, 프레임 웍)    
            - 최신 트렌드( 4~5년(2015~6)부터 진행되었던 부분)
                - 웹 서비스의 무게중심이 서버 ==> 클라이언트로 이동
                - SPA(Single Page Application)
                    - Anglar (구글)     : 가장 오래 되었음. TypeScript
                    - React  (페이스북) 
                        - 웹, 앱(react-native). TypeScript or JavaScript
                        - PC용 어플리케이션( + 일렉트론 )
                    - Vue    (커뮤니티) :
                        - 최근 급상승 , 웹
                        - PC용 어플리케이션


        - 서버 사이드
            - 웹 프로그래밍
            - 결과물
                - UI 있음( html전송, 일반적인 웹프로그래밍, 화면구성, 서버측 렌더링 )
                - UI 없음( 미들웨어, 업무만 수행 json/xml 전송 )
            - 개발도구
                - asp, servlet/jsp, php ( 199x년 후반 )
                - ejb ==> spring /(java진영 2000년대) 
                - nodejs, .net(닷넷)기반, 파이썬 웹 ... / ( 현재까지 )
                - 현재 nodejs(js), spring(java), 파이썬 웹(python), .net(닷넷)(c#)기반, php(php)
                - 파이썬 웹
                    - flask
                        - 자유도가 높다 / 대표 제품 : 주피터노트북
                        - 마이크로 에디션, nodejs와 유사함
                    - DJango
                        - 프레임웍(프레임웍의 규칙에 따라 개발) 기반
                        - spring과 유사함 


        - 데이터베이스
            - 데이터를 저장하는 저장소 
            - 기법?
               - RDBMS
                   - 관계형 데이터베이스
                       - 랭귀지(언어) : SQL
                   - light
                       - mysql
                       - ***maria-DB***
                   - enterprise(유료)
                       - 오로라(아마존)
                       - Oracle
                       - MS-SQL
                       - IBM .. 등
               - No-SQL
                   - 빅데이터의 출현으로 등장
                   - JSON 형태, 로그
                   - 실시간 데이터베이스
                       - 몽고디비, 하둡 ... 등
                       - Realm, Firebase(Google)의 실시간 데이터베이스

### 데이터베이스 테이블 생성
      - 회원 테이블
            CREATE TABLE `users_tbl` (
                `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT '내부관리ID',
                `uid` VARCHAR(64) NOT NULL COMMENT '회원ID' COLLATE 'utf8_general_ci',
                `upw` VARCHAR(64) NOT NULL COMMENT '회원PW' COLLATE 'utf8_general_ci',
                `name` VARCHAR(64) NOT NULL COMMENT '회원이름' COLLATE 'utf8_general_ci',
                `regdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP() COMMENT '가입일',
                PRIMARY KEY (`id`) USING BTREE,
                UNIQUE INDEX `uid` (`uid`) USING BTREE
            )
            COLLATE='utf8_general_ci'
            ENGINE=InnoDB
            ;

      - 회원 테이블 ( 회원가입)
            1.
            INSERT INTO `python_db`.`users_tbl` (`uid`, `upw`, `name`) VALUES ('guest', '1', '게스트');
            == INSERT INTO python_db.users_tbl (uid, upw, name) VALUES ('guest', '1', '게스트');
            `들어가는건 기존에 정의된 것 때문에 오류날까바 들어간거 안들어가도됨
            즉 위 두 코드는 같은내용이다

            2.
            INSERT INTO `python_db`.`users_tbl` (`uid`, `upw`, `name`) VALUES ('admin', '1', '관리자');
            == INSERT INTO python_db.users_tbl (uid, upw, name) VALUES ('admin', '1', '관리자');

      - 로그인 처리
             - SQl 쿼리 == DBA의 언어이다. 
             - SQL 쿼리의 주석에는, --(대쉬*2), #(샵) 두개가 있다.
             - CRUD
             - SQL문 : 데이터를 입력(insert)/수정(update)/삭제(delete) 함.        직접적으로 DB를 변경하는 파트가있고
             - SQL문 : 데이터 조회(무조건 select로시작함)                         DB내용을 변경하지 않고 조회만 하는 영역이있다
             - ID/PW 들어오면 이 정보를 가진 회원이 있는지 조회  == 로그인 쿼리

             - 모든 회원 정보를 가져오시오
                SELECT * FROM users_tbl;

             - 특정 uid/upw를 가진 고객정보를 가지오시오.
             -  == 특정 uid/upw와 일치하는 회원정보가 있다면(조건문) 가져오시오 (로그인 처리)
                 SELECT * FROM users_tbl           # user_tbl의 모든것(*)에서
                 WHERE uid='guest' AND upw='1';    # uid가 게스트이고(and) upw가 1인 것을 찾으시오            

      - 조회영역
            - SQl 쿼리 == DBA의 언어이다. 
            - SQL 쿼리의 주석에는, --(대쉬*2), #(샵) 두개가 있다.
            - CRUD
            - SQL문 : 데이터를 입력(insert)/수정(update)/삭제(delete) 함.        직접적으로 DB를 변경하는 파트가있고
            - SQL문 : 데이터 조회(무조건 select로시작함)                         DB내용을 변경하지 않고 조회만 하는 영역이있다
            - ID/PW 들어오면 이 정보를 가진 회원이 있는지 조회  == 로그인 쿼리

SELECT * FROM users_tbl;
             

## 개발환경 구축
    - python 설치
    - 필요한 패키지 설치
        - $pip install flask == conda install flask
        - $ == 프롬프트를 표현하는것
    - Visual Studio Code 설치
    - 구동 명령어
        - python *.py
        - 삼각형 시작버튼 클릭 or ctrl + F5
        - 구동결과
            * Serving Flask app "f2" (lazy loading)
            * Environment: production
              WARNING: This is a development server. Do not use it in a production deployment.
              Use a production WSGI server instead.
            * Debug mode: off
            * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


## 추가사항
    - 파이썬 연습용 자료
    - 플라스크 뒤쪽 고급내용
        - 블루프린트 통한 구조 고도화
        - 라이프 사이클을 통한 응답 처리 ( 세션처리 )
        - 채팅
        
    - 배포
        - AWS에서 배포하는 절차
           - febric 기술이용
           - 

