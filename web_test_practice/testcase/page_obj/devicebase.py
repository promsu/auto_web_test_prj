#! -*- coding: utf-8 -*-


from selenium import webdriver


class BaiduSearch():

    def __init__(self, url):
        self.dr = webdriver.Chrome()
        self.url = url
        self.title = ''
        self.dr.get(self.url)

    def get_title(self):
        self.title = self.dr.title
        return self.title

    def send_keys(self, sendkeys):
        testarea = self.dr.find_element_by_id('kw')
        testarea.send_keys(sendkeys)
        self.dr.find_element_by_id('su').click()
        if self.dr.find_element_by_id('kw').get_attribute('value') == sendkeys:
            return True
        return False






