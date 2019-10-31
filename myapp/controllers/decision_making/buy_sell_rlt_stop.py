# Enumerate the stock status
AVAILABLE = 1   
UNAVAILABLE = 2 

# Enumerate the direction
UP = 1  
DOWN = 2 
INSIGNIFICANT = 3


# Declare the static status that need to live across executions of the following algorithm.
last_direction=INSIGNIFICANT  
stock_status= UNAVAILABLE


def buy_sell_rlt_stop(buying_angle,selling_angle,relative_angle,angle,buying_price,current_candle_low_price,less_than_buy):

    global last_direction,stock_status,UP,DOWN,INSIGNIFICANT,AVAILABLE,UNAVAILABLE

    a = buying_price * (less_than_buy/100)
    selling_price = buying_price - a 
    selling_price = round(selling_price,2)
    
    BUY = 1
    SELL= 2
    HOLD= 3

    if angle <=relative_angle:  
       
        if stock_status ==  AVAILABLE:
            decision = SELL
            stock_status = UNAVAILABLE
        else:
            last_direction = DOWN
            decision = HOLD

    elif (angle < selling_angle) and (angle > relative_angle) and (stock_status == AVAILABLE):
       
        if (stock_status == AVAILABLE):
            decision = SELL
            stock_status = UNAVAILABLE
        else:
            last_direction = DOWN
            decision = HOLD

    elif current_candle_low_price < selling_price and  stock_status == AVAILABLE:
        
        decision = SELL
        stock_status = UNAVAILABLE
        last_direction = DOWN
    

    elif angle > buying_angle:

        if (stock_status == UNAVAILABLE) and (last_direction == UP):
            decision = BUY
            stock_status = AVAILABLE
        else:
            last_direction = UP
            decision = HOLD

    
    else:
        last_direction = INSIGNIFICANT
        decision = HOLD
 
 
    return decision

def buy_sell_rlt_stop_reset():
    
    global last_direction,stock_status,UP,DOWN,INSIGNIFICANT,AVAILABLE,UNAVAILABLE,decision

    stock_status = UNAVAILABLE
    last_direction = INSIGNIFICANT

   

def buy_sell_rlt_stop_isavaliable():
    
    global last_direction,stock_status,UP,DOWN,INSIGNIFICANT,AVAILABLE,UNAVAILABLE,decision

    if stock_status == AVAILABLE:
        return True
    else:
        return False


    
