# -*- coding: UTF-8 -*-
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.image import MIMEImage
from email.utils import formataddr
import io
class EmailReport():

    def sendEmail(self,path):
        print("report from "+str(path))
        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "977820015@qq.com"  # 用户名
        mail_pass = "oaaceexvgidbbcjf"  # 口令

        sender = '977820015@qq.com'

        receivers = ['2321628281@qq.com', '390485519@qq.com',
                     '1937826409@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 ,

        msgRoot = MIMEMultipart('related')

        # msgRoot['From'] = Header("发送人", 'utf-8')
        msgRoot['From'] = formataddr(["liwei.xu_TestReport", sender])

        msgRoot['To'] = ','.join(receivers)  # 注意
        subject = '自动化测试报告'
        msgRoot['Subject'] = Header(subject, 'utf-8')

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        file = path
        with open(file, encoding='utf-8') as f:
            message = f.read()
        msgAlternative.attach(MIMEText(message, 'html', 'utf-8'))

        message = MIMEText(open(file, 'rb').read(), 'base64', 'utf8')
        message.add_header('content-disposition', 'attachment', filename='TestReport.html')
        msgRoot.attach(message)

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, msgRoot.as_string())
            print("邮件发送成功")

        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

        msg="sendEmail success"
        return msg

    def sendErrorEmail(self,path):
        print("report from "+str(path))
        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "977820015@qq.com"  # 用户名
        # mail_pass = "oaaceexvgidbbcjf"  # 口令
        mail_pass = "ehgymfjlhkbcbchh"  # 口令

        sender = '977820015@qq.com'

        receivers = ['1937826409@qq.com','xuliwei@bringbuys.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱 ,

        msgRoot = MIMEMultipart('related')

        # msgRoot['From'] = Header("发送人", 'utf-8')
        msgRoot['From'] = formataddr(["liwei.xu_TestReport", sender])

        msgRoot['To'] = ','.join(receivers)  # 注意
        subject = '服务监测'
        msgRoot['Subject'] = Header(subject, 'utf-8')

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        file = path
        with open(file, 'r',encoding='utf-8') as f:
            message = f.read()
        msgAlternative.attach(MIMEText(message, 'html', 'utf-8'))

        message = MIMEText(open(file, 'rb').read(), 'base64', 'utf8')
        # message.add_header('content-disposition', 'attachment', filename='TestReport.html')
        msgRoot.attach(message)

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, msgRoot.as_string())
            print("邮件发送成功")

        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

        msg="sendEmail success"
        return msg
