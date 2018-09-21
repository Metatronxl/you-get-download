# you-get-download
定制you-get下载脚本



### TODO

- you-get下载部分视频存在403问题



### 0x00  Requirements

- requests
- you-get



###  0x01 添加了动漫合集下载（多进程）

新建`config`文件，添加参数`startId`和`num`，求中`startId`代表这个动漫的ep的开始集数对应的数字，`num`是指要下载的集数

效果如图：

![屏幕快照 2018-09-20 下午12.16.07](https://ws4.sinaimg.cn/large/006tNbRwly1fvh512bqssj31j80rmgsy.jpg)



### 0x02 爬取up主的所有的视频

需要做的就是把up主的所有视频所在的页面填写进去，省下的就交给它吧：P

![屏幕快照 2018-09-21 下午2.13.00](https://ws2.sinaimg.cn/large/006tNbRwly1fvh52rx7o4j31kw0kudo6.jpg)