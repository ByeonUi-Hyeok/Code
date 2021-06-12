-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.5.10-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- python_db 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `python_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `python_db`;

-- 테이블 python_db.news_tbl 구조 내보내기
CREATE TABLE IF NOT EXISTS `news_tbl` (
  `title` text DEFAULT NULL,
  `originallink` text DEFAULT NULL,
  `link` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `pubDate` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 python_db.news_tbl:~40 rows (대략적) 내보내기
/*!40000 ALTER TABLE `news_tbl` DISABLE KEYS */;
INSERT INTO `news_tbl` (`title`, `originallink`, `link`, `description`, `pubDate`) VALUES
	('[Who Is ?] 김영문 한국동서발전 사장', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', ' (2019/04/14, 한국경제 인터뷰에서 한진그룹 총수 일가의 밀수 혐의 등을 조사한 결과를 이야기하며) 장기적으로 우리나라도 알리바바나 아마존 같은 전자상거래 플랫폼을 만들 수 있다면 좋겠지만 당장은 전자상거래... ', 'Fri, 28 May 2021 10:26:00 +0900'),
	('아마존 데이터를 현지 시장조사에 활용하라', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', '◇아마존, 시장조사에 어떻게 활용할까 = 이날 세미나에서 발표를 맡은 김성수 케이존 대표는 미국 등 해외 시장에 진출할 때 데이터를 바탕으로 시장조사를 하는 것이 중요한데, 가장 효율적인 방법 중 하나가 아마존을... ', 'Fri, 28 May 2021 10:24:00 +0900'),
	('네이버클라우드, 단종 앞둔 센트OS 대안 록키리눅스와 협력', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', '록키리눅스는  클라우드 서비스 공급자(CSP)로는 네이버클라우드와 아마존웹서비스(AWS)와 협력을 진행하고 있다. ​록키 리눅스 정식 배포는 6월 말~7월 중순경 이뤄질 예정으로, 네이버클라우드는 한국 이용자... ', 'Fri, 28 May 2021 10:20:00 +0900'),
	('[월가 분석] 캐시우드 ETF 내 유망 종목', 'https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202105280010&t=NNv', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=104&oid=215&aid=0000960953', '분석가들은 올해 들어 횡보하던 아마존(AMZN)이 반등할 거라고 봤습니다. 매출이 44% 급증한 회사 실적 발표에 힘입어 앞으로 1년 내 30% 이상 랠리를 예상했습니다. 이 외에도 클라우드 기반 커뮤니테이션 플랫폼... ', 'Fri, 28 May 2021 10:16:00 +0900'),
	('\'안티팬\' 최수영, 전 직장 선배 유서진과 팽팽한 신경전! 예고된 자존심 싸움', 'http://www.marketnews.co.kr/news/articleView.html?idxno=63416', 'http://www.marketnews.co.kr/news/articleView.html?idxno=63416', '30분 분량으로 금요일 2회, 토요일 2회씩 네이버TV와 V-LIVE에서 방송된다. 글로벌 플랫폼 iQIYI(아이치이), VIKI(비키), 일본 아마존 프라임 비디오(Amazon Prime Video JP)에서는 한 회에 60분 분량으로 매주 금, 토요일 동시 공개된다.', 'Fri, 28 May 2021 10:16:00 +0900'),
	('[글로벌 블록체인] 5월 28일 오전 뉴스 브리핑', 'http://www.newspim.com/news/view/20210528000291', 'http://www.newspim.com/news/view/20210528000291', '또 그는 이날 지금 비트코인 및 암호화폐를 거부하는 것은 아마존이 1990년대 초 전자상거래를 처음 시작했을 때 인터넷 사업 모델을 받아들이지 않는 것과 비슷하다. 암호화폐는 \'돈의 자유\'를 제공하기 위해 존재한다... ', 'Fri, 28 May 2021 10:31:00 +0900'),
	('[Who Is ?] 김영문 한국동서발전 사장', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', ' (2019/04/14, 한국경제 인터뷰에서 한진그룹 총수 일가의 밀수 혐의 등을 조사한 결과를 이야기하며) 장기적으로 우리나라도 알리바바나 아마존 같은 전자상거래 플랫폼을 만들 수 있다면 좋겠지만 당장은 전자상거래... ', 'Fri, 28 May 2021 10:26:00 +0900'),
	('아마존 데이터를 현지 시장조사에 활용하라', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', '◇아마존, 시장조사에 어떻게 활용할까 = 이날 세미나에서 발표를 맡은 김성수 케이존 대표는 미국 등 해외 시장에 진출할 때 데이터를 바탕으로 시장조사를 하는 것이 중요한데, 가장 효율적인 방법 중 하나가 아마존을... ', 'Fri, 28 May 2021 10:24:00 +0900'),
	('네이버클라우드, 단종 앞둔 센트OS 대안 록키리눅스와 협력', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', '록키리눅스는  클라우드 서비스 공급자(CSP)로는 네이버클라우드와 아마존웹서비스(AWS)와 협력을 진행하고 있다. ​록키 리눅스 정식 배포는 6월 말~7월 중순경 이뤄질 예정으로, 네이버클라우드는 한국 이용자... ', 'Fri, 28 May 2021 10:20:00 +0900'),
	('[월가 분석] 캐시우드 ETF 내 유망 종목', 'https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202105280010&t=NNv', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=104&oid=215&aid=0000960953', '분석가들은 올해 들어 횡보하던 아마존(AMZN)이 반등할 거라고 봤습니다. 매출이 44% 급증한 회사 실적 발표에 힘입어 앞으로 1년 내 30% 이상 랠리를 예상했습니다. 이 외에도 클라우드 기반 커뮤니테이션 플랫폼... ', 'Fri, 28 May 2021 10:16:00 +0900'),
	('[글로벌 블록체인] 5월 28일 오전 뉴스 브리핑', 'http://www.newspim.com/news/view/20210528000291', 'http://www.newspim.com/news/view/20210528000291', '또 그는 이날 지금 비트코인 및 암호화폐를 거부하는 것은 아마존이 1990년대 초 전자상거래를 처음 시작했을 때 인터넷 사업 모델을 받아들이지 않는 것과 비슷하다. 암호화폐는 \'돈의 자유\'를 제공하기 위해 존재한다... ', 'Fri, 28 May 2021 10:31:00 +0900'),
	('[Who Is ?] 김영문 한국동서발전 사장', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', ' (2019/04/14, 한국경제 인터뷰에서 한진그룹 총수 일가의 밀수 혐의 등을 조사한 결과를 이야기하며) 장기적으로 우리나라도 알리바바나 아마존 같은 전자상거래 플랫폼을 만들 수 있다면 좋겠지만 당장은 전자상거래... ', 'Fri, 28 May 2021 10:26:00 +0900'),
	('아마존 데이터를 현지 시장조사에 활용하라', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', '◇아마존, 시장조사에 어떻게 활용할까 = 이날 세미나에서 발표를 맡은 김성수 케이존 대표는 미국 등 해외 시장에 진출할 때 데이터를 바탕으로 시장조사를 하는 것이 중요한데, 가장 효율적인 방법 중 하나가 아마존을... ', 'Fri, 28 May 2021 10:24:00 +0900'),
	('네이버클라우드, 단종 앞둔 센트OS 대안 록키리눅스와 협력', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', '록키리눅스는  클라우드 서비스 공급자(CSP)로는 네이버클라우드와 아마존웹서비스(AWS)와 협력을 진행하고 있다. ​록키 리눅스 정식 배포는 6월 말~7월 중순경 이뤄질 예정으로, 네이버클라우드는 한국 이용자... ', 'Fri, 28 May 2021 10:20:00 +0900'),
	('\'안티팬\' 최수영, 전 직장 선배 유서진과 팽팽한 신경전! 예고된 자존심 싸움', 'http://www.marketnews.co.kr/news/articleView.html?idxno=63416', 'http://www.marketnews.co.kr/news/articleView.html?idxno=63416', '30분 분량으로 금요일 2회, 토요일 2회씩 네이버TV와 V-LIVE에서 방송된다. 글로벌 플랫폼 iQIYI(아이치이), VIKI(비키), 일본 아마존 프라임 비디오(Amazon Prime Video JP)에서는 한 회에 60분 분량으로 매주 금, 토요일 동시 공개된다.', 'Fri, 28 May 2021 10:16:00 +0900'),
	('[글로벌 블록체인] 5월 28일 오전 뉴스 브리핑', 'http://www.newspim.com/news/view/20210528000291', 'http://www.newspim.com/news/view/20210528000291', '또 그는 이날 지금 비트코인 및 암호화폐를 거부하는 것은 아마존이 1990년대 초 전자상거래를 처음 시작했을 때 인터넷 사업 모델을 받아들이지 않는 것과 비슷하다. 암호화폐는 \'돈의 자유\'를 제공하기 위해 존재한다... ', 'Fri, 28 May 2021 10:31:00 +0900'),
	('[Who Is ?] 김영문 한국동서발전 사장', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', ' (2019/04/14, 한국경제 인터뷰에서 한진그룹 총수 일가의 밀수 혐의 등을 조사한 결과를 이야기하며) 장기적으로 우리나라도 알리바바나 아마존 같은 전자상거래 플랫폼을 만들 수 있다면 좋겠지만 당장은 전자상거래... ', 'Fri, 28 May 2021 10:26:00 +0900'),
	('아마존 데이터를 현지 시장조사에 활용하라', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', '◇아마존, 시장조사에 어떻게 활용할까 = 이날 세미나에서 발표를 맡은 김성수 케이존 대표는 미국 등 해외 시장에 진출할 때 데이터를 바탕으로 시장조사를 하는 것이 중요한데, 가장 효율적인 방법 중 하나가 아마존을... ', 'Fri, 28 May 2021 10:24:00 +0900'),
	('네이버클라우드, 단종 앞둔 센트OS 대안 록키리눅스와 협력', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', '록키리눅스는  클라우드 서비스 공급자(CSP)로는 네이버클라우드와 아마존웹서비스(AWS)와 협력을 진행하고 있다. ​록키 리눅스 정식 배포는 6월 말~7월 중순경 이뤄질 예정으로, 네이버클라우드는 한국 이용자... ', 'Fri, 28 May 2021 10:20:00 +0900'),
	('[월가 분석] 캐시우드 ETF 내 유망 종목', 'https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202105280010&t=NNv', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=104&oid=215&aid=0000960953', '분석가들은 올해 들어 횡보하던 아마존(AMZN)이 반등할 거라고 봤습니다. 매출이 44% 급증한 회사 실적 발표에 힘입어 앞으로 1년 내 30% 이상 랠리를 예상했습니다. 이 외에도 클라우드 기반 커뮤니테이션 플랫폼... ', 'Fri, 28 May 2021 10:16:00 +0900'),
	('[글로벌 블록체인] 5월 28일 오전 뉴스 브리핑', 'http://www.newspim.com/news/view/20210528000291', 'http://www.newspim.com/news/view/20210528000291', '또 그는 이날 지금 비트코인 및 암호화폐를 거부하는 것은 아마존이 1990년대 초 전자상거래를 처음 시작했을 때 인터넷 사업 모델을 받아들이지 않는 것과 비슷하다. 암호화폐는 \'돈의 자유\'를 제공하기 위해 존재한다... ', 'Fri, 28 May 2021 10:31:00 +0900'),
	('[Who Is ?] 김영문 한국동서발전 사장', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', ' (2019/04/14, 한국경제 인터뷰에서 한진그룹 총수 일가의 밀수 혐의 등을 조사한 결과를 이야기하며) 장기적으로 우리나라도 알리바바나 아마존 같은 전자상거래 플랫폼을 만들 수 있다면 좋겠지만 당장은 전자상거래... ', 'Fri, 28 May 2021 10:26:00 +0900'),
	('아마존 데이터를 현지 시장조사에 활용하라', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', '◇아마존, 시장조사에 어떻게 활용할까 = 이날 세미나에서 발표를 맡은 김성수 케이존 대표는 미국 등 해외 시장에 진출할 때 데이터를 바탕으로 시장조사를 하는 것이 중요한데, 가장 효율적인 방법 중 하나가 아마존을... ', 'Fri, 28 May 2021 10:24:00 +0900'),
	('네이버클라우드, 단종 앞둔 센트OS 대안 록키리눅스와 협력', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', '록키리눅스는  클라우드 서비스 공급자(CSP)로는 네이버클라우드와 아마존웹서비스(AWS)와 협력을 진행하고 있다. ​록키 리눅스 정식 배포는 6월 말~7월 중순경 이뤄질 예정으로, 네이버클라우드는 한국 이용자... ', 'Fri, 28 May 2021 10:20:00 +0900'),
	('[월가 분석] 캐시우드 ETF 내 유망 종목', 'https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202105280010&t=NNv', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=104&oid=215&aid=0000960953', '분석가들은 올해 들어 횡보하던 아마존(AMZN)이 반등할 거라고 봤습니다. 매출이 44% 급증한 회사 실적 발표에 힘입어 앞으로 1년 내 30% 이상 랠리를 예상했습니다. 이 외에도 클라우드 기반 커뮤니테이션 플랫폼... ', 'Fri, 28 May 2021 10:16:00 +0900'),
	('[글로벌 블록체인] 5월 28일 오전 뉴스 브리핑', 'http://www.newspim.com/news/view/20210528000291', 'http://www.newspim.com/news/view/20210528000291', '또 그는 이날 지금 비트코인 및 암호화폐를 거부하는 것은 아마존이 1990년대 초 전자상거래를 처음 시작했을 때 인터넷 사업 모델을 받아들이지 않는 것과 비슷하다. 암호화폐는 \'돈의 자유\'를 제공하기 위해 존재한다... ', 'Fri, 28 May 2021 10:31:00 +0900'),
	('[Who Is ?] 김영문 한국동서발전 사장', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', ' (2019/04/14, 한국경제 인터뷰에서 한진그룹 총수 일가의 밀수 혐의 등을 조사한 결과를 이야기하며) 장기적으로 우리나라도 알리바바나 아마존 같은 전자상거래 플랫폼을 만들 수 있다면 좋겠지만 당장은 전자상거래... ', 'Fri, 28 May 2021 10:26:00 +0900'),
	('아마존 데이터를 현지 시장조사에 활용하라', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', '◇아마존, 시장조사에 어떻게 활용할까 = 이날 세미나에서 발표를 맡은 김성수 케이존 대표는 미국 등 해외 시장에 진출할 때 데이터를 바탕으로 시장조사를 하는 것이 중요한데, 가장 효율적인 방법 중 하나가 아마존을... ', 'Fri, 28 May 2021 10:24:00 +0900'),
	('네이버클라우드, 단종 앞둔 센트OS 대안 록키리눅스와 협력', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', '록키리눅스는  클라우드 서비스 공급자(CSP)로는 네이버클라우드와 아마존웹서비스(AWS)와 협력을 진행하고 있다. ​록키 리눅스 정식 배포는 6월 말~7월 중순경 이뤄질 예정으로, 네이버클라우드는 한국 이용자... ', 'Fri, 28 May 2021 10:20:00 +0900'),
	('[월가 분석] 캐시우드 ETF 내 유망 종목', 'https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202105280010&t=NNv', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=104&oid=215&aid=0000960953', '분석가들은 올해 들어 횡보하던 아마존(AMZN)이 반등할 거라고 봤습니다. 매출이 44% 급증한 회사 실적 발표에 힘입어 앞으로 1년 내 30% 이상 랠리를 예상했습니다. 이 외에도 클라우드 기반 커뮤니테이션 플랫폼... ', 'Fri, 28 May 2021 10:16:00 +0900'),
	('[글로벌 블록체인] 5월 28일 오전 뉴스 브리핑', 'http://www.newspim.com/news/view/20210528000291', 'http://www.newspim.com/news/view/20210528000291', '또 그는 이날 지금 비트코인 및 암호화폐를 거부하는 것은 아마존이 1990년대 초 전자상거래를 처음 시작했을 때 인터넷 사업 모델을 받아들이지 않는 것과 비슷하다. 암호화폐는 \'돈의 자유\'를 제공하기 위해 존재한다... ', 'Fri, 28 May 2021 10:31:00 +0900'),
	('[Who Is ?] 김영문 한국동서발전 사장', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', 'https://www.businesspost.co.kr/BP?command=article_view&num=233573', ' (2019/04/14, 한국경제 인터뷰에서 한진그룹 총수 일가의 밀수 혐의 등을 조사한 결과를 이야기하며) 장기적으로 우리나라도 알리바바나 아마존 같은 전자상거래 플랫폼을 만들 수 있다면 좋겠지만 당장은 전자상거래... ', 'Fri, 28 May 2021 10:26:00 +0900'),
	('아마존 데이터를 현지 시장조사에 활용하라', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', 'http://www.weeklytrade.co.kr/news/view.html?section=1&category=3&item=&no=73531', '◇아마존, 시장조사에 어떻게 활용할까 = 이날 세미나에서 발표를 맡은 김성수 케이존 대표는 미국 등 해외 시장에 진출할 때 데이터를 바탕으로 시장조사를 하는 것이 중요한데, 가장 효율적인 방법 중 하나가 아마존을... ', 'Fri, 28 May 2021 10:24:00 +0900'),
	('네이버클라우드, 단종 앞둔 센트OS 대안 록키리눅스와 협력', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403769', '록키리눅스는  클라우드 서비스 공급자(CSP)로는 네이버클라우드와 아마존웹서비스(AWS)와 협력을 진행하고 있다. ​록키 리눅스 정식 배포는 6월 말~7월 중순경 이뤄질 예정으로, 네이버클라우드는 한국 이용자... ', 'Fri, 28 May 2021 10:20:00 +0900'),
	('[월가 분석] 캐시우드 ETF 내 유망 종목', 'https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202105280010&t=NNv', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=104&oid=215&aid=0000960953', '분석가들은 올해 들어 횡보하던 아마존(AMZN)이 반등할 거라고 봤습니다. 매출이 44% 급증한 회사 실적 발표에 힘입어 앞으로 1년 내 30% 이상 랠리를 예상했습니다. 이 외에도 클라우드 기반 커뮤니테이션 플랫폼... ', 'Fri, 28 May 2021 10:16:00 +0900'),
	('소형 고급주거시설 \'원에디션 강남\' 분양 중', 'http://mbnmoney.mbn.co.kr/news/view?news_no=MM1004344681', 'http://mbnmoney.mbn.co.kr/news/view?news_no=MM1004344681', '아마존·페이스북 등 글로벌 기업 입주가 예정돼 있어 인근 테헤란로와 연계한 산업클러스터로 자리매김할 전망입니다. 또 글로벌 MICE 산업 중심지로 거듭날 글로벌 비즈니스 센터(GBC) 부지가 가까워, 해외 수요 유입에... ', 'Fri, 28 May 2021 11:04:00 +0900'),
	('SK와 합작 추진 美 플러그파워 “모빌리티·발전용 연료전지 적극 진출”', 'http://www.electimes.com/article.php?aid=1622074834217824121', 'http://www.electimes.com/article.php?aid=1622074834217824121', '현재 30개 이상의 아마존 물류창고와 50개 이상의 월마트 물류창고에 지게차를 납품했고, 홈디포·GM·BMW 등도 플러그파워가 납품한 지게차로 화물을 운반하고 있다. 플러그파워는 프랑스 자동차그룹 르노와 연내... ', 'Fri, 28 May 2021 11:02:00 +0900'),
	('AWS, 기업내 컨테이너 앱 관리 서비스 \'ECS 애니웨어\' 공식 출시', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403782', 'http://www.digitaltoday.co.kr/news/articleView.html?idxno=403782', '아마존웹서비스 로고. 아마존웹서비스(AWS)가 온프레미스(on premise: 내부에 인프라나 소프트웨어를 구축한 방식)에서 컨테이너 기반 애플리케이션을 돌리고 싶은 기업들을 겨냥해 완전 관리되는 컨테이너... ', 'Fri, 28 May 2021 11:02:00 +0900'),
	('[신간안내]\'아마존 사람들은 이렇게 일합니다\' 外', 'https://view.asiae.co.kr/article/2021052416310044466', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=103&oid=277&aid=0004910497', '◆아마존 사람들은 이렇게 일합니다= 아마존 내부자들의 시선으로 그들만의 독보적인 조직 운영을 들여다본다. 특유 리더십을 비롯해 성과 관리, 인재 육성, 목표 설정 등이다. 빠르게 성장한 초일류 기업의 조직문화와... ', 'Fri, 28 May 2021 10:58:00 +0900'),
	('[글로벌 블록체인] 5월 28일 오전 뉴스 브리핑', 'http://www.newspim.com/news/view/20210528000291', 'http://www.newspim.com/news/view/20210528000291', '또 그는 이날 지금 비트코인 및 암호화폐를 거부하는 것은 아마존이 1990년대 초 전자상거래를 처음 시작했을 때 인터넷 사업 모델을 받아들이지 않는 것과 비슷하다. 암호화폐는 \'돈의 자유\'를 제공하기 위해 존재한다... ', 'Fri, 28 May 2021 10:31:00 +0900');
/*!40000 ALTER TABLE `news_tbl` ENABLE KEYS */;

-- 테이블 python_db.users_tbl 구조 내보내기
CREATE TABLE IF NOT EXISTS `users_tbl` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '내부관리ID',
  `uid` varchar(64) NOT NULL COMMENT '회원ID',
  `upw` varchar(64) NOT NULL COMMENT '회원PW',
  `name` varchar(64) NOT NULL COMMENT '회원이름',
  `regdate` timestamp NOT NULL DEFAULT current_timestamp() COMMENT '가입일',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uid` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- 테이블 데이터 python_db.users_tbl:~2 rows (대략적) 내보내기
/*!40000 ALTER TABLE `users_tbl` DISABLE KEYS */;
INSERT INTO `users_tbl` (`id`, `uid`, `upw`, `name`, `regdate`) VALUES
	(1, 'guest', '1', '게스트', '2021-06-10 10:23:48'),
	(2, 'admin', '1', '관리자', '2021-06-10 10:28:22');
/*!40000 ALTER TABLE `users_tbl` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
