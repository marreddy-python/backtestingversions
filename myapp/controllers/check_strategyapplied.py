from myapp.models.users import Trades,db,Strategy
import json 
from sqlalchemy import desc

def applied_or_not(s,start,end):
   
    sc = {
        "buying_angle":s.startegy_values[0] ,
        "selling_angle":  s.startegy_values[1],
        "optimization":s.startegy_values[2],
        "relative_angle": s.startegy_values[3],
        "stop_order":  s.startegy_values[4],
        "less_than_buy": s.startegy_values[5]
    }
 
    print ('score',sc)
        
    data  = json.dumps(sc)
    score = json.loads(data)

    current_strategy = score 

    db_get_strategies =  Trades.query.filter(Trades.Symbol=='TVIX').all()
    fetched_length = len(db_get_strategies)
    print (fetched_length)
    stored_strategies = []

    for st in range(0,fetched_length):
        strategies = db_get_strategies[st].Strategy  
        if  db_get_strategies[st].buy_time == start and db_get_strategies[st].Sell_time == end:
            stored_strategies.append(strategies)

    # Check if current strategy is exist in strategies table 
    if (current_strategy in stored_strategies):  
        return 'exist'
    else:
        return 'notexist'


def strategy_savedornot(s,start,end):
    sc = {
        "buying_angle":s.startegy_values[0] ,
        "selling_angle":  s.startegy_values[1],
        "optimization":s.startegy_values[2],
        "relative_angle": s.startegy_values[3],
        "stop_order":  s.startegy_values[4],
        "less_than_buy": s.startegy_values[5]
    }
 
    print ('score',sc)
        
    data  = json.dumps(sc)
    score = json.loads(data)

    current_strategy = score 
   
    db_get_strategies =  Strategy.query.filter(Strategy.Symbol=='TVIX').all()
    fetched_length = len(db_get_strategies)
    print (fetched_length)
    stored_strategies = []

    for st in range(0,fetched_length):
        strategies = db_get_strategies[st].Strategy  
        if  db_get_strategies[st]. Start_time == start and db_get_strategies[st].End_time == end:
            stored_strategies.append(strategies)

    # Check if current strategy is exist in strategies table 
    if (current_strategy in stored_strategies):  
        return 'saved'
    else:
        return 'notsaved'


def get_strategy_id(Stratey_values):

    res = Strategy.query.order_by(Strategy.strategy_id.desc()).all()

    if res != None:

        for pams in range(0,res.count()):

            strategy_id = pams.strategy_id

            
            strategy_params = pams.Params 

            if (strategy_params["buying_angle"]= Stratey_values[0] and strategy_params["selling_angle"]= Stratey_values[1] and strategy_params["optimization"]= Stratey_values[2] and strategy_params["relative_angle"]= Stratey_values[3] andstrategy_params["stop_order"]= Stratey_values[4] andstrategy_params["less_than_buy"]= Stratey_values[5]  ):

                return strategy_id 
        

        return strategy_id + 1

    else:
        return 1




def get_lastsaved_strategy():

    entities = Strategy.query.order_by(desc(Strategy.Created_at)).first()

    if entities != None:

        start_time = entities.Start_time
        tweenty_days = entities.End_time

        params = entities.Params 

        Strategy_values = [params["buying_angle"],params["selling_angle"],params["optimization"],params["relative_angle"],params["stop_order"],params["less_than_buy"]]

        return Strategy_values,start_time,tweenty_days 
    

    else:
        Strategy_values = None
        start_time = None
        tweenty_days = None

        return Strategy_values,start_time,tweenty_days 


def get_strategyinfo(id):

    db_get_strategies =  Strategy.query.filter(Strategy.strategy_id==id).first()

    params = db_get_strategies.Params 

    if db_get_strategies != None:
        strategy_params = [params["buying_angle"],params["selling_angle"],params["optimization"],params["relative_angle"],params["stop_order"],params["less_than_buy"],id]
        
        return strategy_params

    else:
        strategy_params = []

        return strategy_params











 