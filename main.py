from F_zjzs import F_zjzs
id = '33088120001013004X'
pw = '20001013wx'
id1 = '33088120000816892X'
pw1 = '20000816xyx'
zhoulongfei = F_zjzs()
zhoulongfei.IdentityID = '330881200003083716'
zhoulongfei.PassWorld = 'dragonfly000308'
zhoulongfei.get_Verifycode()
print zhoulongfei.cookie
print zhoulongfei.VerifyCode
zhoulongfei.Tidy_Data()
zhoulongfei.login()
print zhoulongfei.result.text
zhoulongfei.default()
print zhoulongfei.resultpage.text
zhoulongfei.logout()
