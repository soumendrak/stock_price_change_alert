import urllib2
import cookielib
from customizable_data import username, password, number
# from stat import *


def send_sms(message='Hi', number=number):
    print('sending {} to {}'.format(message, number))
    assert len(message) < 136
    message = "+".join(message.split(' '))

# logging into the sms site
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username=' + username + '&password=' + password + '&Submit=Sign+in'

# For cookies

    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

# Adding header details
    opener.addheaders = [
        ('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    try:
        usock = opener.open(url, data)
    except IOError:
        print "error"

    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    for each_number in number:
        send_sms_data = 'ssaction=ss&Token=' + jession_id + \
            '&mobile=' + each_number + '&message=' + message + '&msgLen=136'
        print('send_sms_data', send_sms_data)
        opener.addheaders = [
            ('Referer', 'http://site25.way2sms.com/sendSMS?Token=' + jession_id)]
        try:
            sms_sent_page = opener.open(send_sms_url, send_sms_data)
            print "success"
            return True
        except IOError:
            print "error"
            return False


if __name__ == "__main__":
    message = "Hello again from Python"
    send_sms(message, number)
