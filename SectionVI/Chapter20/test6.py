class Descriptor:
    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print('descriptor __get__ executed')

    def __set__(self, instance, value):
        print('descriptor __set__ executed')


class A:
    value = Descriptor('value')

    def hello_world(self):
        print(self.value)


if __name__ == '__main__':
    a = A()
    print(a.value)
