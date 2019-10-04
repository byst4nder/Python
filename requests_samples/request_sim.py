import  requests
import json


# get方法
web = requests.get("http://httpbin.org/get?user=wanglian")
print('web数据类型：',type(web))
print('状态码和描述：',web.status_code,web.reason)
print("get返回信息：",json.loads(web.text))
web.close()

# post方法
web=requests.post('http://httpbin.org/post?login=a',json={"user":3421,"passwd":'adfe'})
print('post返回信息：',json.loads(web.text))