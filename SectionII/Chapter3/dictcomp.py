if __name__ == '__main__':
    some_list = list(zip(range(1, 11), range(11, 21)))
    dictcomp = {a: b for a,b in some_list}
    print(dictcomp)