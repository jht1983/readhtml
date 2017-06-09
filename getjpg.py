import os
import urllib
import re

def gethtml(url):
    return urllib.urlopen(url).read()
    
def getimg(html):
    img_re = re.compile(r'src=“(http:.+\.jpg)')
    imgList = re.findall(img_re,html)
    imgNo = 1
    for imgAddr in imgList:
         urllib.urlretrieve(imgAddr,"img%s.jpg" % imgNo)
         imgNo += 1
getimg(gethtml('http://www.ifeng.com'))

print 'finish!'

    
