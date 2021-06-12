# -*- coding: utf-8 -*-

import os
import sys
import urllib.request

def 태그삭제( oriTxt ) : 
  return oriTxt.replace('&quot;','').replace('<b>','').replace('</b>','')

CLIENT_ID     = 'quAs4Y6uHPoWLrrwpi0W'
CLIENT_SECRET = 'vqVSw4zlV3'

# 함수 정의
def searchNewsByKeyword(arg):
  searchKeyword = arg#'한미정상회담'
  encText       = urllib.parse.quote( searchKeyword )
  url           = 'https://openapi.naver.com/v1/search/news.json'
  url           = f'{url}?query={encText}&display=5'           #display = 20개 설정한거 디폴트 10 5개로변경했음
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

  return [ {
      "title"         : 태그삭제(item['title']),
      "originallink"  : item['originallink'],
      "link"          : item['link'],
      "description"   : 태그삭제(item['description']),
      "pubDate"       : item['pubDate'],
  } for item in tmp['items'] ]



res = searchNewsByKeyword('아마존')


# [ { } ] dataFrame으로 변경
import pandas as pd

df = pd.DataFrame.from_dict( res )

import pymysql

from sqlalchemy import create_engine

import pandas.io.sql as pSql

id       = 'root'        #접속 id
pw       = '1234'        #접속 pw
host     = 'localhost'   #localhost 127.0.0.1
port     = '3306'        #접속 포트
database = 'python_db'   #데이터베이스 명
db_url   = f'mysql+pymysql://{id}:{pw}@{host}:{port}/{database}'        

# 2. 연결 엔진 생성
engine = create_engine( db_url, encoding = 'utf8' )           #아까 불러온 함수

# 3. 실제 db에 연결
conn = engine.connect()
# 구글 드라이브기때문에 오류


df.to_sqldf.to_sql( name='news_tbl', con=conn, if_exists='append', index=False  )

conn.close()