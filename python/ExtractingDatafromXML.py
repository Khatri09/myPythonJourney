import urllib.request, urllib.error
import xml.etree.ElementTree as ET
import ssl
# from bs4 import BeautifulSoup
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)
counts = tree.findall('.//count')
# print("Count: " + str(len(counts)))
total = 0

for count in counts:
    # print(count.text)
    # total = total + int(count.text)
    total += int(count.text)
print('Sum:', total)
