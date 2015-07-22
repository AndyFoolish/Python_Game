#!/usr/bin/env python
# -*- coding: utf-8 -*-
#定义一个函数，实现去除重复单词的功能
def rem_dup():
	#打开文件，读取内容
	with open('ex6.py','r') as f:
		text = f.read()
	#首先将文本中的单词提取出来
	
	#字符串替换返回一个新的字符串，原先字符串不改变，因此不能使用replace()方法
	#先将字符串转换为list，然后对list进行替换，最后再转换为字符串
	stringList = list(text)

	for i in range(len(stringList)):
		if (stringList[i] >='a' and stringList[i] <='z') or\
	    	(stringList[i] >='A' and stringList[i]<='Z') or\
	     	(stringList[i]==' '):
			continue
		else:
			stringList[i]=' '		
	#将列表重新组装成字符串	
	string2 = ''.join(stringList)
	#提取出单词list
	stringList2 = string2.split()

	#去除重复单词
	stringList3 = []
	for i in stringList2:
		if stringList2.count(i) == 1:
			stringList3.append(i)
	#组装字符串
	string3 = ' '.join(stringList3)
	
	#写入到文件中
	with open('ex6.py','w') as f:
		f.write(string3)

#调用
rem_dup()
		