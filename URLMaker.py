#! usr/bin/evn python3
# -*- coding: utf-8 -*-
# author: Kwinner Chen


import config, datetime
import urllib.parse


class URLMaker(object):
    '''这是一个链接生成器，输入产品名称后可迭代生成目标链接,可以迭代，或者使用next（）函数得到下一链接。如链接无效，需更改config的链接规则
       如：
       >>>for url in URLMaker('手机'):
       或者：
       >>>product_url= URLMaker('手机')
       >>>nexturl = next(product_url)
       '''

    def __init__(self, product):
        self.product = urllib.parse.urlencode({'q':'%s' % product})
        self.flag = 0

    def __iter__(self):
        return self

    def __next__(self):
        pagenum = self.flag * 48
        url = config.BASE_URL.format(self.product, str(pagenum))
        self.flag += 1
        if self.flag <= 100:
            return url
        else:
            raise StopIteration

if __name__ == '__main__':
    product = config.PARSING_RULES.popitem()[0]
    product_url = URLMaker(product)
    for i in product_url:
        print(i)