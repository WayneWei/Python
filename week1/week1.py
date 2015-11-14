#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
from BeautifulSoup import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

url = "https://tw.stock.yahoo.com/us/worldidx.php"
data = requests.get(url).text
# print data
soup = BeautifulSoup(data)

# print (soup.prettify())

table = soup('table')[5]

# print table.prettify()

tag = table.findAll('tr')[4].findAll('td')[2].b.string

print "日經指數 " + tag
