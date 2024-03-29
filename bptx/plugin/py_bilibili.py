#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json
import time
import base64

class Spider(Spider):  # 元类 默认的元类 type
	def getName(self):
		return "哔哩"
	def init(self,extend=""):
		print("============{0}============".format(extend))
		pass
	def isVideoFormat(self,url):
		pass
	def manualVideoCheck(self):
		pass
	def homeContent(self,filter):
		result = {}
		cateManual = {
	"Zard": "Zard",
"倒库": "倒库",
"动画": "动画",
"少儿": "少儿",
"美食": "美食",
"说案": "说案",		     
"探案": "探案",	     
"宇宙": "宇宙",
"外太空": "外太空",
"太阳系": "太阳系",
"银河系": "银河系",
"恒星": "恒星",
"行星": "行星",
"黑洞": "黑洞",
"奥秘": "奥秘",
"未解之谜": "未解之谜",
"外星人": "外星人",
"飞碟探索": "飞碟探索",
"纪录片": "纪录片",
"BBC记录": "BBC记录",
"Discovery": "Discovery",
"荒野求生": "荒野求生",
"大灾难": "大灾难",
"探索发现": "探索发现",
"人与自然": "人与自然",
"河马": "河马",
"鳄鱼": "鳄鱼",
"角马迁徙过河": "角马迁徙过河",
"鲸鱼": "鲸鱼",
"巨蜥": "巨蜥",
"狮子": "狮子",
"微观世界": "微观世界",
"微生物": "微生物",
"昆虫": "昆虫",
"动物世界": "动物世界",
"地理": "地理",
"历史": "历史",
"纪实": "纪实",
"考古": "考古",
"航拍": "航拍",
"户外": "户外",
"赶海": "赶海",
"钓鱼": "钓鱼",
"水上运动": "水上运动",
"皮划艇": "皮划艇",
"龙舟比赛": "龙舟比赛",
"钱塘江观潮": "钱塘江观潮",
"冲浪": "冲浪",
"旅游": "旅游",
"相声小品": "相声小品",
"戏曲": "戏曲",
"搞笑": "搞笑",
"快板": "快板",
"莲花落": "莲花落",
"评书": "评书",
"魔术": "魔术",
"杂技": "杂技",
"广场舞": "广场舞",
"mtv": "mtv",
"健身": "健身",
"DJ热播": "DJ热播",
"演唱会": "演唱会",
"赵本山": "赵本山",
"宋小宝": "宋小宝",
"文松": "文松",
"张帝": "张帝",
"张行": "张行",
"刘文正": "刘文正",
"张蔷": "张蔷",
"吴涤清": "吴涤清",
"刀郎": "刀郎",
"陈淑桦": "陈淑桦",
"轮滑": "轮滑",
"蹦极": "蹦极",
"攀岩": "攀岩",
"跑酷": "跑酷",
"蹦极": "蹦极",
"翼装飞行": "翼装飞行",
"高山速降": "高山速降",
"极现运动": "极现运动",
"飞镖": "飞镖",
"斗牛": "斗牛",
"摔角": "摔角",
"武林风": "武林风",
"太极": "太极",
"足球": "足球",
"篮球": "篮球",
"排球": "排球",
"世界杯": "世界杯",
"NBA": "NBA",
"围棋": "围棋",
"桥牌": "桥牌",
"斗地主": "斗地主",
"将棋": "将棋",
"五子棋": "五子棋",
"国际象棋": "国际象棋",
"国际跳棋": "国际跳棋",
"中国象棋": "中国象棋",
"麻将": "麻将",
"中式台球": "中式台球",
"乒乓球": "乒乓球",
"曲棍球": "曲棍球",
"橄榄球": "橄榄球",
"高尔夫": "高尔夫",
"台球": "台球",
"九球": "九球",
"斯诺克": "斯诺克",
"冰球": "冰球",
"羽毛球": "羽毛球",
"壁球": "壁球",
"保龄球": "保龄球",
"网球": "网球",
"冰壶": "冰壶",
"电子竞技": "电子竞技",
"决战平安京": "决战平安京",
"畜牧": "畜牧",
"养殖": "养殖",
"水产": "水产",
"假窗-白噪音": "假窗-白噪音"
		}
		classes = []
		for k in cateManual:
			classes.append({
				'type_name':k,
				'type_id':cateManual[k]
			})
		result['class'] = classes
		if(filter):
			result['filters'] = self.config['filter']
		return result
	def homeVideoContent(self):
		result = {
			'list':[]
		}
		return result
	cookies = ''
	def getCookie(self):
		rsp = self.fetch("https://www.bilibili.com/")
		self.cookies = rsp.cookies
		return rsp.cookies
	def categoryContent(self,tid,pg,filter,extend):		
		result = {}
		url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword={0}&duration=4&page={1}'.format(tid,pg)
		if len(self.cookies) <= 0:
			self.getCookie()
		rsp = self.fetch(url,cookies=self.cookies)
		content = rsp.text
		jo = json.loads(content)
		if jo['code'] != 0:			
			rspRetry = self.fetch(url,cookies=self.getCookie())
			content = rspRetry.text		
		jo = json.loads(content)
		videos = []
		vodList = jo['data']['result']
		for vod in vodList:
			aid = str(vod['aid']).strip()
			title = vod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
			img = 'https:' + vod['pic'].strip()
			remark = str(vod['duration']).strip()
			videos.append({
				"vod_id":aid,
				"vod_name":title,
				"vod_pic":img,
				"vod_remarks":remark
			})
		result['list'] = videos
		result['page'] = pg
		result['pagecount'] = 9999
		result['limit'] = 90
		result['total'] = 999999
		return result
	def cleanSpace(self,str):
		return str.replace('\n','').replace('\t','').replace('\r','').replace(' ','')
	def detailContent(self,array):
		aid = array[0]
		url = "https://api.bilibili.com/x/web-interface/view?aid={0}".format(aid)

		rsp = self.fetch(url,headers=self.header)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		title = jo['title'].replace("<em class=\"keyword\">","").replace("</em>","")
		pic = jo['pic']
		desc = jo['desc']
		typeName = jo['tname']
		vod = {
			"vod_id":aid,
			"vod_name":title,
			"vod_pic":pic,
			"type_name":typeName,
			"vod_year":"",
			"vod_area":"",
			"vod_remarks":"",
			"vod_actor":"",
			"vod_director":"",
			"vod_content":desc
		}
		ja = jo['pages']
		playUrl = ''
		for tmpJo in ja:
			cid = tmpJo['cid']
			part = tmpJo['part']
			playUrl = playUrl + '{0}${1}_{2}#'.format(part,aid,cid)

		vod['vod_play_from'] = 'B站'
		vod['vod_play_url'] = playUrl

		result = {
			'list':[
				vod
			]
		}
		return result
	def searchContent(self,key,quick):
		result = {
			'list':[]
		}
		return result
	def playerContent(self,flag,id,vipFlags):
		# https://www.555dianying.cc/vodplay/static/js/playerconfig.js
		result = {}

		ids = id.split("_")
		url = 'https://api.bilibili.com:443/x/player/playurl?avid={0}&cid=%20%20{1}&qn=112'.format(ids[0],ids[1])
		rsp = self.fetch(url)
		jRoot = json.loads(rsp.text)
		jo = jRoot['data']
		ja = jo['durl']
		
		maxSize = -1
		position = -1
		for i in range(len(ja)):
			tmpJo = ja[i]
			if maxSize < int(tmpJo['size']):
				maxSize = int(tmpJo['size'])
				position = i

		url = ''
		if len(ja) > 0:
			if position == -1:
				position = 0
			url = ja[position]['url']

		result["parse"] = 0
		result["playUrl"] = ''
		result["url"] = url
		result["header"] = {
			"Referer":"https://www.bilibili.com",
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
		}
		result["contentType"] = 'video/x-flv'
		return result

	config = {
		"player": {},
		"filter": {}
	}
	header = {}

	def localProxy(self,param):
		return [200, "video/MP2T", action, ""]