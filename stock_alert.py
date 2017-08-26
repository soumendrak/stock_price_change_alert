"""
Frequency: This program will run on every business day of NSE.
Function:  This program will send SMS/email if any of the provided
           stocks price decreased or increased more than 5% in a day.
Future scope: If stock price decreased/increased continuously (< 5 %)
              it will trigger email/SMS.
Author:     Soumendra Kumar Sahoo
Created on: 23 April 2017
"""
from __future__ import print_function

import json
from urllib import urlopen

from customizable_data import defined_limit, number, watchlist
from way2sms import send_sms


# import pdb
# import sys


class SharePrice:

    def __init__(self, share):
        self.share = share

    def quote_grab(self):
        """
        Grab the stock and related information.
        :return:
            Percentage changes in the share price
        """
        try:
            base_url = 'http://finance.google.com/finance/info?client=ig&q='
            url_data = urlopen(base_url + self.share)
            # [3:] is done to avoid the initial `//`
            google_finance_data = json.loads(url_data.read().decode(
                'ascii', 'ignore').strip()[3:])
            share_price_change = float(google_finance_data[0]['cp_fix'])
            self.share_price_change = share_price_change
            print('Checking quotes for {}'.format(self.share))
            return share_price_change
        except Exception as error_message:
            print('Parsing the share failed:', error_message)
            return None

    def check_further_status(self):
        """
        Check whether the share price has been changed further defined_limit
        If changed
        """
        pass

    def is_share_price_changed_above_limit(self):
        """
        Status depending on the fluctuations on defined limit
        :return: True or False
        """
        return abs(self.share_price_change) > defined_limit

    def is_increased(self):
        """
        Return whether share price increased or decreased
        """
        return self.share_price_change > 0

    def notify_user(self, key_message):
        message = self.share + ' price has ' + key_message + ' by ' + \
            str(abs(self.share_price_change)) + ' percent.'
        print('sending SMS for {}'.format(self.share))
        sms_status = send_sms(message, number)
        if sms_status:
            print('SMS for {} sent successfully'.format(self.share))
        else:
            print('SMS for {} Failed to go'.format(self.share))


def main():
    """
    Invoke each share and trigger for SMS if the share price
    changed more than the defined percentage.
    """
    try:
        for each_share in watchlist:
            share_obj = SharePrice(each_share)
            quote_price_change = share_obj.quote_grab()
            if share_obj.is_share_price_changed_above_limit():
                if share_obj.is_increased():
                    share_obj.notify_user('UP')
                else:
                    share_obj.notify_user('DOWN')
            print('{}:{}'.format(each_share, quote_price_change))
    except Exception as error_message:
        print('Calculating the share percentage failed:', error_message)


if __name__ == '__main__':
    # Invoke the main call in every 15 minutes by scheduler
    main()
