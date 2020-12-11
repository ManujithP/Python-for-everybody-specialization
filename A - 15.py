import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_869869.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

lst = list()
tags = soup('span')
for tag in tags:
    words = tag.contents[0]
    no = re.findall('[0-9]+',words)
    num = int(no[0])
    lst.append(num)
print(sum(lst))
