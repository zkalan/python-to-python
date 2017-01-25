import urllib2
import urllib

value = {"username":"2206813598@qq.com","password":"chenjin125"}

data = urllib.urlencode(value)

loginurl = "https://www.acg44.com/sign?redirect=%2F%2Fwww.acg44.com%2Faccount"

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

loginrequest = urllib2.Request(loginurl,data,headers)

response = urllib2.urlopen(loginrequest)

print response.read()