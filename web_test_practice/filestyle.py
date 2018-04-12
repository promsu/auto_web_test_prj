#!/usr/bin/python
# -*- coding: utf-8 -*-
'''''
@author:freesigefei
Created on 2016年3月20日
Updated on 2016年5月4日
'''
# ------------------------------------------------------------------------------------------------
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os, time, re


def send_Test_email(mail_to):
    '''''本模块实现获取最新的测试报告html文件，读取部分报告内容作为邮件正文，将报告作为附件，并发送到指定的邮箱，
        参数mail_to代表的是接收邮箱，例如:'xxx@126.com' '''

    # 发送邮箱
    mail_from = 'yyy@sina.com'
    # 发送邮件主题
    mail_subject = 'Automation Test Report'
    # 发送邮箱服务器
    mail_smtpserver = 'smtp.sina.com'
    # 发送邮箱用户/密码
    mail_username = 'yyy@sina.com'
    mail_password = 'yyyyyy'

    # 定义邮件内容，中文需参数‘utf-8’，单字节字符不需要
    ''''' 
    #发送文件形式的邮件 
    msg = MIMEText('你好!','text','utf-8') 
    '''
    ''''' 
    #发送html形式以正常文本显示在邮件内容中的邮件 
    msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8') 
    '''
    ''''' 
    #读取html文件内容并发送 
    f=open(file_new,'rb') 
    mail_body=f.read() 
    f.close() 
    print mail_body 
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8') 
    '''

    # 创建一个带附件的邮件实例（内容）
    msg = MIMEMultipart()
    # 找到report目录下最新生成的报告文件供后续使用
    result_dir = 'D:\\report'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not
               os.path.isdir(result_dir + "\\" + fn) else 0)
    print(u'The Latest Test Report is: ' + lists[-1])
    file_new = os.path.join(result_dir, lists[-1])
    # 读取最新的测试报告文件获取部分信息来定义邮件的内容
    Regex_Theme = re.compile(r'Automation Test Report')
    Regex_Content = re.compile(r'<strong>(.*:)</strong>(.*)<')
    Report_File = open(file_new, 'r')
    Mail_Content = []
    for line in Report_File.readlines():
        if '<title>Automation Test Report</title>' in line or "<p class='attribute'>" in line:
            i = Regex_Theme.findall(line)
            j = Regex_Content.findall(line)
            if i != []:
                Mail_Content.append(i)
            if j != []:
                Mail_Content.append(j)
    Report_File.close()
    # 将读取到的测试报告的数据以html形式显示为邮件的中文
    msgTest = MIMEText('''''<html><h1>Test completed,Test results are as follows:</h1></html>'''
                       '''''<hr />'''
                       '''''<p><strong>''' + Mail_Content[0][0] + '''''</strong></p>'''
                                                                  '''''<p><strong>''' + Mail_Content[1][0][
                           0] + '''''</strong>''' + Mail_Content[1][0][1] + '''''</p>'''
                                                                            '''''<p><strong>''' + Mail_Content[2][0][
                           0] + '''''</strong>''' + Mail_Content[2][0][1] + '''''</p>'''
                                                                            '''''<p><strong>''' + Mail_Content[3][0][
                           0] + '''''</strong>''' + Mail_Content[3][0][1] + '''''</p>'''
                                                                            '''''<hr />'''
                                                                            '''''<p>PS: Detailed test results please refer to the attachment</p>'''
                       , 'html', 'utf-8')
    msg.attach(msgTest)
    # 定义邮件的附件
    att1 = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="Automation test report.html"'
    # 这里的filename指的是附件的名称及类型
    msg.attach(att1)
    # 将邮件的主题等相关信息添加到邮件实例
    msg['Subject'] = Header(mail_subject)
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    # 创建发送服务器实例并将发送服务器添加到实例中
    smtp = smtplib.SMTP()
    smtp.connect(mail_smtpserver)
    ''''' 
    #采用ssl加密传输 
    smtp.ehlo() 
    smtp.starttls() 
    smtp.ehlo() 
    '''
    ''''' 
    #打印交互的日志信息 
    #smtp.set_debuglevel(1) 
    '''
    # 登录发送邮件服务器并进行邮件的发送
    smtp.login(mail_username, mail_password)
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    print(u'Test report sent successfully，Please go to the following '
          u'email to check the test report :%s' % mail_to)
    smtp.quit()


# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    send_Test_email('xxx@126.com')
