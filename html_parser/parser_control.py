# encoding=utf8
import sys
sys.path.append("..")

import threading
import time
import utils.tools as tools
import base.constance as Constance
from html_parser.parsers import *
from base.collector import Collector

db = tools.getConnectedDB()

class  PaserControl(threading.Thread):
    def __init__(self):
        super(PaserControl, self).__init__()
        self._collector = Collector()
        self._urlCount = int(tools.getConfValue("html_parser", "url_count"))
        self._interval = int(tools.getConfValue("html_parser", "sleep_time"))

    def run(self):
        while True:
            urls = self._collector.getUrls(self._urlCount)
            print("取到的url大小 %d"%len(urls))
            for url in urls:
                self.parseUrl(url)

            time.sleep(self._interval)

    def parseUrl(self, urlInfo):
        website_id = urlInfo['website_id']

        domain = list(db.website.find({'_id':website_id}))[0]['domain']
        if domain == Constance.YOUKU:
            youku.parseUrl(urlInfo)
        elif domain == Constance.TENCENT:
            tencent.parseUrl(urlInfo)
        elif domain == Constance.WANG_YI:
            wangyi.parseUrl(urlInfo)
        elif domain == Constance.PPTV:
            pptv.parseUrl(urlInfo)
        elif domain == Constance.KAN_KAN:
            kankan.parseUrl(urlInfo)
        elif domain == Constance.CCTV:
            cctv.parseUrl(urlInfo)
        elif domain == Constance.TUDOU:
            tudou.parseUrl(urlInfo)
        elif domain == Constance.V1:
            v1.parseUrl(urlInfo)
        elif domain == Constance.KU6:
            ku6.parseUrl(urlInfo)