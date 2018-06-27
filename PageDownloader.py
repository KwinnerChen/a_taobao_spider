#! usr/bin/evn python3
# -*- coding: utf-8 -*-
# author: Kwinner Chen


import requests, config, random
from IP.IPPool import IPPool


class PageDownloader(object):
    '''页面下载器，返回链接相应页面，如果链接错误，则返回None'''
    def __init__(self):
        self.headers = {'User-Agent':'%s' % random.choice(config.USER_AGENTS)}

    def gethtml(self, url, proxy):
        try:
            response = requests.get(url, proxy, headers=self.headers, timeout=5)
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
    html = PageDownloader().gethtml('https://s.taobao.com/search?q=手机&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180318&ie=utf8&p4ppushleft=5%2C48&s=96',{'http': 'http://183.252.17.81:63000'})
    print(html[0:100])


