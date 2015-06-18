"""tocHw3.py"""
__author__ = "Wayne Wei"
__email__ = "tinglongwei@gmail.com"
__id__ = "F74014025"
__version__ = "1"
"""
===Description===
Using some simple ways to get top k outlinks from the input file
"""

import re
import sys

if len(sys.argv) < 3:   # Check arguments
    print "Not enough arguments!\n"
    sys.exit()
else:
    try:
        f = open(sys.argv[1], 'r')
        top = int(sys.argv[2])
        if(top < 0):
            print "Top k should be positve integer!\n"
            sys.exit()
    except IOError:
        print "Can't open file: %s !\n" %sys.argv[1]
        sys.exit()
    except ValueError:
        print "Top k should be integer!\n"
        sys.exit()

res_uri = re.compile("WARC-Target-URI\":\"([^\"]*)\"")
res_link = re.compile("\"Links\":\[(.*?)\}\]")
res_href = re.compile("\"href\":\"([^\"]*)\"")
res_url = re.compile("\"url\":\"([^\"]*)\"")

uri = []
num = []

for line in f:
    weburi = res_uri.search(line)
    uri.append(weburi.group(1))
    link = res_link.search(line)

    if link is not None:  # Find "Links"
        linkUrl = res_url.findall(link.group(1))
        linkHref = res_href.findall(link.group(1))
        num.append(len(linkUrl) + len(linkHref))
    else:
        num.append(0)

f.close()

# sort all the outlinks in reverse
result = sorted(range(len(num)), key=lambda i: num[i], reverse=True)

x = 0
if (top <= len(uri) and top != 0):
    for resVal in result:   # get top k outlinks
        if x + 1 < len(uri):
            if x < top:
                previous = num[resVal]
                print "%s: %d" % (uri[resVal], num[resVal])
            # handle same number of outlinks
            elif (x >= top and num[resVal] == previous):
                print "%s: %d" % (uri[resVal], num[resVal])
            else:
                break
            x += 1
        else:
            break
    print

elif top == 0:
    pass
else:
    print "Top %d is out of range!\n" % top
