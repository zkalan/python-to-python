#coding=utf-8
import urllib2
import cookielib

filename = "cookie.txt"

#声明一个MozillaCookieJar对象实例来保存cookie
file_cookie = cookielib.MozillaCookieJar(filename)

#实例化一个cookiejar对象来存储cookie
cookie = cookielib.CookieJar()

#利用urllib2库中的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
file_handler = urllib2.HTTPCookieProcessor(file_cookie)

#创建一个功能容器
opener = urllib2.build_opener(handler)
file_opener = urllib2.build_opener(file_handler)

url = 'http://www.baidu.com'

response = opener.open(url)
file_opener.open(url)

#输出到命令窗口
for item in cookie:
    print 'Name = ' + item.name
    print 'Value = ' + item.value

#保存cookie到文件
file_cookie.save(ignore_discard=True, ignore_expires=True)

#从文件读取cookie
read_cookie = cookielib.MozillaCookieJar()

read_cookie.load("cookie.txt", ignore_discard=True, ignore_expires=True)

req = urllib2.Request(url)

read_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(read_cookie))

result = read_opener.open(req)

print result.read()