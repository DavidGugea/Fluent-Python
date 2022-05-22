t1 = tuple([1, 2, 3, 4, 5])
t2 = tuple()

if __name__ == '__main__':
    for x in t1:
        print(x)
    else:
        print("After for-loop-iteration over t1")

    i  = 0
    while i < len(t1):
        print(t1[i])
        i += 1
    else:
        print("After while-loop-iteration over t1")

    try:
        # print(1 + t3)
        print(t1)
    except Exception as e:
        print(e)
    else:
        print("The try-block didn't raise any exception.")

