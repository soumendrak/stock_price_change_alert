"""
This function is used to send SMS via way2sms.com
"""
from __future__ import print_function
import urllib2
import cookielib
from customizable_data import username, password, number


def send_sms(message='Hi', number=number):
    try:
        print('sending {} to {}'.format(message, number))
        assert len(message) < 136
        message = "+".join(message.split(' '))
    # logging into the sms site
        url = 'http://site24.way2sms.com/Login1.action?'
        data = 'username=' + username + '&password=' + \
            password + '&Submit=Sign+in'

        # For cookies
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

        # Adding header details
        opener.addheaders = [
            ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
        try:
            opener.open(url, data)
        except IOError:
            print("error while opening the headers")

        jession_id = str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        for each_number in number:
            send_sms_data = 'ssaction=ss&Token=' + jession_id + \
                '&mobile=' + each_number + '&message=' + message + \
                '&msgLen=136'
            # print('send_sms_data', send_sms_data)
            opener.addheaders = [
                ('Referer', 'http://site25.way2sms.com/sendSMS?Token=' +
                    jession_id)]
            try:
                opener.open(send_sms_url, send_sms_data)
                print("SMS has been sent successfully")
                return True
            except IOError:
                print("There is error in sending the message")
                return False
    except Exception as error_message:
        print('Message sending failed:', error_message)


if __name__ == "__main__":
    message = "Hello again from Python"
    send_sms(message, number)
