# -*- coding: utf-8 -*-

# 문자열에서 가비지 제거하는 함수(<br>,...)
def removeTag( oriTxt ):
  return oriTxt.replace('&quot;','').replace('<b>','').replace('</b>','')

import os
import sys
import urllib.request

# 검색어를 바꾸면 새로운 결과가 나올것이다 
# 현재 코드는 검색어 한미정상회담, 아마존, 손홍민,.. 가 늘어간다 
# 각각 검색어별로 검색결과를 출력할려면 코드를 어떻게 변경 해야 효율적인가?
# 함수화 시켜서 간결하게 표현하시오!!
# 함수 => 재사용성을 높이고, 코드를 간격하게 처리, 모듈화, 코드를 공유하여 제작

CLIENT_ID     = 'quAs4Y6uHPoWLrrwpi0W'
CLIENT_SECRET = 'vqVSw4zlV3'

# 함수 정의
def searchNewsByKeyword( arg ):
  searchKeyword = arg#'한미정상회담'
  encText       = urllib.parse.quote( searchKeyword )
  url           = 'https://openapi.naver.com/v1/search/news.json'
  url           = f'{url}?query={encText}&display=5'
  request       = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id",CLIENT_ID)
  request.add_header("X-Naver-Client-Secret",CLIENT_SECRET)
  response      = urllib.request.urlopen(request)
  import json
  rescode       = response.getcode()
  if(rescode==200):
    tmp = json.load( response )
  else:
    print("Error Code:" + rescode)
  # titles = [ 
  #   item["title"].replace('&quot;','').replace('<b>','').replace('</b>','')
  #   for item in tmp['items']
  # ]
  # print( titles )
  # return titles

  # 데이터를 재구성하여 리턴한다. 구조는 동일하지만, 
  # <br>등등제거해야한다

  # 리스트 내포를 이용하여, 결과를 바로 생성한다
  return [ {
    "title"       : removeTag( item["title"] ),
    "originallink": item["originallink"],
    "link"        : item["link"],
    "description" : removeTag( item["description"] ),
    "pubDate"     : item["pubDate"],
  } for item in tmp['items'] ]

# 함수 호출
res = searchNewsByKeyword( '아마존' )


"""# 데이터 적제를 위한 형식(타입) 변경

- 수집한 데이터를 DB에 적제시키기 위해서 형태를 다음과 같이 만든다
  - [ { 키:값, ... },..   ]
  - 응답 데이터중에 items 항목을 그대로 사용하겠다, 단 태그나 &..된 기호는 제거하겟다
  - 위의 데이터를 pandas의 DataFrame으로 변형한후 DB에 입력한다 (룰, 절차)
"""

# [ {} ] => DataFrame으로 변경
import pandas as pd

df = pd.DataFrame.from_dict( res )


# 파이썬에서 마리아디비를 엑세스 하는 모듈
import pymysql
# 대량으로 데이터를 디비에 편하게 밀어 넣고 싶다 -> 고차원모듈이필요
from sqlalchemy import create_engine
# DataFrame에서 DB에 sql(데이터베이스 언어)를 전송하는 기능
# DataFrame를 Db에 밀어넣는 기능
import pandas.io.sql as pSql

# 1. 디비 연결 문자열 생성
id       = 'root'
pw       = '1234'
host     = 'localhost'
port     = '3306'
database = 'python_db'
db_url   = f'mysql+pymysql://{id}:{pw}@{host}:{port}/{database}'

# 2. 연결 엔진 생성
engine = create_engine( db_url, encoding='utf8' )

# 3. 실제 데이터베이스에 연결
conn = engine.connect()

# 4. 데이터 입력
'''
name : 테이블명
con  : 디비와 연결됭 세션
if_exists='append' : 이미 테이블이 존재한다면 데이터를 누적해라
'''
df.to_sql( name='news_tbl', con=conn, 
           if_exists='append', index=False  )

# 5. 연결했으면 연결종료 => I/O을 수행하면 받드시 닫는다
conn.close()