## Send to addresses passed on stdin
import sys, time
from random import randint
import argparse
import yaml
import spambot

settings = {
    'host': 'localhost',
    'port': 25,
    'username': None,
    'password': None,
#    'debug': False,
#    'reply-to': None,
}

with open ('settings.yaml') as fp:
    settings.update (yaml.load (fp.read()))
    assert 'from' in settings

#from pprint import pprint
#pprint (settings)
#exit(1)


parser = argparse.ArgumentParser()
parser.add_argument ('-s', '--subject', required=True)
parser.add_argument ('-r', '--reply-to')
args = parser.parse_args()


msg = spambot.EmailMessage ('body.html', 'body.txt')
msg['From'] = settings['from']
msg['Subject'] = unicode (args.subject, 'utf-8')
if args.reply_to:
    msg['Reply-to'] = args.reply_to


#spammer = spambot.Sender()
spammer = spambot.Sender (host = settings['host'],
                          port = settings['port'],
                          username = settings['username'],
                          password= settings['password'])
#spammer = spambot.Sender (**settings)  # unexpected keyword argument 'from'

# Read email addresses from stdin and send email
for line in sys.stdin:
    recipient = line.strip()
    del msg['To']
    msg['To'] =  recipient
    print 'Sending to ' + recipient
    sys.stdout.flush()
    spammer.send (msg, recipient)
    spammer.wait(10, 5)    # slow down, to appear less spammy


print '- The End -'
