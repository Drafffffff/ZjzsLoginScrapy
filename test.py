#
import requests
header = {
    'Accept': 'image/webp,image/*,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': '',
    'Host': 'pgzy.zjzs.net:8011',
    'Referer': 'http://pgzy.zjzs.net:8011/login.htm',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
data = ''
request = requests.get(
    'http://pgzy.zjzs.net:8011/INC/VerifyCode.aspx',
    headers=header)
print type(request.cookies['ASP.NET_SessionId'])
result = requests.post(
    'http://pgzy.zjzs.net:8011/ashx/loginHandler.ashx',
    headers=header, data=data
)
