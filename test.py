import time
from getters.api import td_ameritrade
from getters.decides_dg_count import check
from getters.export import highcharts_export
from getters.decides_start_end import decide_start_end
from celery_task import db
from flask import session 
from models_celery.tables import price_data
from celery_task import Strategy_features
from sqlalchemy import and_
from decimal import *
import json
import sys
sys.dont_write_bytecode=True

from sqlalchemy.types import Integer

db_data = price_data.query.filter(and_(price_data.Time_stamp >= 1571668200000 ,price_data.Time_stamp <= 1571754600000 ,price_data.stock_symbol=='TVIX'))
        
fetchdata_length = db_data.count()
print ('fetchdata_length',fetchdata_length)

stock_data = []
            
if fetchdata_length == 0 :
    pass
else:

    # CONVERTING FETCHED DATA INTO THE LIST FORMAT INORDER TO SEND TO HIGHCHARTS EXPORT SERVER 
    for candle in db_data:

        Time_stamp = int(candle.Time_stamp)
        Opening = candle.Opening_price
        High = candle.High
        Low = candle.Low
        close = candle.Closing_price
        Volume = candle.Volume
                
        stock_data.append([Time_stamp,Opening,High,Low,close,Volume])

print (stock_data)
