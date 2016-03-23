import random
MAX_INCREASE = 0.175 # 10%
MAX_DECREASE = 0.05 # 5%
MIN_PRICE = 0.01
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0

def format_currency(value):
    return "${:,.2f}".format(value)


day_count = 0
price = INITIAL_PRICE
print("Starting price: ", format_currency(price))
#print(type(day_count))
while price >= MIN_PRICE and price <= MAX_PRICE:
    priceChange = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
    # generate a random floating-point number
    # between 0 and MAX_INCREASE
        priceChange = random.uniform(0, MAX_INCREASE)
    else:
    # generate a random floating-point number
    # between negative MAX_INCREASE and 0
        priceChange = random.uniform(-MAX_DECREASE, 0)
    price *= (1 + priceChange)
    day_count += 1
    print("On day {}, the stock price was".format(day_count), format_currency(price))