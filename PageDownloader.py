#! usr/bin/evn python3
# -*- coding: utf-8 -*-

import requests, config, random
from IPPool import IPPool

class PageDownloader(object):
    '''页面下载器，返回链接相应页面，如果链接错误，则返回None'''
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent':'%s' % random.choice(config.USER_AGENTS)}
        self.ippool = IPPool()

    def gethtml(self):
        try:
            proxy_ip = self.ippool.get_ip()
            response = requests.get(self.url, headers=self.headers, proxies=proxy_ip, timeout=5)
            response.raise_for_status()
            response.encoding = 'utf-8'
            html = response.text
            print('%s页面已被下载' % response.url)
        except Exception as e:
            print('下载页面时出现错误:%s' % e)
            html = None
        finally:
            return html

if __name__ == '__main__':
    pagedownloader = PageDownloader('https://s.taobao.com/search?q=手机&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180318&ie=utf8&p4ppushleft=5%2C48&s=96')
    html = pagedownloader.gethtml()
    print(html[0:100])


