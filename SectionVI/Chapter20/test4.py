class DescriptorTest:
    def __init__(self, value_name):
        self.value_name = value_name

    def __get__(self, instance, owner):
        print('descriptor __get__ method triggered')

    def __set__(self, instance, value):
        print('descriptor __set__ method triggered')


class A:
    value = DescriptorTest('value')

    def __init__(self, value):
        pass


if __name__ == '__main__':
    a = A(23)
    print(a.value)
    # a.value = 19