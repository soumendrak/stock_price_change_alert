"""
Frequency: This program will run on every business day of NSE.
Function:  This program will send SMS/email if any of the provided
           stocks price decreased or increased more than 5% in a day.
Future scope: If stock price decreased/increased continuously (< 5 %)
              it will trigger email/SMS.
Author:     Soumendra Kumar Sahoo
Created on: 23 April 2017
"""
import json
from urllib import urlopen
from customizable_data import defined_limit, watchlist, number
from way2sms import send_sms
# import pdb
# import sys


def quote_grab(symbol):
    """
    Grab the stock and related information.
    :return:
        Stock price in float format
        Percentage changes in the share price
    """
    base_url = 'http://finance.google.com/finance/info?client=ig&q='
    url_data = urlopen(base_url + symbol)
    # [3:] is done to avoidthe initial `//`
    google_finance_data = json.loads(url_data.read().decode('ascii', 'ignore').strip()[3:])
    share_price_changes = float(google_finance_data[0]['cp_fix'])
    print ('Checking quotes for {}'.format(symbol))
    return share_price_changes


def main():
    """
    Invoke each share and trigger for SMS if the share price
    changed more than the defined percentage.
    """
    for each_share in watchlist:
        quote_price_change = quote_grab(each_share)
        print('{}:{}'.format(each_share, quote_price_change))
        if abs(quote_price_change) > defined_limit:
            if quote_price_change > 0:
                message = each_share + ' price has UP by ' + \
                    str(abs(quote_price_change)) + ' percent.'
            else:
                message = each_share + ' price has DOWN by ' + \
                    str(abs(quote_price_change)) + ' percent.'
            print('sending SMS for {}'.format(each_share))
            sms_status = send_sms(message, number)
            if sms_status:
                print('SMS for {} sent successfully'.format(each_share))
            else:
                print('SMS for {} Failed to go'.format(each_share))


if __name__ == '__main__':
    main()
