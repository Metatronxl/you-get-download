#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/20
# @Author : lei.X


import os
import requests
from pyquery import PyQuery as pq


def get_urls(url):
    """
    解析网页数据，获得目标url
    """
    response = requests.get(url)
    if response.status_code == 200:
        # print(response.text)
        html = response.text
        doc = pq(html)
        a_list = doc('li.video a.title')
        # print(a_list)
        print(type(a_list))
        url_list = [a.attr('href').strip('//') for a in a_list.items()]
        print(url_list)
        return url_list
    return None


def cmd_download(url):
    """
    逐条进行下载视频
    """
    try:
        info = os.system(r'you-get --debug -o C:\test  {}'.format(url))
        print(info)
    except Exception as e:
        print(e)
        cmd_download(url)


def main():
    """
    函数的主入口
    """
    for i in range(1, 3):
        url = 'https://search.bilibili.com/video?keyword=%E8%90%A7%E4%BA%95%E9%99%8C&order=totalrank&page=' + str(i)
        url_list = get_urls(url)
        if url_list is not None:
            [cmd_download(url) for url in url_list]

def test(url):
    try:
        info = os.system(r'you-get --debug -o /Users/xulei2/Downloads  {}'.format(url))
        print(info)
    except Exception as e:
        print(e)



if __name__ == '__main__':
    test("https://www.bilibili.com/bangumi/play/ep205871")