import smtplib
import base64

filename = 'test.txt'
fo = open(filename, 'rb')
filecontent = fo.read()
encode = base64.b64decode(filecontent)
marker = "UNIQUEMARKER"

body ="""
this is body
"""
part1="""From: hank181017@gmail.com
To:hank181017@gmail.com
MIME-Version: 1.0
Content-type: multipart/mixed; boundary=%s
--%s
"""%(marker, marker)

part2="""Content-type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
"""%(body, marker)

part3="""Content-type: multipart/mixed; name=\ "%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment ; filename=%s

%s
--%s
"""%(filename, filename, encode, marker)

msg = part1 + part2 + part3 


to = 'sherry110534@gmail.com'
gmail_user = 'hank8760@gmail.com'
gmail_pwd = '87608760'

smptserver = smtplib.SMTP('smtp.gmail.com', 587)
smptserver.ehlo()
smptserver.starttls()
smptserver.ehlo
smptserver.login(gmail_user, gmail_pwd)

headers = 'To: ' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'


smptserver.sendmail(gmail_user, to, msg)
smptserver.close()