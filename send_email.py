import smtplib, time
import sys
from email.mime.text import MIMEText
from email.header import Header

def send_email_to_user(user):
    HOST = 'smtp.163.com'
    PORT = '465'
    USER = 'sam_ftp'
    passwd = 'OPPQBPHUNNEISJCZ'

    FROM = 'sam_ftp@163.com'
    TO = user + '@samsung.com'
#    TO = 'guoliang.hou@samsung.com'
#    TO = 'chuster2005@163.com'
#    SUBJECT = 'test email'
#    CONTENT = 'test email'
#    msg = '\n'.join(['From: {}'.format(FROM), 'To: {}'.format(TO), 'SUBJECT:{}'.format(SUBJECT), '', CONTENT])

    message = MIMEText('Your SSCR ftp account has been expired, please reapply it, thanks!')
    message['Subject'] = 'SSCR ftp account expired'
    message['From'] = FROM
    message['To'] = TO

    '''
    try:
      smtp_obj = smtplib.SMTP()
      smtp_obj.connect(host = HOST, port = PORT)
      res = smtp_obj.login(USER, passwd)
      ret = smtp_obj.sendmail(FROM, TO, message.as_string())
      print('send success:', "res = ", res, "ret = ", ret)
    except:
      print('send failed: ', "res = ", res)
    #  print('send failed')
    '''

    smtp_obj = smtplib.SMTP_SSL()
    smtp_obj.connect(host = HOST, port = PORT)
    res = smtp_obj.login(USER, passwd)
    ret = smtp_obj.sendmail(FROM, TO, message.as_string())
    #ret = smtp_obj.sendmail(FROM, TO, msg.encode('utf-8'))
    print( "res = ", res, "ret = ", ret)

if __name__ == '__main__':
  if (len(sys.argv) < 2):
    print('Too less args')
    sys.exit()
  user = sys.argv[1]
  send_email_to_user(user)

