#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/20
# @Author : lei.X

import requests
from configparser import RawConfigParser
import os

class MainDownload:
    def __init__(self):
        cf = RawConfigParser()
        cf.read('config')
        self.startId = int(cf.get('info','startId'))
        self.num = int(cf.get('info','num'))
        self.mainPage ="https://www.bilibili.com/bangumi/play/ep"

    def cmd_download(self,url):
        try:
            info = os.system(r'you-get --debug -o /Users/xulei2/Downloads  {}'.format(url))
            print(info)
        except Exception as e:
            print(e)
            self.cmd_download(url)

    def generate_download_url(self):

        download_url_list = [ self.mainPage+str(i) for i in range(self.startId,self.startId+self.num)]
        for singlen_url in download_url_list:
            self.cmd_download(singlen_url)



if __name__ == '__main__':

    mainDownload = MainDownload()
    mainDownload.generate_download_url()


