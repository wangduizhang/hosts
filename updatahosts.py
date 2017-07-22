#!/usr/bin/python
#_*_coding:utf-8

from download import download
import os
import shutil
import Tkinter
from wxpy import *
import PIL

hostspath = "/Users/wp/Desktop/hosts/hosts"
d_hosts = "/Users/wp/Desktop/hosts/hosts.part"
to_path = "/private/etc/hosts"
bak_path = "/private/etc/hosts.bak"

'''
def gethosts():
    bot = Bot(console_qr = True)
  

    mpss = bot.mps().search(u'喜淘')
    u = ensure_one(mpss)

    u.send(u"富强")
    

    @bot.register(u,SHARING)
    def just_print(msg):
        # 打印消息
        print msg.url




    embed()
    #bot.logout()
'''



#处理文件
def delhosts():
    with open(hostspath, 'r') as f:
        lines = f.readlines()

    openwrite = True

    f2 = open(hostspath,'w')

    f2.write("####################仅供学习使用####################\n")
    for index,l in enumerate(lines):
        if index < 4:
            pass
        elif openwrite:
            f2.write(l)
        if "Tumblr Start" in l:
            openwrite = False
            f2.write("####pass####\n")
        if "Tumblr End" in l:
            openwrite = True
            f2.write("# Tumblr End\n")
    f2.close()
    print "处理完成"



def download_hosts():
    #下载hosts
    try:
        os.remove(d_hosts)
    except OSError as e:
        pass
    file = download("https://raw.githubusercontent.com/wangduizhang/hosts/master/hosts","/Users/wp/Desktop/hosts",replace=True)
    try:
        os.remove(hostspath)
    except OSError as e:
        pass
    os.rename(d_hosts, hostspath)
    #备份
    try:
        os.rename(to_path, bak_path)
    except OSError as e:
        pass
    #移动
    f = open(to_path,"w")
    f.close()

    shutil.copyfile(hostspath, to_path)
    print "hosts更新完成..."



if __name__ == '__main__':
    print "1.获取微信hosts更新2.处理原始hosts 3.自动下载更新"
    
    choice = int(raw_input(">>>"))
    ok = True

    while (ok):
        if choice == 1:
            gethosts()
            ok = False
        elif choice == 2:
            delhosts()
            ok = False
        elif choice == 3:
            download_hosts()
            ok = False
        else:
            pass
    




