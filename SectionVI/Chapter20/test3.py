class A:
    value = 19
    another_value = 15

    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    a = A(23)
    print(a)

    print(a.value)  # 23
    print(a.another_value)  # 15