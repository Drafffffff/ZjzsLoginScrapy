# coding=utf-8

from bs4 import BeautifulSoup
from F_zjzs import F_zjzs
from Excelio import get_identid, get_passwd, wr_in, get_name


order = {'SXXK': 'D',
         'YWXK': 'E',
         'YYXK': 'F',
         'SZXK': 'G',
         'LSXK': 'H',
         'DLXK': 'I',
         'WLXK': 'J',
         'HXXK': 'K',
         'SWXK': 'L',
         'JSXK': 'M',
         'SZXN': 'N',
         'LSXN': 'O',
         'DLXN': 'P',
         'WLXN': 'Q',
         'HXXN': 'R',
         'SWXN': 'S',
         'JSXN': 'T',
         'WYXN': 'U'
         }


if __name__ == "__main__":
    user = F_zjzs()
    for i in xrange(3, 20):
        print '________', i, '_________'
        id = get_identid(i)
        pw = get_passwd(i)
        print get_name(i)
        # print id, '____', pw
        user.IdentityID = id
        user.PassWorld = pw
        try:
            user.get_Verifycode()
        except KeyError:
            user.get_Verifycode()
        else:
            pass

        user.Tidy_Data()
        try:
            user.login()
        except KeyError:
            user.login()
        else:
            pass
        soup = BeautifulSoup(user.result.text, "lxml")
        tmpppp = soup.select(
            '#form1 > div:nth-of-type(4) > div:nth-of-type(2) > \
            div > div > span')
        # print tmpppp
        for A in tmpppp:
            print A
            wr_in(order[A['id']], i, str(A.string))
        user.clean()
