import os
import urllib
import re

def gethtml(url):
    return urllib.urlopen(url).read()
    
def getimg(html):
    img_re = re.compile(r'src=(http:.+\.jpg)" width')
    imgList = findall(img_re,html)
    imgNo = 1
    for imgAddr in imgList:
         urllib.urlretrieve(os.path.join(url,"img%s.jpg" % imgNo)
         imgNo += 1
getimg(gethtml('http://www.baidu.com'))

print 'finish!'

    
