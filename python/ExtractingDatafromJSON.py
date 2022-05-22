import json
import urllib.request, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
info = json.loads(data)
print('Retrieved', len(data), 'characters')
#print('User count:', len(info))
sumcount = 0
count = 0
for item in info['comments']:
    item = int(item['count'])
    sumcount = sumcount + item
    count+=1
print(count, sumcount)
