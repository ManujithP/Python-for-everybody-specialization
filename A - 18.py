import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_869871.xml'
xml = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(xml)
lst = tree.findall('comments/comment')
print('User count:', len(lst))

lt = []
for branch in lst:
    lt.append(int(branch.find('count').text))

print('Sum:',sum(lt))
