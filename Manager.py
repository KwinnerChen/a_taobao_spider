#! usr/bin/evn python3
# -*- coding: utf-8 -*-

from URLMaker import URLMaker
from PageDownloader import PageDownloader
from HtmlParser import HtmlParser
from DataOutput import DataOutput
import config
from threading import Thread, RLock


def main(url, product_rule, mylock, dbname='taobao', collection_name='cellphone_info'):
    html = PageDownloader(url).gethtml()
    if html:
        datalist = HtmlParser(html).getdata(product_rule)
        if datalist:
            mylock.acquire() # 进程锁，保证每次只有一个进程在存储，以免数据出错
            DataOutput(db=dbname, collection=collection_name).save_info(datalist)
            mylock.release()

if __name__ == '__main__':
    mylock = RLock()
    flag = 0
    product = input('请输入要爬取的产品（默认为手机，其它产品需更改config中的解析规则）：')
    db = input('MongoDB数据库名称(默认为taobao)：')
    collection = input('MongoDB的集合名称(默认为cellphone_info）：')
    if not product or product == '手机':
        product_rule = config.PARSING_RULES.get('手机')
        for url in URLMaker(product='手机'):
            #main(url)
        #     p.apply_async(func=main, args=(url, product_rule, mylock))
        # p.close()
        # p.join()
            t = Thread(target=main, args=(url, product_rule, mylock))
            t.start()
        #t.join()
            # if db and collection:
            #     p = Process(target=main, args=(url, product_rule, mylock, db, collection))
            #     p.start()
            #     p.join()
            #
            # elif not db and not collection:
            #     p = Process(target=main, args=(url, product_rule, mylock,))
            #     p.start()
            #     p.join()
            #
            # elif db and not collection:
            #     p = Process(target=main, args=(url, product_rule, mylock, db))
            #     p.start()
            #     p.join()
            #
            # elif collection and not db:
            #     p = Process(target=main, args=(url, product_rule, mylock, 'taobao', collection))
            #     p.start()
            #     p.join()
    # elif product:
    #     product_rule = config.PARSING_RULES.get(product,'geterro')
    #     if product_rule == 'geterro':
    #         print('请先配置config中的解析规则！')
    #     else:
    #         for url in URLMaker(product='手机'):
    #             # main(url)
    #             # p.apply_async(func=main, args=(url, mylock))
    #             # t = Thread(target=main, args=(url,mylock))
    #             # t.start()
    #             # t.join()
    #             if db and collection:
    #                 p = Process(target=main, args=(url, product_rule, mylock, db, collection))
    #                 p.start()
    #
    #             elif not db and not collection:
    #                 p = Process(target=main, args=(url, product_rule, mylock,))
    #                 p.start()
    #                 p.join()
    #             elif db and not collection:
    #                 p = Process(target=main, args=(url, product_rule, mylock, db))
    #                 p.start()
    #                 p.join()
    #             elif collection and not db:
    #                 p = Process(target=main, args=(url, product_rule, mylock, 'taobao', collection))
    #                 p.start()
    #                 p.join()

