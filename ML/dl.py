import urllib2
c = urllib2.urlopen(url = 'http://www.baidu.com')
content = c.read()
print content