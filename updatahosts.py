#!/usr/bin/python
#_*_coding:utf-8

from download import download
import os
import shutil
import Tkinter
#from wxpy import *
import PIL
import sys


if sys.platform[:3] == 'win':
    hostspath = "C:\Users\w3260\Desktop\hosts"
    d_hosts = "C:\Users\w3260\Desktop\hosts.part"
    to_path = "C:\Windows\System32\drivers\etc\hosts"
    bak_path = "C:\Windows\System32\drivers\etc\hosts.bak"
else:
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
    print u"处理完成"



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
    print u"hosts更新完成..."

def set_hosts():
    try:
        os.rename(to_path, bak_path)
    except OSError as e:
        pass
    #移动
    f = open(to_path,"w")
    f.close()
    shutil.copyfile(hostspath, to_path)
    
    print u"hosts更新完成..."
    
def return_hosts():
    try:
        os.remove(to_path)
    except OSError as e:
        pass
    os.rename(bak_path,to_path)
    print u"hosts恢复成功"
    
    
    
    
if __name__ == '__main__':
    print u"1.获取微信hosts更新\t2.处理原始hosts\t3.放置hosts\n4.自动下载更新\t5.恢复上版"
    
    choice = int(raw_input(">>>"))
    ok = True
    while (ok):
        if choice == 1:
            #print u"功能暂未开放"
            ok = False
        elif choice == 2:
            delhosts()
            ok = False
        elif choice == 3:
            set_hosts()
            ok = False
        elif choice == 4:
            download_hosts()
            ok = False
        elif choice == 5:
            return_hosts()
            ok = False
        else:
            pass
    




