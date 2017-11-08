#coding:UTF-8
import urllib.request

url = "http://www.jinyingfei.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)