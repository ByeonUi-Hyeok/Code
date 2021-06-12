-- 게시판 기본 데이터 로드 -- 
SELECT * FROM news_tbl;  -- news_tbl에(from nuews_tbl) 존재하는 모든 데이터(*)를 가져오시요(select)

-- 최신순으로 가져오시오

SELECT * FROM news_tbl ORDER BY id DESC; -- id 컬럼을 기준으로 최신순으로(숫자높은게 최신) desc==내림차순

-- 한페이지에 10개만 보일 것이다.
-- 최신순으로 가져오되 10개만 가져오시오

SELECT * FROM news_tbl ORDER BY id DESC limit 0, 10;
SELECT * FROM news_tbl ORDER BY id DESC limit 10;
-- 위 두 코드는 같음
-- 그 다음 패이지는 ? 페이지번호-1 * 페이지의 양

SELECT * FROM news_tbl ORDER BY id asc LIMIT 10, 10;
-- limit 10 부터 10개



-- 검색쿼리
SELECT * FROM news_tbl WHERE title LIKE '%BTS%';