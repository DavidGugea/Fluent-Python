class A:
    def __init__(self, value: int) -> None:
        self.value = value

    def add5(self) -> int:
        return self.value + 5


if __name__ == '__main__':
    a = A(23)
    print(a.add5)