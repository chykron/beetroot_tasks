"""
Use one of your previous homeworks - especially with loops, and estimate functions complexity with Big O notation.
"""


def total_price_of_stock(stock: dict, prices: dict) -> int | float:
    total_price = 0
    for key, value in stock.items():
        item_price = value * prices[key]
        total_price += item_price
    return total_price

# Time Complexity: O(N) - where N is the number of items in the stock dictionary
# Space Complexity: O(1) - since we are using a constant amount of additional space
