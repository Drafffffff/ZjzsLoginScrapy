# ZjzsLoginScrapy
## 1. 这是一个用来爬取浙江招生网信息的爬虫


## 2. 一个大概是我写过最工整的程序，认真的写了一个叫“F(uck)_zjzs”的类，在F_zjzs.py文件下。最基本的登录操作如下：
> 1. 定义F_zjzs类的实例user
> 2. 传入user.IdentityID和user.PassWorld 两个参数
> 3. 调用user.get_Verifycode(),获取验证码，此时获取验证码的客户端的SessionId、程序识别好的验证码会分别储存在user.ASP和user.VerifyCode中
> 4. 此时可以需调用user.Tidy_Data()方法，整理收集好的Cookie保存在请求头中
> 5. 到这一步终于可以用user.login()方法登录了
> 6. 登录成功后，可用user.default()方法获取登录后的主界面，请求到的网页信息储存在user.resultpage 变量上
> 7. 根据需要对请求到的数据进行分析。（这步还没写）
> 8. 使用user.logout()方法退出登录



## 3. 需要的依赖有 requests tesseract3.04 


## 4. 菜逼写的小脚本，希望有大神能指出更好的写法～


Mail:i0.0ia@qq.com


## 5. TODO
> 1. 完成从Excel读取储存用户数据的部分
> 2. 完成对查分网站的网页分析（需等到学考查分开放）
