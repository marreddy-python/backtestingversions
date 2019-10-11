from myapp.models.users import Strategy,db,Trades,Daily_metric,Total_metric
from sqlalchemy import and_
# from sqlalchemy import JSON
# from sqlalchemy.dialects.postgres import JSON
from sqlalchemy.sql.expression import cast

def addFav(clicked_id):
       
    res = Strategy.query.filter_by(strategy_id=clicked_id).first()
    print (res)

    if res != None:
  
        if res.isFavourite == True:

            res = Strategy.query.filter_by(strategy_id=clicked_id).update(dict(isFavourite=False))
            db.session.commit()

        else:
            res = Strategy.query.filter_by(strategy_id=clicked_id).update(dict(isFavourite=True))
            db.session.commit()
        
    print ('done')


def deletestrategy(clicked_id):

    # get the startegy from strategy table and delete it from the trades, total metric,daily metric

    # Trades
    res = Trades.query.filter_by(strategy_id=clicked_id).delete()
    db.session.commit()

    # Daily metric
    res = Daily_metric.query.filter_by(strategy_id=clicked_id).delete()
    db.session.commit()

    # Total metric  
    res = Total_metric.query.filter_by(strategy_id=clicked_id).delete()
    db.session.commit()


    # deleting the strategy from the strategy page
    res = Strategy.query.filter_by(strategy_id=clicked_id).delete()
    db.session.commit()

    print ('STRATEGY DELETED SUCCESFULLY')





 