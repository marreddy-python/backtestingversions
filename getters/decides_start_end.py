import requests,json,time,urllib2

import sys
sys.dont_write_bytecode=True

def decide_start_end():

    url = 'http://52.14.190.48/api/v1/price_histories/get_stock_data?stock_symbol=TVIX'

    r = requests.post(url)
    a = r.json()
    # stock_data = a['result']

    start_date = a['result'][0][0]
    end_date = a['result'][len(a['result'])-1][0]

    return start_date, end_date 