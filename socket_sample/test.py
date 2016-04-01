#coding = utf-8
import re
from bs4 import BeautifulSoup
import urllib2
from urlparse import urlparse


url_to_work = []

host = 'http://www.dytt8.net'
u = 'http://www.2tu.cc/Html/GP1681.html'
try:
    data = urllib2.urlopen(u).read().decode('gbk','ignore')
    data.encode('utf-8')
except:
    pass
try:
    soup = BeautifulSoup(data)

    link =  soup.find('div',{'class':'mox'})
    for url in  link.findAll('a'):
       print host+url['href']
except:
    pass
