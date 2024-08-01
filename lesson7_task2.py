"""
Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure mentioned above, then computes and returns
the total price of stock.
"""


def total_price_of_stock(stock: dict, prices: dict) -> int | float:
    total_price = 0
    for key, value in stock.items():
        item_price = value * prices[key]
        total_price += item_price
    return total_price


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
print(total_price_of_stock(stock, prices))
