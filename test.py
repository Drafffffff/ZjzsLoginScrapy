# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from F_zjzs import F_zjzs
from Excelio import get_identid, get_passwd, wr_in

user = F_zjzs()

for i in xrange(2, 5):
    id = get_identid(i)
    pw = get_passwd(i)
    print id, '____', pw
    user.IdentityID = id
    user.PassWorld = pw
    user.get_Verifycode()
    user.Tidy_Data()
    user.login()
    user.default()
    # print user.resultpage.text
    soup = BeautifulSoup(user.resultpage.text, "lxml")
    tag = soup.select('#Div11')[0]
    url = 'http://pgzy.zjzs.net:8011/' + tag["name"]
    tmp = user.Req(url).text
    # print tmp
    soupp = BeautifulSoup(tmp, 'lxml')
    lishi = soupp.select(
        'body > div > table:nth-of-type(1) > tr:nth-of-type(4) > td:nth-of-type(6)')[0].string
    dili = soupp.select(
        'body > div > table:nth-of-type(1) > tr:nth-of-type(4) > td:nth-of-type(7)')[0].string
    huaxue = soupp.select(
        'body > div > table:nth-of-type(1) > tr:nth-of-type(4) > td:nth-of-type(9)')[0].string
    print lishi, dili, huaxue
    wr_in('D', i, lishi)
    wr_in('E', i, dili)
    wr_in('F', i, huaxue)
    user.logout()

# #
# import requests
# header = {
#     'Accept': 'image/webp,image/*,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Connection': 'keep-alive',
#     'Cookie': '',
#     'Host': 'pgzy.zjzs.net:8011',
#     'Referer': 'http://pgzy.zjzs.net:8011/login.htm',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
#     (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
# }
# data = ''
# request = requests.get(
#     'http://pgzy.zjzs.net:8011/INC/VerifyCode.aspx',
#     headers=header)
# print type(request.cookies['ASP.NET_SessionId'])
# result = requests.post(
#     'http://pgzy.zjzs.net:8011/ashx/loginHandler.ashx',
#     headers=header, data=data
# )
