import sys
sys.dont_write_bytecode=True

from factory import get_ds,get_ss


class DataController():
    
    DS = get_ds()

    def __init__(self):
        self.symbols = None
        self.Strategy = None
        self.l = []
        self.start = None
        self.end = None

    def getTrades(self,symbols,Strategy,start,end):
        self.symbols = symbols
        self.Strategy = Strategy
        self.start = start 
        self.end = end
        a = self.DS.getTrades(symbols,Strategy,start,end)
        return a

    def getPerformance(self,symbol,Strategy,start,end):
        self.symbol = symbol 
        self.Strategy = Strategy
        self.start = start 
        self.end = end
        a = self.DS.getPerformance(symbol,Strategy,start,end)
        return a 


    def MarketData(self,start,end):
        self.start = start 
        self.end = end
        a = self.DS.MarketData(start,end)
        return a

    
    def getStrategies(self):
        data = self.DS.getStrategies()
        return data 
     





class StrategyController():
     
    SS = get_ss()

    def __init__(self):
        self.Strategy = None
        self.l = []
        self.symbol = None
        self.start = None
        self.end = None
    
    def saveStrategy(self,Strategy,Start_time,End_time,strategy_id ):
        self.Strategy = Strategy
        b = self.SS.saveStrategy(Strategy,Start_time,End_time,strategy_id)
        return b 

    def getNewStrategy(self,l):
        self.l = l
    
    def updateStrategy(self,Strategy,params):
        self.Strategy = Strategy
        self.params = params
        b = self.SS.updateStrategy(Strategy,params)
        return b 


    def applyStrategy(self,symbol,Strategy,start,end,strategy_id):
        self.symbol = symbol
        self.Strategy = Strategy
        self.start = start 
        self.end = end
        self.strategy_id = strategy_id
        b = self.SS.applyStrategy(symbol,Strategy,start,end,strategy_id)
        return b 

    def metricCalculation(self,start_time,tweenty_days,St,strategy_id):
        self.St = St
        self.start_time = start_time
        self.tweenty_days = tweenty_days
        self.strategy_id = strategy_id

        b = self.SS.metric_calcgetMetric(start_time,tweenty_days,St,strategy_id)

        return b 

    
    def Total_metricCalculation(self,start_time,tweenty_days,St,strategy_id):
        self.St = St
        self.start_time = start_time
        self.tweenty_days = tweenty_days
        self.strategy_id = strategy_id

        b = self.SS.metric_calcTot_met(start_time,tweenty_days,St,strategy_id)
        return b 
            







    def getProgress():
        pass


class Arena():

    def __init__(self,pStrategies,noOfStrategies,maximumlimit):
        self.pStrategies = None
        self.noOfStrategies = None
        self.maximumlimit = None

    def addStrategiesToArena(self,Strategy):
        self.Strategy = Strategy

    def deleteStrategiesFromArena(self,Strategy):
        self.Strategy = Strategy
    
    def createArena():
        pass


class Strategy():

    def __init__(self,id,startegy_values,isFavourite):
        self.id = id 
        self.startegy_values = startegy_values
        self.isFavourite = isFavourite

    def __new__(cls):
        return [id,startegy_values,isFavourite]



