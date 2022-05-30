class Quantity:  # Descriptor is a protocol-based feature; no subclassing is needed to implement one.
    def __init__(self, storage_name):
        self.storage_name = storage_name  # Each Quantity instance will have a storage_name attribute: that's the name of the attribute that will hold the value in the managed instances.

    def __set__(self, instance, value):  # __set__ is called when there is an attempt to assign to the managed attribute. Here, self is the descriptor instance (i.e., LineItem.weight or LineItem.price), instance is the manage instnace (a LineItem instance), and value is the value being assigned
        if value > 0:
            instance.__dict__[self.storage_name] = value  # Here, we must handle the managed instance __dict__ directly; trying to use the setattr built-in would trigger the __set__ method again, leading to infinite recursion.
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity('weight')  # The first descriptor instance is bound to the weight attribute
    price = Quantity('price')  # The second descriptor instance is bound to the price attribute

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    truffle = LineItem('White truffle', 100, 0)
    print(truffle.weight)