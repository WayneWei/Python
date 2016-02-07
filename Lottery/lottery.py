#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
from bs4 import BeautifulSoup
import json
reload(sys)
sys.setdefaultencoding('utf8')
from sys import argv
import random
from time import strftime

def checkValidComment():
	for i in xrange(len(data["comments"]["data"])):
		if "我想住普立緹"  not in data["comments"]["data"][i]["message"]:
			data["comments"]["data"].pop(i)
			return checkValidComment()

def checkRepeatComment():
	for i in range(0,len(data["comments"]["data"])):
		for x in range(i+1, len(data["comments"]["data"])):
			if data["comments"]["data"][i]["from"]["name"] == data["comments"]["data"][x]["from"]["name"]:
				data["comments"]["data"].pop(x)
				return checkRepeatComment()

def printAll():
	for post in data["comments"]["data"]:
		print "\t", post["from"]["name"], post["message"]

print "普立緹住宿會館 [ 雙人住宿卷 ] 抽獎\n-----------------------------"

print ">>", strftime("%Y-%m-%d %H:%M:%S"), "讀取留言"

with open('comment.json') as data_file:    
    data = json.load(data_file)

print ">>", strftime("%Y-%m-%d %H:%M:%S"), "檢查留言 是否符合規定"

checkValidComment()

print ">>", strftime("%Y-%m-%d %H:%M:%S"), "檢查留言 是否有重複回覆"

checkRepeatComment()


print ">>", strftime("%Y-%m-%d %H:%M:%S"), "有效留言: 共有", len(data["comments"]["data"]), "則"


printAll()

print ">>", strftime("%Y-%m-%d %H:%M:%S"), "開始抽獎（亂數隨機）"

pick = random.choice(data["comments"]["data"])

print "\t恭喜,", pick["from"]["name"], "\t獲得 '免費雙人住宿卷' 乙份"