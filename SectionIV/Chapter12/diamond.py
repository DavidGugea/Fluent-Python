class A:
    def ping(self):
        print("ping: {0}".format(self))


class B(A):
    def pong(self):
        print("pong: {0}".format(self))


class C(A):
    def pong(self):
        print("ping: {0}".format(self))


class D(B, C):
    def ping(self):
        super().ping()
        print("post-ping: {0}".format(self))

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == '__main__':
    d = D()
    d.pong()
    C.pong(d)
