#! usr/bin/evn python3
# -*- coding: utf-8 -*-
# author: Kwinner Chen


import re, config


class DataError(Exception): # 自定义一个错误类型，遇到空信息的时候抛出，以停止收集。
    
    def __str__(self):
        return '此处没有提取到数据'
    __repr__ = __str__


class HtmlParser(object):

    def __init__(self, html):
        self.html = html
        
    def getdata(self, product_rule):  # 用三个内置方法，分别提取相应字段，遇到空信息抛出错误
        '''
           product_rule是一个字典类型，包含了提取的字段及对应的正则表达式
        '''
        datalist = []
        if self.html:
            for strcut in self.html.split(config.HTML_SPLIT_RULE):
                try:
                    dictinfo = {}
                    dictinfo['name'] = self._getname(strcut, product_rule)
                    dictinfo['price'] = self._getprice(strcut, product_rule)
                    dictinfo['summary'] = self._getsummary(strcut, product_rule)
                    datalist.append(dictinfo)
                except Exception as e:
                    print('此处没有信息被收集，可能信息不完整，或%s' % e)
            return datalist
        else:
            print('页面为空，未提取到数据')
            return datalist

    def _getname(self, strcut, product_rule):
        nameslist = re.findall('%s' % product_rule['title'], strcut)
        if nameslist:
            print('提取到名称%s' % nameslist[0])
            return nameslist[0]
        else:
            raise(DataError)

    def _getprice(self, strcut, product_rule):
        pricelist = re.findall('%s' % product_rule['price'], strcut)
        if pricelist:
            print('提取到价格%s' % pricelist[0])
            return pricelist[0]
        else:
            raise(DataError)

    def _getsummary(self, strcut, product_rule):
        summarylist = re.findall('%s' % product_rule['summary'], strcut)
        if summarylist:
            print('提取到简介')
            return summarylist
        else:
            raise(DataError)

if __name__ == '__main__':
    from PageDownloader import PageDownloader
    html = PageDownloader().gethtml('https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&p4ppushleft=5%2C48&s=48',{'http': 'http://183.252.17.81:63000'})
    page = HtmlParser(html)
    rul = config.PARSING_RULES.popitem()
    dictinfo_one = page.getdata(rul[1])
    print(dictinfo_one)