import getpass
import os
from time import sleep


print ('请输入要储存的网站信息（或名称）：')
web = input()
print ('请输入要存储的用户名：')
name = input()
pwd = getpass.getpass('请输入密码： ')
pwd_ = getpass.getpass('请重新输入密码：')
if pwd != pwd_ :
    print ('两次密码输入不一致，请重新输入！')
    sleep(1.5)
    while 1:
        os.system('cls')
        print ('请输入要储存的信息：\n' + web + '\n请输入要存储的用户名：\n'+name+'\n')
        pwd = getpass.getpass('请输入密码： ')
        pwd_ = getpass.getpass('请重新输入密码：')
        if pwd == pwd_ :
            break
        else:
            print ('两次密码输入不一致，请重新输入！')
            sleep(2.5)
            continue
print ('请输入备注：')
note = input()
if note == '':
    note = '无备注'
f = open('pwd_record.txt','a+')
f.write(web+'用户名:'+name+'\n'+'密码:'+pwd_+'\n备注:'+note+'\n\n')
f.close()
print ('用户名密码保存成功！')
sleep(1.5)
        

