#! usr/bin/evn python3
# -*- coding: utf-8 -*-

import pymongo

class DataOutput(object):
    '''
        一个本地的MongoDB对象，可以支持多个数据库实例，可以更改链接的数据库名称和集合名称。
        如：
        >>>DataOutput(db='computer', collection='notebook')
        save_info(datalist)方法应该接受的是一个字典的列表或元组或其它可迭代对象
    '''
    def __init__(self, db, collection):
        self.clint = pymongo.MongoClient()
        self.db = self.clint[db]
        self.collection = self.db[collection]

    def save_info(self, datalist):
        if datalist:
            for one in datalist:
                self.collection.insert(one)
        else:
            print('数据集合为空')

    def finddata(self, command):
        for one in self.collection.find(command):
            print(one)

if __name__ == '__main__':
    adata = DataOutput()
    adata.save_info([{'name': '努比亚 Z17', 'price': '2404', 'summary': ['2倍变焦双摄', '低音炮扬声器', '智能防水']}, {'name': 'vivo Y79', 'price': '1912', 'summary': ['全面屏2.0', '2400万 * 更美更清晰']}, {'name': '华为 麦芒6', 'price': '1883', 'summary': ['前置智能柔光双摄', '出彩四镜头']}, {'name': '锤子 坚果Pro', 'price': '1150', 'summary': ['智能语义拖拽', '闪念胶囊', '自定义来电语音']}, {'name': 'OPPO A79', 'price': '2099', 'summary': ['全面屏，才貌双全', '前后1600万，前后都精彩', '存储更大，运行更快']}, {'name': '荣耀 畅玩6', 'price': '596', 'summary': ['前置500万柔光自拍', '人体工程学设计', '大字体，轻松用']}, {'name': '诺基亚 诺基亚 6 第二代', 'price': '1354', 'summary': ['双视野模式', '空间声音捕捉技术']}, {'name': '华为 P10', 'price': '2772', 'summary': ['徕卡人像摄影', '多彩外观设计 ', '3D面部检测']}, {'name': '努比亚 Z17 mini', 'price': '1173', 'summary': ['背景虚化景深摄影', '超级截图', '9种滤镜10级美颜']}, {'name': '美图 M8S', 'price': '2832', 'summary': ['前置双像素双摄像头', 'PDAF疾速对焦', 'OIS光学防抖']}, {'name': '华为 畅享6S', 'price': '749', 'summary': ['轻薄金属机身', '指纹多用途', '省电低耗能']}, {'name': '360手机 N6', 'price': '994', 'summary': ['0.1s快速相位对焦', '高功率快充']}, {'name': '华为 P10 Plus', 'price': '3000', 'summary': ['每一拍都是大片', '金属钻雕工艺', '简约设计']}, {'name': '美图 M8', 'price': '2351', 'summary': ['人工智能自拍', '六曲面3D玻璃机身']}, {'name': '美图 V6', 'price': '5950', 'summary': ['双像素双摄像头', '独家影像黑科技，每一拍都是大片']}, {'name': '华为 NOVA 2', 'price': '1552', 'summary': ['前置2000万高清美拍', '纤薄设计精致美学', '专业级音质，3D环绕音效']}, {'name': '360手机 N6 Lite', 'price': '803', 'summary': ['精美金属机身', '双频Wi-Fi']}, {'name': '索尼 Xperia XZ Premium', 'price': '3859', 'summary': ['4K HDR显示屏', '凝时慢拍', '防水防尘']}, {'name': 'OPPO A73', 'price': '1710', 'summary': ['超清全面屏更大更清晰', '前置1600万智慧美颜']}, {'name': '华为 Mate 9 Pro', 'price': '3141', 'summary': ['快充慢用', '金融级安全芯片', '2K双曲面屏']}, {'name': '诺基亚 诺基亚7 ', 'price': '1457', 'summary': ['3D康宁玻璃机身', '双视野拍摄，反正都更美']}, {'name': 'vivo Y66i', 'price': '1198', 'summary': ['智慧解锁，面部识别', '分屏多任务2.0']}, {'name': '魅族 魅蓝E2', 'price': '806', 'summary': ['天线闪光灯', '4LED闪光灯', '按压式指纹识别']}, {'name': '华为 NOVA 2 PLUS', 'price': '2040', 'summary': ['光学变焦双镜头', '前置暗光拍摄', '纤薄设计精致美学']}, {'name': '三星 Galaxy C9 Pro', 'price': '2165', 'summary': ['环绕音响，动感体验', '畅享多媒体', '全铝机身薄至6.9mm']}, {'name': '魅族 PRO7 Plus', 'price': '2300', 'summary': [' 配置IMX386 镜头', '双屏联动 别样出彩']}, {'name': '荣耀 V9', 'price': '2106', 'summary': ['双1200万像素平行镜头', '2K高清屏', '性能怪兽']}, {'name': '华为 NOVA 青春版', 'price': '1276', 'summary': ['柔光护眼屏', '快充10分钟追剧2小时', ' 精致双面2.5D弧面玻璃']}, {'name': '荣耀 荣耀8青春版', 'price': '1030', 'summary': ['2.5D玻璃机身', '0.3s指纹解锁', '十级美肤']}, {'name': '魅族 魅蓝5s', 'price': '646', 'summary': ['CNC金属机身', '新全网通 VoITE高清语音', 'mCharge 快充']}, {'name': '努比亚 Z17S', 'price': '2985', 'summary': ['无边框全面屏', 'AI人像2.0', '全像素极速对焦']}, {'name': '华为 Mate 9', 'price': '2754', 'summary': ['2倍双摄变焦', '4Mic降噪丽音', '化繁为简，交互革命']}, {'name': 'vivo X9s Plus', 'price': '2239', 'summary': ['2000万柔光双摄', '内置震撼HIFI音效', '便捷一屏两用']}, {'name': '诺基亚 新105', 'price': '150', 'summary': ['独立按键一键拨号', 'LED手电筒']}, {'name': '荣耀 畅玩6A', 'price': '742', 'summary': ['高颜值金属机身', '高清大屏 护眼新主张', '多功能指纹识别']}, {'name': '创星 S1', 'price': '146', 'summary': ['强悍三防', '持久续航']}, {'name': '荣耀 畅玩6X', 'price': '964', 'summary': ['曲面金属，指纹识别', '轻松背景虚化', '智能防伪基站']}, {'name': 'vivo Xplay6', 'price': '3370', 'summary': ['4弧面3D玻璃', '景深虚化双摄', 'ECO节能引擎']}, {'name': '美图 T8', 'price': '2827', 'summary': ['双像素前置摄像头', '前置OIS光学防抖']}, {'name': '华为 NOVA', 'price': '1091', 'summary': ['实时美妆自拍', '小体积大容量', '高能低耗，强劲芯片硬实力']}, {'name': '小米 红米4X', 'price': '641', 'summary': ['高画质相机', '隐私双系统', '18天待机']}, {'name': '小米 MIX', 'price': '2627', 'summary': ['6.4英寸全面屏', '超声波距离传感器', '全陶瓷机身']}, {'name': '索尼 Xperia XZ1', 'price': '3002', 'summary': ['HDR高清屏幕', '追踪对焦连拍']}, {'name': '波导 A520', 'price': '173', 'summary': ['大字大声', '高清横屏', 'LED强光双手电筒']}, {'name': 'vivo X9', 'price': '1879', 'summary': ['前置2000万柔光双摄', '金属流线机身']}, {'name': '天语 X11', 'price': '538', 'summary': ['HIFI原声技术', '0.1s极速指纹解锁']}, {'name': '魅族 PRO 6 Plus', 'price': '1604', 'summary': ['AOD息屏显示技术', '四轴光学防抖']}, {'name': '三星 SM-W2018', 'price': '11389', 'summary': ['金属双轴一体成型', '双核疾速对焦']}])
    