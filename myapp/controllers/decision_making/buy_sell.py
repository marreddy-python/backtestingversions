# GLOBAL VARAIBALES FOR DECISION MAKING

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

decision = None

def buy_sell(buying_angle,selling_angle,angle):

    global last_direction,stock_status,UP,DOWN,INSIGNIFICANT,AVAILABLE,UNAVAILABLE,decision

    
    BUY = 1
    SELL= 2
    HOLD= 3

    if angle < selling_angle:
    
        if (stock_status == AVAILABLE)and(last_direction == DOWN):
            decision = SELL
            stock_status = UNAVAILABLE
        else:
            last_direction = DOWN
            decision = HOLD

    elif angle > buying_angle:
        if stock_status == UNAVAILABLE and last_direction == UP:
            decision = BUY
            stock_status = AVAILABLE
        else:
            last_direction = UP
            decision = HOLD
            

    else:
        
        last_direction = INSIGNIFICANT
        decision = HOLD

    return decision


def buy_sell_reset():

    print('================ buy_sell_reset called  ========================')
    print('======== BEFORE RESTING IT ======',stock_status, last_direction)

    stock_status = UNAVAILABLE
    last_direction = INSIGNIFICANT

    print('======== AFTER RESTING IT ======',stock_status, last_direction)

def buy_sell_isavaliable():
    
    print('CALLED  buy_sell_isavaliable ' )
    print ('I AM RETURNING STOCK STATUS', stock_status)
    if stock_status == AVAILABLE:
        return 1
    else:
        return 2








 

