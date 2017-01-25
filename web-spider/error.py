import urllib2
import urllib

url = "http://www.zkalan.top"

request = urllib2.Request(url)

try:
    urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print e.code
    print e.reason