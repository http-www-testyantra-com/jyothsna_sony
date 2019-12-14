import requests
import json
parm={"un":"huhhi,","pass":"testing"}
r=requests.post("http://httpbin.org/post",data=parm)
print(r.status_code)
print(r.text)
#here it wil take data to form not args

import requests
import json
param={"un":"huhhi,","pass":"testing"}
r=requests.post("http://httpbin.org/post",params=param)
print(r.status_code)
print(r.text)
#args it wil take data


