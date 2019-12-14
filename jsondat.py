import requests
import json
parm={"page":2,"count":4}
r=requests.get("http://httpbin.org/get",params=parm)
print(r.status_code)
print(r.text,type(r.text))
print(json.loads(r.text))
print(r.json())

#     "User-Agent": "python-requests/2.22.0"
#   },
#   "origin": "157.45.28.164, 157.45.28.164",
#   "url": "https://httpbin.org/get?page=2&count=4"
# }
#  <class 'str'>
# {'args': {'count': '4', 'page': '2'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0'}, 'origin': '157.45.28.164, 157.45.28.164', 'url': 'https://httpbin.org/get?page=2&count=4'}
# {'args': {'count': '4', 'page': '2'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.22.0'}, 'origin': '157.45.28.164, 157.45.28.164', 'url': 'https://httpbin.org/get?page=2&count=4'}
