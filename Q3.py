f = open("sample_AAPL.txt", "r")

listItems = f.read().splitlines()

appleprices=listItems

for i in range(0, len(listItems)):
 appleprices[i] = float(listItems[i])

def buy_and_sell(Stock_prices):
    max_profit_val = 0
    current_max_val = 0
    for price in reversed(Stock_prices):
        current_max_val = max(current_max_val, price) 
        potential_profit = current_max_val - price
        max_profit_val = max(potential_profit, max_profit_val)

    return max_profit_val 
    
print (buy_and_sell(appleprices))
