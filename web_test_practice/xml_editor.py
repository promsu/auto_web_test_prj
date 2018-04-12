#! /usr/bin/python3
#! -*- coding:utf-8 -*-


import xml.dom.minidom

f = open('C:/Users/AYYK/Desktop/mv.xml', 'r', encoding='utf-8')
strs = f.read()
doc = xml.dom.minidom.parseString(strs)
root = doc.documentElement
types = root.getElementsByTagName('type')
types[0].firstChild.data = '厉害了'
print(types[0].firstChild.data)
