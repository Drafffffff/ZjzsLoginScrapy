# -*- coding: utf-8 -*-


import requests
import os
from ocr import get_yzm


class F_zjzs:
    userflag = 0
    IdentityID = ""
    PassWorld = ""
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://cx.zjzs.net',
        'Referer': 'http://cx.zjzs.net/exam/xyks201701/default.aspx',
        'Upgrade-Insecure-Requests': 1,
        'Cookie': '',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    cookie = ""
    VerifyCode = ""
    appid = " "

    def get_Verifycode(self):
        request = requests.get(
            # 'http://pgzy.zjzs.net:8011/INC/VerifyCode.aspx',
            'http://cx.zjzs.net/INC/VerifyCode.aspx',
            headers=self.header)
        self.ASP = request.cookies['ASP.NET_SessionId']
        self.format_cookie()
        self.header['Cookie'] = self.cookie
        # request  "ASP_NET_SessionId"
        path = os.getcwd() + '/img/' + 'tmp' +\
            '.jpg'
        open(path, 'wb').write(request.content)
        self.VerifyCode = get_yzm(path)
        # print self.VerifyCode

    def Tidy_Data(self):
        self.data = {'yzm': self.VerifyCode,
                     'ZKZH': self.PassWorld,
                     'SFZH': self.IdentityID
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
            self.cookie = self.cookie + ' CheckCode=' + self.VerifyCode + ';'
        if appid:
            self.cookie = self.cookie + ' appid=' + self.appid + ';'
        if userflag:
            self.cookie = self.cookie + ' userflag=' + str(self.userflag) + ';'
        self.cookie = self.cookie[:-1]

    # def weilo(self):
    #     self.format_cookie(ASP=True, usersfz=True, appid=True)
    #     self.header['Cookie'] = self.cookie
    #     self.resultpage = requests.get(
    #         'http://pgzy.zjzs.net:8011/default.aspx') , headers=self.header)

    def login(self):
        # http://pgzy.zjzs.net:8011/ashx/loginHandler.ashx
        self.format_cookie(ASP=True, usersfz=True)
        self.header['Cookie'] = self.cookie
        # print self.cookie
        self.Tidy_Data()
        self.result = requests.post(
            # 'http://pgzy.zjzs.net:8011/ashx/loginHandler.ashx',
            'http://cx.zjzs.net/exam/xyks201701/resault.aspx',
            headers=self.header, data=self.data
        )
        # self.userflag = 1
        # print self.result.text
        # self.appid = self.result.cookies['appid']
        # print self.appid
        print 'login!'

    # def Req(self, url):
    #     return requests.get(
    #         url, headers=self.header)

    def default(self):
        self.format_cookie(ASP=True, usersfz=True, appid=True)
        self.header['Cookie'] = self.cookie
        # print self.cookie
        self.resultpage = requests.get(
            'http://pgzy.zjzs.net:8011/default.aspx', headers=self.header)

    def logout(self):
        self.format_cookie(ASP=True, usersfz=True, appid=True,
                           userflag=True)
        self.header['Cookie'] = self.cookie
        requests.get(
            'http://pgzy.zjzs.net:8011/logout.aspx', headers=self.header)
        self.clean()
        print "logoutted!"

    def clean(self):
        self.IdentityID = ""
        self.PassWorld = ""
        self.header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://cx.zjzs.net',
            'Referer': 'http://cx.zjzs.net/exam/xyks201701/default.aspx',
            'Upgrade-Insecure-Requests': 1,
            'Cookie': '',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
        }
        self.cookie = ""
        self.VerifyCode = ""