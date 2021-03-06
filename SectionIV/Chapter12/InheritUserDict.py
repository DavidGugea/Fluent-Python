import collections


class DoppelDict(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


class AnswerDict(collections.UserDict):
    def __getitem__(self, item):
        return 42


if __name__ == '__main__':
    dd = DoppelDict(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=1)
    print(dd)

    print("-"*50)

    ad = AnswerDict(a='foo')
    print(ad['a'])
    d = {}
    d.update(ad)
    print(d['a'])
    print(d)
