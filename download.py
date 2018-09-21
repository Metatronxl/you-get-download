#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/9/20
# @Author : lei.X


import os
import requests
import json
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
"""
根据up主的所有视频页面来爬取他所有的视频
"""
def get_urls(url):
    """
    解析网页数据，获得目标url
    """
    try:
        response = requests.get(url)
        json_dict = json.loads(response.text)
        result_list = analyseJson(json_dict)
        return result_list
    except Exception as e:
        print(e)

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


"""
输入参数为up主的uid
默认下载前100个视频
"""
def getUPsAllVideoUrl(uid):
    full_url = "https://space.bilibili.com/ajax/member/getSubmitVideos?mid="+str(uid)+"&pagesize=100&tid=0&page=&keyword=&order=pubdate"
    url_list =  get_urls(full_url)
    return url_list

def getUpsVideoUrl(uid,count):
    full_url = "https://space.bilibili.com/ajax/member/getSubmitVideos?mid="+str(uid)+"&pagesize="+str(count)+"&tid=0&page=&keyword=&order=pubdate"
    url_list =  get_urls(full_url)

    return url_list



def test(url):
    try:
        info = os.system(r'you-get --debug -o /Users/xulei2/Downloads  {}'.format(url))
        print(info)
    except Exception as e:
        print(e)



if __name__ == '__main__':
    result_list = get_urls("https://space.bilibili.com/ajax/member/getSubmitVideos?mid=617285&pagesize=100&tid=0&page=&keyword=&order=pubdate")
    for singlen in result_list:
        print(singlen)