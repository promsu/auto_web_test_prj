#! -*- coding: utf-8 -*-


import os
from selenium import webdriver
import time
import random


class Screenshot:

    def __init__(self, driver):
        self.dr = driver
        self.filename = ''
        self.img_path = ''

    def get_filename(self):
        self.filename = time.strftime('%y%m%d%H%M%S') + '_' + '_' + str(random.randint(0, 10000))

    def get_imgdir(self):
        cur_path = os.getcwd()
        tmp_dir = os.path.dirname(os.path.dirname(cur_path))
        self.img_path = tmp_dir + '/reports/img/'+self.filename + '.png'

    def get_img(self, filename=''):
        self.filename = filename
        if len(self.filename) == 0:
            self.get_filename()
        self.get_imgdir()
        self.dr.get_screenshot_as_file(self.img_path)


if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.get('http://www.baidu.com')
    img = Screenshot(dr)
    img.get_img()
