# -*- coding: utf-8 -*-

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
def searchNewsByKeyword(arg):
  searchKeyword = arg#'한미정상회담'
  encText       = urllib.parse.quote( searchKeyword )
  url           = 'https://openapi.naver.com/v1/search/news.json'
  url           = f'{url}?query={encText}&display=20'
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
  titles = [ item["title"].replace('&quot;','').replace('<b>','').replace('</b>','') for item in tmp['items']]
  #print( titles )
  return titles

# 함수 호출
#searchNewsByKeyword('아마존')

res = searchNewsByKeyword('아마존')
print(res)

#미션 검색어를 바꾸면 새로운 결과가 나올것이다.
#현재코드는 검색어 한미정상회담, 아마존, 손흥민
#각각 검색어 별로 검색결과를 출력하려면 코드를 어떻게 변경해야 효율적인가
# 재사용성 함수 ? 
#여기가진운래 절차적 프로그래밍 함수화시키면 함수 지향성..
#함수시켜서 간결하게 표현
#함수는 서치키워드 부터 맨끝까지 함수로 만들기........
#함수 = 재사용성
# 함수는 내장함수와 외장함수 사용자 정의 함수

#def a()
#    daf b()
# 함수안에 함수... 고급방법... 클로우저/?/
# 함수를 써서 얻는 이득은
# 함수 = > 재사용성을 높이고, 코드를 간결하게 처리할수 있고, 모듈화를 할 수있고, 모듈화를통해 코드를 공유하여 제작가능
# xxx문 : 콜론다음은 들여쓰기다.
# 