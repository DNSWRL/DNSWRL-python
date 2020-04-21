from django.test import TestCase

# Create your tests here.
import requests

try:
    url = "https://lab.isaaclin.cn/nCoV/api/news"
    r = requests.get(url)
    rjson = r.json()
    res = rjson['results']
    for i in res:
        print(i['title'])
except:
    print('ok')