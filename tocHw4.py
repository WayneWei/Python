"""tocHw4.py"""
__author__ = "Wayne Wei"
__email__ = "tinglongwei@gmail.com"
__id__ = "F74014025"
__version__ = "1"
"""
===Description===
Find out the file extension and number from the inpur file which match the query
"""

import re
import sys
from collections import Counter

if len(sys.argv) < 3:   # incorrect arguments
    print "Not enough arguments!\n"
    sys.exit()
else:
    try:
        f = open(sys.argv[1], 'r')
        string = str(sys.argv[2])
    except IOError:
        print "Can't open file: %s !\n" %sys.argv[1]
        sys.exit()

res_uri = re.compile("WARC-Target-URI\":\"([^\"]*)\"")
res_link = re.compile("\"Links\":\[(.*?)\}\]")
reString = ""

for t in list(string):
    if (t == '.') | (t == '?') | (t == '-'):
        reString += "\\" + t
    else:
        reString += t

res_query = re.compile(reString)
# res_query = re.compile(str(sys.argv[2]))
res_href = re.compile("\"href\":\"([^\"]*)\"")
res_url = re.compile("\"url\":\"([^\"]*)\"")
res_http = re.compile("https?:\/\/(\S*)")
res_slash = re.compile("\/")
res_file = re.compile("\.")
res_para = re.compile("([^\?]*)")

uri = []
total = 0
index = []
url = []
href = []
extension = []
outlink = []

for line in f:
    weburi = res_uri.search(line)
    uri.append(weburi.group(1))

    if res_query.search(weburi.group(1)) is not None:
        index.append(total)  # query may match multiple web

    link = res_link.search(line)

    if link is not None:
        linkUrl = res_url.findall(link.group(1))    # Get url
        url.append(linkUrl)
        linkHref = res_href.findall(link.group(1))  # Get href
        href.append(linkHref)
    else:
        url.append(None)
        href.append(None)

    total += 1

f.close()

if not index:  # Can't find query
    print "Page not found!\n"
    sys.exit()
else:  # Match query
    i = 0
    # print index
    # print len(index)
    for i in index:
        if i is not None:
            if (url[i] is not None and href[i] is not None):
                outlink = url[i] + href[i]
                for j in outlink:
                    # outlinks is http or https
                    if res_http.search(j) is not None:
                        # except the link with query
                        rx = res_http.search(j).group(1)
                        if res_query.search(rx) is None:    #
                            if res_slash.search(rx) is not None:
                                if res_para.search(rx) is not None:
                                    rk = res_para.search(rx).group(1)
                                    tp = rk.split("/")
                                    if res_file.search(tp[len(tp) - 1]) is not None:
                                        qt = tp[len(tp) - 1].split(".")
                                        extension.append(qt[len(qt) - 1])
    result = Counter(extension)

    if len(extension) != 0:
        for k in result:
            print k, ":", result[k]
        print
    else:
        print "Type not found!\n"
