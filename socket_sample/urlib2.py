__author__ = 'Admin'
import requests
import urllib2
u = "http://www.baidu.com"
s = requests.get(u)
#data = urllib2.urlopen(u).read().decode('gbk','ignore')
#data.encode('utf-8')
print s.content,s.status_code

#print data