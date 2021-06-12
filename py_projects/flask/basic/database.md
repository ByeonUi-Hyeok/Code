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