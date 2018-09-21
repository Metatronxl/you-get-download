#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/20
# @Author : lei.X

from configparser import RawConfigParser
import os
from multiprocessing import Process
from download import *

class MainDownload:
    def __init__(self):
        cf = RawConfigParser()
        cf.read('config')
        self.startId = int(cf.get('info','startId'))
        self.num = int(cf.get('info','num'))
        self.mainPage ="https://www.bilibili.com/bangumi/play/ep"

    def cmd_download(self,url):
        try:
            info = os.system(r'lulu --debug -o /Users/xulei2/Downloads  {}'.format(url))
            print("OS.SYSTEM :"+info)
        except Exception as e:
            # print(e)
            print("error exist ,re-download")
            self.cmd_download(url)

    def multi_download(self,download_url_list):
        processes = list()
        for singlen_url in download_url_list:
            p = Process(target=self.cmd_download,args=(singlen_url,))
            print("开始一个新的进程任务")
            p.start()
            processes.append(p)
        for p in processes:
            p.join()
        print("多线程任务结束")

    def sequence_download(self,download_url_list):
        for single_url in download_url_list:
            self.cmd_download(single_url)



    def generate_download_url(self):

        download_url_list = [ self.mainPage+str(i) for i in range(self.startId,self.startId+self.num)]
        return download_url_list



if __name__ == '__main__':

    mainDownload = MainDownload()
    """
    适用于视频号连接在一起的视频
    """
    # url_list = mainDownload.generate_download_url()

    url_list = getUpsVideoUrl("617285",1)
    mainDownload.multi_download(url_list)

