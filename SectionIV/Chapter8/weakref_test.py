import weakref

if __name__ == '__main__':
    s1 = {1, 2, 3}
    s2 = s1

    def deleted():
        print("The object got deleted")

    ender = weakref.finalize(s1, deleted)
    print(ender.alive)
    del s1
    print(ender.alive)
    s2 = 'spam'
    print(ender.alive)
