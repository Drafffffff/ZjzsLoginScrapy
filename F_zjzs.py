# -*- coding: utf-8 -*-


import requests
import os
from ocr import get_yzm


class F_zjzs:
    userflag = 0
    IdentityID = ""
    PassWorld = ""
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
    cookie = ""
    VerifyCode = ""
    appid = "sjs81a01h81ar8ss8ay5y4c9yi09i99yi949"

    def get_Verifycode(self):
        request = requests.get(
            'http://pgzy.zjzs.net:8011/INC/VerifyCode.aspx',
            headers=self.header)
        self.ASP = request.cookies['ASP.NET_SessionId']
        self.format_cookie()
        self.header['Cookie'] = self.cookie
        # request  "ASP_NET_SessionId"
        path = os.getcwd() + '/img/' + 'tmp' +\
            '.jpg'
        open(path, 'wb').write(request.content)
        self.VerifyCode = get_yzm(path)

    def Tidy_Data(self):
        self.data = {'yzm': self.VerifyCode,
                     'mima': self.PassWorld,
                     'shenfenzheng': self.IdentityID,
                     'title': 'login'
                     }

    def format_cookie(self, ASP=True, usersfz=False, appid=False,
                      userflag=False):
        self.cookie = ''
        if ASP:
            if self.cookie == '':
                pass
            else:
                self.cookie = self.cookie + ';'
            self.cookie = self.cookie + ' ASP.NET_SessionId=' + self.ASP + ';'
        if usersfz:
            self.cookie = self.cookie + ' usersfz=' + self.IdentityID + ';'
        if appid:
            self.cookie = self.cookie + ' appid=' + self.appid + ';'
        if userflag:
            self.cookie = self.cookie + ' userflag=' + str(self.userflag) + ';'
        self.cookie = self.cookie[:-1]

    def weilo(self):
        self.format_cookie(ASP=True, usersfz=True, appid=True)
        self.header['Cookie'] = self.cookie
        self.resultpage = requests.get(
            'http://pgzy.zjzs.net:8011/default.aspx')  # , headers=self.header)

    def login(self):
        # http://pgzy.zjzs.net:8011/ashx/loginHandler.ashx
        self.format_cookie(ASP=True, appid=True)
        self.header['Cookie'] = self.cookie
        print self.cookie
        self.Tidy_Data()
        self.result = requests.post(
            'http://pgzy.zjzs.net:8011/ashx/loginHandler.ashx',
            headers=self.header, data=self.data
        )
        self.userflag = 1
        print 'login!'

    def default(self):
        self.format_cookie(ASP=True, usersfz=True, appid=True)
        self.header['Cookie'] = self.cookie
        print self.cookie
        self.resultpage = requests.get(
            'http://pgzy.zjzs.net:8011/default.aspx', headers=self.header)

    def logout(self):
        self.format_cookie(ASP=True, usersfz=True, appid=True,
                           userflag=True)
        self.header['Cookie'] = self.cookie
        requests.get(
            'http://pgzy.zjzs.net:8011/logout.aspx', headers=self.header)
        self.userflag = 0
        print "logoutted!"
