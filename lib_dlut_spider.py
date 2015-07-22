#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import urllib.request
import urllib.parse
# from collections import deque

class dlutSpider(object) :
	def __init__(self) :
		print("开始爬取网页")

	def changePage(self, url, totalPage) :
		# 获取不同页面的url
		page_group = []
		regexUrl = re.compile(r'classid=00000(\d+)', re.S)
		nowPage = int(regexUrl.search(url).group(1))

		for i in range(nowPage, totalPage) :
			link = re.sub('classid=00000\d+', 'classid=00000{0:05}'.format(i), url, re.S)
			# link = re.sub('classid=00000\d+', 'classid=00000%05d'%i, url, re.S)
			page_group.append(link)
		return page_group

	def convert(self, data):
		#转码
		data = data.strip('&#x;') #把'&#x957f;'变为'957f'
		data = bytes(r'\u'+data, 'ascii')#把'957f'转换为b'\\u957f' 
		return data.decode('unicode_escape')#转换为汉字

	def getData(self, url) :
		#获取网页内容
		html = urllib.request.urlopen(url)
		data = html.read().decode('utf-8')
		data = re.sub(r'&#x....;', lambda match:self.convert(match.group()), data)#这里的match是指通过r'&#x....;'得到的匹配项
		return data

	def getSource(self, data) :
		# 获取网页中所要提取的所有条内容
		source = re.findall(r'<tr id="del_(.*?)</tr>', data, re.S)
		return source

	def getInfo(self, eachSource) :
		# 对每一条内容，再分类提取有用信息
		info = {}	#定义一个字典
		info["title"] = re.search(r'<a class="blue".*?>(.*?)</a>', eachSource, re.S).group(1)
		otherInfo = re.findall(r'<td bgcolor.*?"whitetext">(.*?)</td>', eachSource, re.S)
		info["author"] = otherInfo[2]
		info["publishHouse"] = otherInfo[3]
		info["publishDate"] = otherInfo[4]
		info["callNumber"] = otherInfo[5]
		return info

	def saveInfo(self, CollectInfo) :
		#保存结果
		writeFile = open('dlut_lib_info.txt', 'a')
		for item in CollectInfo :
			writeFile.writelines('题名：  ' + item['title'] + '\n')
			writeFile.writelines('责任者： ' + item['author'] + '\n')
			writeFile.writelines('出版社： ' + item['publishHouse'] + '\n')
			writeFile.writelines('出版日期：' + item['publishDate'] + '\n')
			writeFile.writelines('索书号： ' + item['callNumber'] + '\n')
			writeFile.write('\n\n')
		writeFile.close()

def dlutLibSpider(initial_url, num):
	#调用爬虫的函数
	lib_dlut_spider = dlutSpider()
	page_group = lib_dlut_spider.changePage(initial_url, num)# 获取不同页面的url

	for page in page_group:
		print("----正在处理页面----"+page)
		CollectInfo = []
		data = lib_dlut_spider.getData(page)
		source = lib_dlut_spider.getSource(data)
		if len(source) == 0:
			print("该页面无内容")
			continue
		else:
			for eachSource in source:
				info = lib_dlut_spider.getInfo(eachSource)
				CollectInfo.append(info)
			lib_dlut_spider.saveInfo(CollectInfo)

initial_url = "http://opac.lib.dlut.edu.cn/opac/show_user_shelf.php?classid=0000000000"
num = 20000
dlutLibSpider(initial_url, num)			
print("爬取结束")
