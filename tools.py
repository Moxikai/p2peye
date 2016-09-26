#!/usr/bin/env python
#coding:utf-8
"""
渲染、缓存等公共函数
"""
import os,time

def makeFolder(path):
    """创建文件夹"""

def checkExitsPath(path):
    """检测文件、文件夹是否存在"""


def saveHtmlCache(content,path):
    """保存HTML缓存到文件"""
    try:
        with open(path,'w') as f:
            f.write(content)
            print '文件-----%s------保存完毕'%(path)
    except Exception as e:
        print '文件-------%s----------保存失败'%(path),e

def loadHtmlCache(path):
    """加载缓存文件"""
    try:
        with open(path,'r') as f:
            return f.read()
    except Exception as e:
        print '文件-------%s--------加载失败'%(path),e

def checkCacheInfo(path,expiretime):
    """核对网页是否过期"""
    mtime = os.path.getmtime(path)
    duration = time.time() - mtime
    if duration >= expiretime:
        """超过"""
        return True
    else:
        return False





