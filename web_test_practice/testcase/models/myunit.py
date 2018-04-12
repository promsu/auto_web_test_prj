#! -*- coding: utf-8 -*-


from selenium import webdriver
import unittest


class Myunit(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(10)
        self.dr.maximize_window()

    def tearDown(self):
        self.dr.quit()
