## Send to addresses passed on stdin
import sys, time
from random import randint
import argparse
import yaml
import spambot

with open ('settings.yaml') as fp:
    settings = yaml.load (fp.read())
    assert 'from' in settings


parser = argparse.ArgumentParser()
parser.add_argument ('-s', '--subject', required=True)
parser.add_argument ('-r', '--reply-to')
args = parser.parse_args()


msg = spambot.EmailMessage ('body.html', 'body.txt')
msg['From'] = settings['from']
msg['Subject'] = unicode (args.subject, 'utf-8')
if args.reply_to:
    msg['Reply-to'] = args.reply_to


# Read email addresses from stdin and send email
spammer = spambot.Sender()
for line in sys.stdin:
    recipient = line.strip()
    del msg['To']
    msg['To'] =  recipient
    print 'Sending to ' + recipient
    sys.stdout.flush()
    spammer.send (msg, recipient)
    spammer.wait(10, 5)    # slow down, to appear less spammy


print '- The End -'
