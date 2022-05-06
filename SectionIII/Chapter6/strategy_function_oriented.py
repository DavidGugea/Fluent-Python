from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context
    def __init__(self, customer: Customer, cart, promotion=None) -> None:
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self) -> float:
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)

        return self.total() - discount

    def __repr__(self) -> str:
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):  # first Concrete Strategy
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):  # second Concrete Strategy
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1

    return discount


def large_order_promo(order):  # third Concrete Strategy
    """7% discount for order with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}

    if len(distinct_items) >= 10:
        return order.total() * .07

    return 0


if __name__ == '__main__':
    joe = Customer("John Doe", 0)
    ann = Customer("Ann Smith", 1100)

    cart = [
        LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0),
    ]

    order1 = Order(joe, cart, fidelity_promo)
    print(order1)

    order2 = Order(ann, cart, fidelity_promo)
    print(order2)

    banana_cart = [
        LineItem('banana', 30, .5),
        LineItem('apple', 10, 1.5),
    ]

    order3 = Order(joe, banana_cart, bulk_item_promo)
    print(order3)

    long_order = [
        LineItem(str(item_code), 1, 1.0)
        for item_code in range(10)
    ]

    order4 = Order(joe, long_order, large_order_promo)
    print(order4)

    order5 = Order(joe, cart, large_order_promo)
    print(order5)
