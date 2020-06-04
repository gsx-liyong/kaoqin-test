#！user/bin/env python
# coding=utf-8

'''
@File  : liyong.py
@Author: 李 永
@Date  : 2020/6/4 14:46
@Desc  : 
'''

###检查字符串是否ip
def is_ip(ip):
	num_list=ip.split(".")
	if len(num_list)!=4:
		return False
	for num in  num_list
