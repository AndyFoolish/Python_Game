#!/usr/bin/env python
# -*- coding: utf-8 -*-
#求素数算法

def prime(n):
	#类似于桶排序，初始化prime序列
	prime = [True]*(n+1)
	num = []
	for i in range(4, n+1, 2):
		#将除2以外的偶数全都设为非素数，便于简化后续计算
		prime[i] = False
	x = 2
	#一个数n的所有的因子不超过sqrt(n)	
	while x*x < n:
		#初步判断数x是否是素数，是素数继续执行
		if prime[x]==True:
			for y in range(2*x, n+1):
				#筛除素数倍数开始的合数
				if prime[y]==False:
					continue
				if y%x == 0:
					#如果能被x整除
					prime[y]=False
		x=x+1
	for i in range(2, n+1):
		if prime[i] == True:
			num.append(i)	
	return num
a=prime(30)
print(a)

    
