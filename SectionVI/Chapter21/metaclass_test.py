import pprint


class Meta(type):
    def __new__(cls, class_name, bases, attrs):
        pprint.pprint(attrs, indent=10)
        return type(class_name, bases, attrs)


class Dog(metaclass=Meta):
    x = 5
    y = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def some_method(self):
        print('hello world')


if __name__ == '__main__':
    d = Dog('some name', 19)
