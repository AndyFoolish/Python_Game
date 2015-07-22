#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
str1 = ["Make yourself at home.",
    "None of your business.",
    "I will be more careful.",
    "How about going to a move?",
    "Your life is your own affair"]
# #将所有字母都转换为小写
# str2=[]
# for i in range(len(str1)):
#     str2.append(str1[i].lower())
# #正则提取表达式
# pattern = re.compile(r'\byour\b')
# #记录次数
# current_list=[]
# for i in range(len(str2)):
#     current_list.append(len(pattern.findall(str2[i]))) 

# 在正则表达式里忽略大小写
pattern = re.compile(r'\byour\b', re.I)
#记录次数
current_list=[]
for i in range(len(str1)):
    current_list.append(len(pattern.findall(str1[i]))) 
print(current_list)

#冒泡排序
for i in range(len(str1)-1):
    for j in range(len(str1)-i-1):
        if current_list[j]<current_list[j+1]:
            current_list[j],current_list[j+1]=current_list[j+1],current_list[j]
            str1[j],str1[j+1]=str1[j+1],str1[j]
             
print(str1)    
