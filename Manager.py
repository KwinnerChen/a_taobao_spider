#! usr/bin/evn python3
# -*- coding: utf-8 -*-
# author: Kwinner Chen


from URLMaker import URLMaker
from DataOutput import DataOutput
from IP.IPPool import IPPool
from threading import Thread
from queue import Queue
import config, os


def parser(q_url, product_rule, q_r, iplist):

    from PageDownloader import PageDownloader
    from HtmlParser import HtmlParser
    import random


    while True:
        url = q_url.get()
        if url is None:
            break
        html = PageDownloader().gethtml(url, random.choice(iplist))
        if html:
            parser_page = HtmlParser(html)
            datalist = parser_page.getdata(product_rule)
            if datalist:
                q_r.put(datalist)
        q_url.task_done()  # 标示该次任务完成

def storage(q_r, db):
    while True:
            r = q_r.get()
            if r is None:
                break
            db.save_info(r)
            


if __name__ == '__main__':
    l_t = []
    dic_rule = config.PARSING_RULES.popitem()
    urlmaker = URLMaker(dic_rule[0])
    q_url = Queue()  # 任务列队，用于信息解析提取
    q_r = Queue()  # 结果列队，用于存储
    db = DataOutput(dbname=config.DB_STRUCTOR['dbname'], collection=config.DB_STRUCTOR['col_name'])
    iplist = IPPool().get_ips
    rul = dic_rule[1]

    for i in range(os.cpu_count()):  # 创建任务线程
        t = Thread(target=parser, args=(q_url, rul, q_r, iplist))
        t.start()
        l_t.append(t)

    t1 = Thread(target=storage, args=(q_r, db))  # 创建存储线程
    t1.start()

    for url in urlmaker:  # 向任务列队中添加任务
        q_url.put(url)

    q_url.join()  # 待所有任务完成

    for i in range(os.cpu_count()):  # 向任务列队中添加任务结束标识
        q_url.put(None)

    for t in l_t:  # 等待所有任务线程完成过
        t.join()

    q_r.put(None)  # 向存储列队中添加结束标志
    t1.join() # 待存储线程完成
    db.clint.close()
    print('爬取完成！')
