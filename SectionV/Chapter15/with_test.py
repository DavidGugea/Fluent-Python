with open("lorem.txt") as fp:
    src = fp.read(60)

if __name__ == '__main__':
    print(len(src))
    print(fp)
    print(fp.closed, fp.encoding)
    print("-"*25)
    try:
        print(fp.read(60))
    except ValueError as e:
        print(e)