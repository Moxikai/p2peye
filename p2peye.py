#!/usr/bin/env python
#coding:utf-8
"""
模拟浏览器加载
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import hashlib

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class P2peye():
    """借助模拟浏览器，实现渲染页面"""

    def __init__(self):
        """实例属性"""
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap[
            'phantomjs.page.settings.userAgent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
        self.driver = webdriver.PhantomJS(executable_path='/home/moxi/下载/phantomjs-2.1.1-linux-x86_64/bin/phantomjs',
                                     desired_capabilities=dcap)
        self.baseDir = os.path.dirname(__file__)
        self.htmlCacheFolder = os.path.join(self.baseDir,'.cache') # 缓存文件夹位置
        self.loadCount = 0 # 驱动加载次数
        self.start_url = 'http://www.p2peye.com/rating'
    def createFolder(self,path):
        """创建文件夹"""
        if os.path.exists(path):
            print '文件夹---%s---已存在'%(path)
            return True
        else:
            os.makedirs(path)
            return True
    def getSignName(self,string):
        """获取签名"""
        return hashlib.sha1(string).hexdigest()

    def getContent(self,url):
        self.driver.get(url)
        return self.driver.page_source

    def saveHtmlCache(self,content,name):
        """保存缓存文件"""
        try:
            path = os.path.join(self.htmlCacheFolder,name+'.html')
            with open(path,'w') as f:
                f.write(content)
            print '缓存保存成功'
        except Exception as e:
            del path
            print '写入文件----%s-----缓存出错'%(name),'\n',e


    def loadHtmlCache(self,name):
        """加载缓存文件"""
        path = self.checkExistCache(name)
        if path:
            with open(path,'r') as f:
                return f.read()
        else:
            return False

    def checkExistCache(self,name):
        """检测缓存是否存在"""
        path = os.path.join(self.htmlCacheFolder,name+'.html')
        if os.path.exists(path):
            return path
        else:
            return False

    def getListContent(self,url):
        """获取列表页内容"""
        name = self.getSignName(url)
        if self.checkExistCache(name):
            print '页面%s发现缓存，准备加载'%(url)
            content = self.loadHtmlCache(name)
        else:
            print '页面%s没有缓存，准备渲染'%(url)
            content = self.getContent(url)
            self.saveHtmlCache(content,name)
            print '页面缓存保存成功'
        return content



    def parseListContent(self,content):
        """解析列表页内容"""
        soup = BeautifulSoup(content,'lxml')



    def getDetailContent(self,url):
        """获取详细页面内容"""

    def parseDetailContent(self,content):
        """解析详细页面内容"""

    def saveToSQLite(self,**kwargs):
        """保存至sqlite数据库"""


if __name__ == '__main__':
    pass
    test = P2peye()
    test.createFolder(test.htmlCacheFolder)
    print test.getListContent(test.start_url)

