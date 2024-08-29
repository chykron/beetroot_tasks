"""
Product Store
Write a class Product that has three attributes:
type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store.
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional
classes to operate on a certain type of product, etc.
Also, the ProductStore class must have the following methods:
add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store
(30 percent)
set_discount(identifier, percent, identifier_type='name') - adds a discount for all products specified by input
identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available,
in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product(Food, 'Ramen, 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell(‘Ramen’, 10)
assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
"""
from typing import Dict, List, Tuple, Union


class Product:
    def __init__(self, product_type: str, name: str, price: float) -> None:
        self.product_type: str = product_type
        self.name: str = name
        self.price: float = price


class ProductStore:
    def __init__(self) -> None:
        self.products: Dict[str, Dict[str, Union[Product, float, int]]] = {}
        self.income: float = 0.0

    def add(self, product: Product, amount: int) -> None:

        if amount <= 0:
            raise ValueError(f'Amount must be greater than zero.')

        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {
                'product': product,
                'amount': amount,
                'price': product.price * 1.3,
            }

    def set_discount(self, identifier: str, percent: int, identifier_type='name') -> None:
        discount = (100 - percent) / 100
        for product_info in self.products.values():
            product = product_info['product']
            if identifier_type == 'name' and product.name == identifier:
                product_info['price'] *= discount
            elif identifier_type == 'type' and product.product_type == identifier:
                product_info['price'] *= discount

    def sell_product(self, product_name: str, amount: int) -> None:
        if product_name in self.products:
            if self.products[product_name]['amount'] >= amount:
                self.products[product_name]['amount'] -= amount
                self.income += self.products[product_name]['price'] * amount
                if self.products[product_name]['amount'] == 0:
                    del self.products[product_name]
            else:
                raise ValueError(f'Not enough {product_name} in stock')
        else:
            raise ValueError(f'Not enough {product_name} in stock')

    def get_income(self) -> float:
        return self.income

    def get_all_products(self) -> List[Tuple[str, int]]:
        return [(product_info['product'].name, product_info['amount']) for product_info in self.products.values()]

    def get_product_info(self, product_name: str) -> Tuple[str, int | float]:
        if product_name in self.products:
            return product_name, self.products[product_name]['amount']
        else:
            raise ValueError(f'Not enough {product_name} in stock')


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product("Food", 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product("Ramen", 10)

print(s.get_product_info("Ramen"))