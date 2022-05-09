if __name__ == '__main__':
    t1 = (1, 2, 3)
    t2 = tuple(t1)
    print(t2 is t1)
    t3 = t1[:]
    print(t3 is t1)