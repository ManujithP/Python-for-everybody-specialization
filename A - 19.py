import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_869872.json'
js = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(js)

lt = []
for i in range(0,len(info["comments"])):
    lt.append(int(info["comments"][i]["count"]))

print('Sum:',sum(lt))
