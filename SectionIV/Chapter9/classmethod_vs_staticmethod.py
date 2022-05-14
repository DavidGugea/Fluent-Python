class Demo:
    @classmethod
    def classmeth(*args):
        return args

    @staticmethod
    def statmeth(*args):
        return args


if __name__ == '__main__':
    print(Demo.classmeth())
    print(Demo.classmeth('spam'))

    print(Demo.statmeth())
    print(Demo.statmeth('spam'))
