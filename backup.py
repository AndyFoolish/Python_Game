#!/usr/bin/env python
# -*- coding: utf-8 -*-
#backup under ubuntu
#filename: backup1.py
import os
import time
import Tkinter #界面编程

def backup():
	global entrySource
	global entryTarget
	# 判断操作系统
	if os.name == "nt":
		pass
		# source = "C:\\User\\AndyFoolish\\source\\"
		# targetDir = "C:\\User\\AndyFoolish\\backup\\"
	elif os.name == "posix":
		# 源文件目录
		# source = "/home/tony/Documents/"
		# 目标路径
		# targetDir = "/home/tony/Desktop/"
		source = entrySource.get()
		targetDir = entryTarget.get()
	# 目标文件夹
	# time.strftime()将时间日期转换为字符串格式
	todayDir = targetDir + time.strftime("%Y%m%d")
	
	# 目标文件名
	timeDir = time.strftime("%H%M%S")
	target = todayDir + os.sep + timeDir + ".zip"
	
	# 压缩指令
	zipCommand = "zip -qr %s %s"%(target, source)
	
	# 判断指定路径的文件或文件夹是否存在
	if os.path.exists(todayDir) == False:
		os.mkdir(todayDir)
	
	# 执行压缩命令
	if os.system(zipCommand) == 0:
		print("backup successful")
	else:
		print("back failed")

#编写界面框架
root = Tkinter.Tk()
root.title('Backup')
root.geometry('200x200')

# 文本控件
lblSource = Tkinter.Label(root, text="Source")
lblSource.grid(row=0, column=0)
# 输入框控件
entrySource = Tkinter.Entry(root)
entrySource.grid(row=0, column=1)

lblTarget = Tkinter.Label(root, text="Target")
lblTarget.grid(row=1, column=0)
entryTarget = Tkinter.Entry(root)
entryTarget.grid(row=1, column=1)

# 按钮控件
button = Tkinter.Button(root, text="Backup", command = backup)
button.grid(row=3, column=0)
# 界面开始
root.mainloop()