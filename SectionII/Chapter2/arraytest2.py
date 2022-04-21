from array import array


if __name__ == '__main__':
    x = array('I')

    for i in range(6):
        x.append(i)

    y = x.tolist()
    print(x.buffer_info())
    print(y)
    print(type(y))