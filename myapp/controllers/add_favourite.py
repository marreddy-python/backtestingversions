from myapp.models.users import Strategy,db,Trades,Daily_metric,Total_metric
from sqlalchemy import and_

def addFav(clicked_id):
       
    res = Strategy.query.filter_by(id=clicked_id).first()
    print (res)

    if res != None:
  
        if res.isFavourite == True:

            res = Strategy.query.filter_by(id=clicked_id).update(dict(isFavourite=False))
            db.session.commit()

        else:
            res = Strategy.query.filter_by(id=clicked_id).update(dict(isFavourite=True))
            db.session.commit()
        
    print ('done')


def deletestrategy(clicked_id):

    # get the startegy from strategy table and delete it from the trades, total metric,daily metric
    res = Strategy.query.filter_by(id=clicked_id)
    fetchdata_length = res.count()
    for i in range(0,fetchdata_length ):
        delete_strategy = res[i].Params

    print('DELETE STRATEGY',delete_strategy)

    # Deleting the trades
    db_data = Trades.query.filter(and_(Strategy["buying_angle"]== delete_strategy["buying_angle"],
    Strategy["selling_angle"]== delete_strategy["selling_angle"],Strategy["optimization"]== delete_strategy["optimization"],Strategy["relative_angle"]==delete_strategy["relative_angle"],
    Strategy["stop_order"]==delete_strategy["stop_order"],Strategy["less_than_buy"]== delete_strategy["less_than_buy"])).all().delete()
     
    db.session.commit()

    #  Deleting the daily_metric
    '''res = Daily_metric.query.filter_by(Strategy = delete_strategy).delete()
    db.session.commit()

    # Total metric
    res = Total_metric.query.filter_by(Strategy = delete_strategy).delete()
    db.session.commit()'''


    # deleting the strategy from the strategy page
    res = Strategy.query.filter_by(id=clicked_id).delete()
    db.session.commit()

    print ('STRATEGY DELETED SUCCESFULLY')





 