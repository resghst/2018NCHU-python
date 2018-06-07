import smtplib
smptserver = smtplib.SMTP('smtp.gmail.com', 587)
smptserver.ehlo()
smptserver.starttls()
smptserver.ehlo
smptserver.login(gmail_user, gmail_pwd)

headers = 'To: ' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print headers
msg = headers + """From: hank181017@gmail.com
To:hank181017@gmail.com
MIME-Version: 1.0
Content-type: text/html
<h1>hi</h1><h2>hello</h2>
"""

smptserver.sendmail(gmail_user, to, msg)
smptserver.close()