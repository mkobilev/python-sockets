import re
import urllib
import requests

url = "http://176.9.193.6/challenges_x/final/wbb_x2/"

ses = requests.session()

index = ses.get(url)
#name="rSBARhObAM"

param = re.findall(r'name="(:?[A-Za-z]{10})"', index.text)[0]

#print param

args = urllib.unquote(ses.cookies['challenge']).encode('utf8')
print args

if '+++' in args:
    ar1 = args.split('+')[0]
    ar2 = args.split('+')[-1]
    ans = int(ar1) + int(ar2)
    print ans
else:
    ar1 = args.split('+')[0]
    ar2 = args.split('+')[-1]
    ans = int(ar1) - int(ar2)
    print ans

data = {param:ans}
post = ses.post(url, data=data)

print post.text