#! usr/bin/evn python3
# -*- coding: utf-8 -*-

import requests, re, random, os
# import json

'''一个简单的代理IP池，代理IP以文本存储。实例化一个代理池，使用get_ip()方法可以随机返回一个字典，包括协议类型和IP端口。
   如{'http': 'http://1.2.3.4:4'},可直接用于requests的proxies参数。
   或者使用get_ips()方法一次返回一个字典列表。
   目前只有使用了一个在线代理网址的数据，所以协议类型还有IP较少。
   如果IPPool文件夹下没有IP.txt文件，可以运行一次IPPool.py，或者直接创建如下的文本文件保存为IP.txt：
   1.2.3.4：5
   2.3.4.5：6
   ...
   '''

class IPPool():
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0'}
        self.url = 'http://www.66ip.cn/nmtq.php?getnum=&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=0&proxytype=0&api=66ip'
        self.iplist = []
        self.file_path = os.path.join(os.path.dirname(__file__), 'IP.txt')
        
    def _pagedownloader(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            html = response.text
            return html
        except:
            print('链接不可用，请更换链接！')

    def _ip_parse(self, html): # 生成器用于提取IP
        html_list = html.split('<br />')
        for html_cut in html_list:
            ip = re.search(r'((25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})\.){3}(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2}):\d+', html_cut)
            if ip:
                yield ip.group()

    def _ip_test(self, ip): # 用于测试IP是否可用
        try:
            response = requests.get('http://www.baidu.com', headers=self.headers, timeout=5)
            response.raise_for_status()
            return ip
        except:
            return None

    def ip_refresh(self): # 用于更新IP数据
        html = self._pagedownloader()
        with open(self.file_path, 'w') as file:
            for ip in self._ip_parse(html):
                result = self._ip_test(ip)
                if result:
                   file.write('%s\n' % result)

    def get_ip(self):
        try:
            with open(self.file_path, 'r') as file:
                iplist = file.readlines()
                return {'http':'http://%s' % random.choice(iplist).strip()}
        except:
            print('检查IPPool文件夹下是否有IP.txt文件，没有请先运行IPPool.py，更新IP文件。')

    def get_ips(self):
        try:
            with open(self.file_path, 'r') as file:
                iplist = file.readlines()
                for ip in iplist:
                    self.iplist.append({'http':'http://%s' % random.choice(iplist).strip()})
                return self.iplist
        except:
             print('检查IPPool文件夹下是否有IP.txt文件，没有请先运行IPPool.py，更新IP文件。')

if __name__ == '__main__':
    ip = IPPool()
    for i in range(10):
        print(ip.get_ip())
