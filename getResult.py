# encoding:utf-8

import requests
import base64

# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=RY6y0LzEz63sPI9sj13d51xf&client_secret=gVjkG7YQQHqHQFgZNEL0EIX1yTFC8Q5M'
tokenResponse = requests.get(host)
tokenResponseData = tokenResponse.json()

request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/get_request_result"
# 二进制方式打开图片文件
f = open('class15.1.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"request_id":"23491381_2353284"}
access_token = tokenResponseData["access_token"]
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())