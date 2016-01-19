from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
#import settings


def EmailMessage (htmlfile, textfile):  # rename Email?
    """Factory function"""
    with open(htmlfile) as fp:
        body_html = fp.read()
    with open(textfile) as fp:
        body_text = fp.read()
    return multipart_email (body_html, body_text)


def multipart_email (body_html, body_text):
    msg = MIMEMultipart ('alternative')
    msg['Date'] =       formatdate (localtime=True)
    msg['To'] =         None
    # RFC 2046 says: the last part of a multipart message is the preferred.
    msg.attach (MIMEText (body_text, 'plain', _charset='utf-8'))
    msg.attach (MIMEText (body_html, 'html',  _charset='utf-8'))
    return msg



import smtplib
from random import randint

class Sender (object):

    def __init__ (self, host='localhost', port=587,
                  username=None, password=None, debug=False):
        if host == 'localhost':
            smtp = smtplib.SMTP (host)
        else:
            smtp = smtplib.SMTP (host, port)
            smtp.starttls()
            if username and password:
                smtp.login (username, password)
        smtp.set_debuglevel (debug)
        self.smtp = smtp

    def send (self, message, recipient):
        try:
            self.smtp.sendmail (message['From'], recipient, message.as_string())
        except smtplib.SMTPException as e:
            #print 'ERROR sending to', recipient
            print 'ERROR sending to: ' + recipient
            print '--- Exception ---'
            print e
            print '-----------------'
            return False
        return True

    def close (self):
        self.smtp.quit()

    def wait (self, mu=60, sigma=30):
        """Wait random amount to appear less spammy"""
        time.sleep (mu + randint(-sigma,sigma))
