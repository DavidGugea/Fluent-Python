import pprint


class A:
    c = 5

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def class_hello_world(cls):
        print(cls)
        print("class hello world")

    @staticmethod
    def static_hello_world():
        print("static hello world")

    def instance_hello_world(self):
        print(self)
        print("instance hello world")


if __name__ == '__main__':
    a = A('letter a', 'letter b')
    pprint.pprint(
        [i for i in dir(a) if not i.startswith('__')],
        indent=10
    )

    """
    A.class_hello_world()
    A.static_hello_world()
    print(A.c)

    print("-" * 50)

    a = A('this is the letter a', 'this is the letter b')
    print(a.a)
    print(a.b)
    print(a.c)
    """
