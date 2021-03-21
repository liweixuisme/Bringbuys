# coding=UTF-8
import re
import time
import requests
# from bs4 import BeautifulSoup
from urllib import parse
import os

def mkdir(path):
    # 引入模块
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False

def loadProductPic(productName,productPicUrl,file_path):
    try:
        goodName = productName.replace('*', 'X')
        name = "S1S1"
        # file_path = "D:\\QianZhangGui_PROJECT\\DATAS\\picFromJD"
        # 获得图片后缀
        file_suffix = os.path.splitext(productPicUrl)[1]

        # 拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path, os.sep, name, file_suffix)

        # 下载图片，并保存到文件夹中
        # urllib.request.urlretrieve(productPicUrl, filename=filename)

        newFileName = os.path.join(file_path, goodName + file_suffix)
        print(newFileName)
        os.rename(filename, newFileName)
    except:
        print("wrong with storing productPic")
        pass

def getCartUrl(): #根据全部分类接口获取所有分类url

    url="https://www.jd.com/allSort.aspx"
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    }
    r=requests.get(url,headers=headers)
    rp=r.text
    rule=re.compile('href="(?P<cats>.*?cat=.*?)" ')
    cartUrl=rule.findall(rp)
    return cartUrl

def getSkuUrl(cartUrl): #传入分类url列表，遍历获取分类下的skuId

    n=1
    while n:
        url = "https://list.jd.com/list.html?cat=1713,4855,4864&page=%s"%str(n)
        print(url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
        }
        r = requests.get(url, headers=headers)
        rp = r.text
        rule = re.compile('href="(?P<cats>//item.jd.com.*?.html)"')
        skuUrl = rule.findall(rp)
        n+=1
        return skuUrl

def getSkuPrice(skuId):
    url='https://p.3.cn/prices/mgets?callback=jQuery2518200&source=jshop&origin=1&area=19_1609_41655_0&skuids=J_981759'
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    rp = r.text
    print(rp)
    rule = re.compile("skuid:[ ]*(?P<skuid>.*?)[,].*?skuid:[ ]*")
    productInfo = rule.findall(rp)
    # print(productInfo)

def getSkuDetailPic(skuId):
    url='https://cd.jd.com/description/channel?skuId=100003311380&mainSkuId=100003311380&charset=utf-8&cdn=2&callback=showdesc'
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    rp = r.text
    rule = re.compile("(?P<skuDetailPic>//img30.360buyimg.com.*?)\)")
    skuDetailPic = rule.findall(rp)
    return skuDetailPic

def getSkuCommonInfo(skuId):     #根据 sku 链接 获取sku商品信息： 商品名称、商品主图、商品分类 等

    url=''.join(['https:','//item.jd.com/100006180837.html'])
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    rp = r.text
    # print(rp)
    rule = re.compile("skuid:[ ]*(?P<skuid>.*?)[,].*?name:[ ]*'(?P<name>.*?)'[,].*?src:[ ]*'(?P<src>.*?)'[,].*?imageList:[ ]*(?P<imageList>\[.*?\]).*?cat:[ ]*(?P<cat>\[.*?\]).*?catName:[ ]*(?P<catName>\[.*?\])",flags=re.S)
    skuCommonInfo = rule.search(rp)
    dic={}
    dic['skuid']=skuCommonInfo.group('skuid')
    dic['name']=skuCommonInfo.group('name')
    dic['src']=skuCommonInfo.group('src')
    dic['imageList']=skuCommonInfo.group('imageList')
    dic['cat']=skuCommonInfo.group('cat')
    dic['catName']=skuCommonInfo.group('catName')

    return dic

def getAllSkuInfo():
    skuInfo=getSkuCommonInfo('d')
    # price=getSkuPrice('d')
    detailPic=getSkuDetailPic('d')
    # skuInfo['price']=price
    skuInfo['detailPic']=detailPic
    return skuInfo

def getNum(skuId):
    url='https://trioprima.net/pt/provider/mem/game/results/B1SC?timestamp=1614655688085&timestamp=1614655688085&lang=zh-cn&gametype=B1SC&search_type=0&per_limit=30&page=1'
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    }
    r = requests.get(url, headers=headers)
    rp = r.text
    rule = re.compile("(?P<skuDetailPic>//img30.360buyimg.com.*?)\)")
    skuDetailPic = rule.findall(rp)
    return skuDetailPic


if __name__ == '__main__':
    # file_path = "/Users/xuliwei/Downloads/QianZhangGui_PROJECT/DATAS/picFromJD/toy"
    # rp=getProductData('玩具',file_path)
    # # print(rp)
    # rule=re.compile('href="(?P<urls>//item.jd.com/.*html)')
    # rp=rule.findall(rp)
    # for url in rp:
    #     print(url)

    rp=getAllSkuInfo()

    print(rp)
    print(rp['imageList'])
    print(rp['detailPic'])
