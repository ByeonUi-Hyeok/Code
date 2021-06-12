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

-- 테이블 python_db.news_tbl 구조 내보내기
CREATE TABLE IF NOT EXISTS `news_tbl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` text DEFAULT NULL,
  `originallink` text DEFAULT NULL,
  `link` text DEFAULT NULL,
  `description` text DEFAULT NULL,
  `pubDate` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;

-- 테이블 데이터 python_db.news_tbl:~25 rows (대략적) 내보내기
/*!40000 ALTER TABLE `news_tbl` DISABLE KEYS */;
INSERT INTO `news_tbl` (`id`, `title`, `originallink`, `link`, `description`, `pubDate`) VALUES
	(1, 'SKT, E3 2021 참여…글로벌 콘솔 게임 시장 공략', 'http://www.nspna.com/news/?mode=view&newsid=507777', 'http://www.nspna.com/news/?mode=view&newsid=507777', 'Xbox와 아시아 국가 중 유일하게 5GX 클라우드 게임 협력을 진행 중인 SKT는 E3 2021에 별도 온라인 부스를... 전시에는 SKT를 비롯해 Xbox·닌텐도·유비소프트 등 글로벌 게임 제조 및 개발 업체 50여 곳이 참여해 12일... ', 'Fri, 11 Jun 2021 12:52:00 +0900'),
	(2, 'SKT, 국내 통신사 최초 세계 최대 게임 박람회 \'E3 2021\' 참여', 'http://www.techholic.co.kr/news/articleView.html?idxno=198661', 'http://www.techholic.co.kr/news/articleView.html?idxno=198661', '전시에는 SKT를 비롯해 Xbox∙닌텐도∙유비소프트 등 글로벌 게임 제조 및 개발 업체 50여 곳이 참여해... SKT는 Xbox와 아시아 국가 중 유일하게 \'5GX 클라우드 게임\' 협력, E3 2021에 별도 온라인 부스를 마련해 국내... ', 'Fri, 11 Jun 2021 12:26:00 +0900'),
	(3, 'SKT, 세계 최대 게임 박람회 \'E3 2021\' 참여...글로벌 콘솔 게임 시장 공략', 'http://www.worktoday.co.kr/news/articleView.html?idxno=16137', 'http://www.worktoday.co.kr/news/articleView.html?idxno=16137', ': SKT가 12일(현지시간)부터 열리는 세계 최대 게임 박람회 \'E3 2021\'에 온라인 부스를 마련하고 국내 게임... Xbox와 아시아 국가 중 유일하게 \'5GX 클라우드 게임\' 협력을 진행 중인 SKT는 E3 2021에 별도 온라인 부스를... ', 'Fri, 11 Jun 2021 12:22:00 +0900'),
	(4, '“SKT 분할하면 시총 5조 증가”', 'http://news.heraldcorp.com/view.php?ud=20210611000529', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=016&aid=0001847316', '인적분할 작업에 돌입한 SK텔레콤이 분할 이후 시가총액이 5조원 증가할 것으로 예측됐다. 이에 최근 최고점을 경신한 주가의 추가적인 상승이 점쳐진다. SK텔레콤의 주가는 인적분할과 액면분할을 결의한 지난 10일... ', 'Fri, 11 Jun 2021 12:20:00 +0900'),
	(5, 'SKT, 세계 최대 게임박람회 ‘E3’ 참가', 'http://news.heraldcorp.com/view.php?ud=20210611000521', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=105&oid=016&aid=0001847308', 'SK텔레콤이 게임 퍼블리싱(배급)을 통해 글로벌 콘솔 게임 시장 공략을 본격화 한다. SK텔레콤은 국내 통신사 최초로 세계 최대 규모의 게임 박람회인 ‘E3 2021’에 참가한다고 11일 밝혔다. E3는 미국... ', 'Fri, 11 Jun 2021 12:17:00 +0900'),
	(6, '[정성봉 칼럼] 글로벌 협상력을 결정하는 4가지 주요 요인', 'http://www.m-economynews.com/news/article.html?no=31088', 'http://www.m-economynews.com/news/article.html?no=31088', '한 예로 US Airline과 Airbus간의 경우인데 US Airline은 세계민항기 제작시장을 한때는 거의 독점하고 있던 보잉과의 상호의존관계가 형성되지 않아서 점보기 구입에 관한 협상을 시도하지 못하고 있었다. 자금 여력이 없는... ', 'Fri, 11 Jun 2021 09:22:00 +0900'),
	(7, '[글로벌 비즈] 넷플릭스, 온라인 스토어 오픈…인기 작품 굿즈 판매 예정', 'https://biz.sbs.co.kr/article_hub/20000018850?division=NAVER', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=101&oid=374&aid=0000247222', '블룸버그통신에 따르면 유나이티드항공은 보잉 737맥스 기종을 포함해 최소 100대의 여객기를 주문하기 위해... 최근 여행에 대한 수요가 여름 휴가철을 앞두고 급증하면서 보잉과 에어버스 같은 항공기 제조업체들 역시... ', 'Fri, 11 Jun 2021 08:08:00 +0900'),
	(8, '비트코인 승인 국가 엘살바도르 마지막 아닐 것...가상화폐 전망은? [글로벌...', 'https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202106110010&t=NNv', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=104&oid=215&aid=0000964091', '보잉, 미중 갈등에 노심초사 보잉은 지난 11월 미 항공당국이 보잉 737 맥스 기종의 재운항을 허가하면서 기분좋은 흐름을 이어가는 듯 했지만, 중국 시장에서 난관에 봉착했습니다. CNN에 따르면, 향후 10년간 중국이... ', 'Fri, 11 Jun 2021 08:03:00 +0900'),
	(9, '美 증시, 인플레 우려 떨치고 강세...S&amp;P 사상최고 [뉴욕 증시]', 'https://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202106110022&t=NNv', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=104&oid=215&aid=0000964092', '골드만, `강력 매수` 투자 의견 보잉 상승...유나이티드항공, 737맥스 100대 구매 논의 게임스톱 하락...... 보잉은 미국 내 항공 수요 회복에 대한 기대감이 커지는 가운데 유나이티드 항공이 보잉 737맥스 기종을... ', 'Fri, 11 Jun 2021 08:03:00 +0900'),
	(10, '뉴욕증시, 인플레 우려에도 일제히 올라-S&amp;P500 사상최고치…아마존 2%대, 테...', 'http://www.econonews.co.kr/news/articleView.html?idxno=203273', 'http://www.econonews.co.kr/news/articleView.html?idxno=203273', '21% 하락했으며 AMC엔터테인먼트 홀딩스와 웬디스도 각각 13.28%, 3.13% 급락했다. 항공기 제작사 보잉은 유나이티드 항공과 대규모 여객기 판매를 논의 중이라는 보도 이후에도 0.18% 상승에 그쳤다.', 'Fri, 11 Jun 2021 06:48:00 +0900'),
	(11, '\'무료수강\' 남성·여성갱년기로 인한 화병 및 편두통증상 등의 극복을 위한 심...', 'http://www.job-post.co.kr/news/articleView.html?idxno=24914', 'http://www.job-post.co.kr/news/articleView.html?idxno=24914', '\'무료수강\' 이벤트 중인 60종 자격증 온라인강의에 대한 자세한 사항은 한국능률교육평가원 홈페이지에서 확인 가능하며, 카카오톡 및 네이버톡톡, 유선을 통한 전화문의가 가능하다.', 'Fri, 11 Jun 2021 13:00:00 +0900'),
	(12, '카카오뱅크, 중·저신용 대출 고객에 \'첫달 이자\' 돌려준다', 'http://www.bloter.net/newsView/blt202106110009', 'https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=105&oid=293&aid=0000035058', '카카오뱅크는 중‧저신용 고객을 대상으로 대출 이자를 지원한다고 11일 밝혔다. 이달 10일부터 다음달 9일까지 카카오뱅크에서 신용대출, 직장인 사잇돌대출을 신규로 받은 중‧저신용 고객(KBC 기준 820점 이하)이... ', 'Fri, 11 Jun 2021 12:58:00 +0900'),
	(13, '글로벌 진격 카카오웹툰, 태국·대만서 출시 직후 웹툰 앱 1위', 'https://www.techm.kr/news/articleView.html?idxno=84707', 'https://www.techm.kr/news/articleView.html?idxno=84707', '사진=카카오페이지 제공 카카오엔터테인먼트는 글로벌향 웹툰 플랫폼 \'카카오웹툰\'이 태국과 대만 시장 출시 동시에 웹툰 앱 1위를 차지했다고 11일 밝혔다. 지난 7일 태국에서 출시된 \'카카오웹툰\'은 구글 플레이... ', 'Fri, 11 Jun 2021 12:58:00 +0900'),
	(14, '카카오톡 쇼핑하기, \'톡딜\'통해 팔도 제철 먹거리 판매', 'http://www.kmaeil.com/news/articleView.html?idxno=286269', 'http://www.kmaeil.com/news/articleView.html?idxno=286269', '카카오커머스가 운영하는 쇼핑플랫폼 \'카카오톡 쇼핑하기\'가 2인 이상 공동구매 서비스인 \'톡딜\'에서 팔도 제철 먹거리를 판매한다고 밝혔다.(사진=카카오커머스) 카카오커머스가 운영하는 쇼핑플랫폼 \'카카오톡 쇼핑하기... ', 'Fri, 11 Jun 2021 12:56:00 +0900'),
	(15, '[더벨]카카오뱅크, 은행업 꼬리표 떼기…거품 논란 잠재우나', 'http://www.thebell.co.kr/front/free/contents/news/article_view.asp?key=202106101430539880107249', 'http://www.thebell.co.kr/front/free/contents/news/article_view.asp?key=202106101430539880107249', '카카오뱅크가 플랫폼 비즈니스에 공을 들이고 있다. 향후 성장성은 물론 당장 눈앞으로 다가온 IPO 과정에서... ◇흑자전환 오히려 밸류 걸림돌?...\'은행업\' 비교기업 존재도 부담 카카오뱅크는 지난 9일부터 새... ', 'Fri, 11 Jun 2021 12:56:00 +0900'),
	(16, '[더벨][IB 수수료 점검]NH증권, 하이브 \'유증\' 수수료 40억…역대 두번째 규모', 'http://www.thebell.co.kr/front/free/contents/news/article_view.asp?key=202106091719094640104917', 'http://www.thebell.co.kr/front/free/contents/news/article_view.asp?key=202106091719094640104917', 'NH투자증권이 하이브 유상증자 수수료로 40억원에 이르는 수익을 확보했다. NH투자증권이 유상증자로 40억원대 수수료를 수취한 것은 2011년 이후 10년만이다. 하이브는 9일 222만7848주의 신주를 발행하는 유상증자... ', 'Fri, 11 Jun 2021 12:56:00 +0900'),
	(17, '하이브·초록뱀미디어, 방탄소년단(BTS) 관련주 모두 상승세로…초록뱀미디어...', 'http://www.econonews.co.kr/news/articleView.html?idxno=203441', 'http://www.econonews.co.kr/news/articleView.html?idxno=203441', '하이브 주가흐름(그래픽=네이버금융 캡처) 방탄소년단(BTS) 관련주인 하이브와 초록뱀미디어가 상승세다. 초록뱀미디어는 11일 코스닥 시장에서 낮 12시54분 현재 전 거래일보다 0.2%(5원) 상승한 2485원에 거래... ', 'Fri, 11 Jun 2021 12:56:00 +0900'),
	(18, '북미 기업 중심 비트코인 채굴협의회 출범···일런 머스크 역할은 없다', 'https://decenter.kr/NewsView/22NLFQTV35', 'https://decenter.kr/NewsView/22NLFQTV35', '그가 공유한 BMC 공식 홈페이지에는 창립 회원으로 아르고 블록체인, 블록캡, 코어사이언티픽, 하이브 블록체인, 허트8마이닝, 마라톤 디지털 홀딩스, 마이크로스트래티지, 라이엇블록체인, 갤럭시 디지털 등... ', 'Fri, 11 Jun 2021 12:10:00 +0900'),
	(19, '방탄소년단, 데뷔일 맞아 13∼14일 온라인 팬미팅 \'소우주\'', 'http://www.incheonilbo.com/news/articleView.html?idxno=1099800', 'http://www.incheonilbo.com/news/articleView.html?idxno=1099800', '▲ /하이브 제공 방탄소년단이 데뷔일인 6월 13일을 맞아 온라인 팬 미팅을 연다. 소속사 하이브는 방탄소년단이 13일과 14일 온라인 스트리밍으로 팬 미팅 \'BTS 2021 머스터(MUSTER) 소우주\'(이하 소우주) 공연을 연다고 11일... ', 'Fri, 11 Jun 2021 10:50:00 +0900'),
	(20, '‘BTS 페스타’ 마지막은 온라인 팬미팅…13·14일 개최', 'http://www.kukinews.com/newsView/kuk202106110046', 'http://www.kukinews.com/newsView/kuk202106110046', '사진=하이브 제공. 그룹 방탄소년단이 오는 13일과 14일 온라인 팬미팅 ‘BTS 2021 머스터 소우주’를 연다. 이번 팬미팅은 방탄소년단이 데뷔 8주년을 기념해 개최한 ‘페스타(FESTA)의 마지막 행사다. 방탄소년단은 매년... ', 'Fri, 11 Jun 2021 10:30:00 +0900'),
	(21, '하이브·초록뱀미디어, 방탄소년단(BTS) 관련주 모두 상승세로…초록뱀미디어...', 'http://www.econonews.co.kr/news/articleView.html?idxno=203441', 'http://www.econonews.co.kr/news/articleView.html?idxno=203441', '하이브 주가흐름(그래픽=네이버금융 캡처) 방탄소년단(BTS) 관련주인 하이브와 초록뱀미디어가 상승세다. 초록뱀미디어는 11일 코스닥 시장에서 낮 12시54분 현재 전 거래일보다 0.2%(5원) 상승한 2485원에 거래... ', 'Fri, 11 Jun 2021 12:56:00 +0900'),
	(22, '[더벨][IB 수수료 점검]NH증권, 하이브 \'유증\' 수수료 40억…역대 두번째 규모', 'http://www.thebell.co.kr/front/free/contents/news/article_view.asp?key=202106091719094640104917', 'http://www.thebell.co.kr/front/free/contents/news/article_view.asp?key=202106091719094640104917', 'NH투자증권이 하이브 유상증자 수수료로 40억원에 이르는 수익을 확보했다. NH투자증권이 유상증자로 40억원대 수수료를 수취한 것은 2011년 이후 10년만이다. 하이브는 9일 222만7848주의 신주를 발행하는 유상증자... ', 'Fri, 11 Jun 2021 12:56:00 +0900'),
	(23, '북미 기업 중심 비트코인 채굴협의회 출범···일런 머스크 역할은 없다', 'https://decenter.kr/NewsView/22NLFQTV35', 'https://decenter.kr/NewsView/22NLFQTV35', '그가 공유한 BMC 공식 홈페이지에는 창립 회원으로 아르고 블록체인, 블록캡, 코어사이언티픽, 하이브 블록체인, 허트8마이닝, 마라톤 디지털 홀딩스, 마이크로스트래티지, 라이엇블록체인, 갤럭시 디지털 등... ', 'Fri, 11 Jun 2021 12:10:00 +0900'),
	(24, '방탄소년단, 데뷔일 맞아 13∼14일 온라인 팬미팅 \'소우주\'', 'http://www.incheonilbo.com/news/articleView.html?idxno=1099800', 'http://www.incheonilbo.com/news/articleView.html?idxno=1099800', '▲ /하이브 제공 방탄소년단이 데뷔일인 6월 13일을 맞아 온라인 팬 미팅을 연다. 소속사 하이브는 방탄소년단이 13일과 14일 온라인 스트리밍으로 팬 미팅 \'BTS 2021 머스터(MUSTER) 소우주\'(이하 소우주) 공연을 연다고 11일... ', 'Fri, 11 Jun 2021 10:50:00 +0900'),
	(25, '‘BTS 페스타’ 마지막은 온라인 팬미팅…13·14일 개최', 'http://www.kukinews.com/newsView/kuk202106110046', 'http://www.kukinews.com/newsView/kuk202106110046', '사진=하이브 제공. 그룹 방탄소년단이 오는 13일과 14일 온라인 팬미팅 ‘BTS 2021 머스터 소우주’를 연다. 이번 팬미팅은 방탄소년단이 데뷔 8주년을 기념해 개최한 ‘페스타(FESTA)의 마지막 행사다. 방탄소년단은 매년... ', 'Fri, 11 Jun 2021 10:30:00 +0900');
/*!40000 ALTER TABLE `news_tbl` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
