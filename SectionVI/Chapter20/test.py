class A:
    def __init__(self, a):
        self.a = a


class B:
    def __init__(self, b):
        self.b = b


class C(A):
    def __init__(self, a, c):
        super().__init__(a)
        self.c = c


class D(B):
    def __init__(self, b, d):
        super().__init__(b)
        self.d = d


class E(C, D):
    def __init__(self, e, a, c):
        super().__init__(a, c)
        self.e = e


print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(D.__mro__)
print(E.__mro__)