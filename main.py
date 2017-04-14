from F_zjzs import F_zjzs


if __name__ == "__main__":
    id = '33088120001013004X'
    pw = '20001013w'
    id1 = '33088120000816892X'
    pw1 = '20000816x'
    zhoulongfei = F_zjzs()
    zhoulongfei.IdentityID = id
    zhoulongfei.PassWorld = pw
    zhoulongfei.get_Verifycode()
    # print zhoulongfei.cookie
    print zhoulongfei.VerifyCode
    zhoulongfei.Tidy_Data()
    zhoulongfei.login()
    print zhoulongfei.result.cookies["appid"]
    zhoulongfei.default()
    print zhoulongfei.resultpage.text
    zhoulongfei.logout()
