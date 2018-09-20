#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/20
# @Author : lei.X


import os
import requests
import json
from bs4 import BeautifulSoup

"""
根据up主的所有视频页面来爬取他所有的视频
"""
def get_urls(url):
    """
    解析网页数据，获得目标url
    """
    response = requests.get(url, verify=False)
    print(response.text)
    json_dict = json.loads(response.text)
    result_list = analyseJson(json_dict)
    print(len(result_list))
    return result_list

def analyseJson(json_dict):

    status = json_dict['status']
    data = json_dict['data']
    vlist = data['vlist']
    video_url = []
    for sub_list in vlist:
        aid = sub_list['aid']
        temp_url = 'https://www.bilibili.com/video/av'+str(aid)
        video_url.append(temp_url)
    return video_url


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
    print(get_urls("https://space.bilibili.com/ajax/member/getSubmitVideos?mid=617285&pagesize=100&tid=0&page=&keyword=&order=pubdate"))