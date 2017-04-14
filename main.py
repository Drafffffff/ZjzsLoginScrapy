# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup
from F_zjzs import F_zjzs
from Excelio import get_identid, get_passwd, wr_in, get_name


if __name__ == "__main__":
    user = F_zjzs()
    for i in xrange(2, 5):
        id = get_identid(i)
        pw = get_passwd(i)
        print get_name(i)
        # print id, '____', pw
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
