def gen_builder():
    for i in range(0, 101, 2):
        yield i


def gen_builder_2():
    for i in range(102, 201, 2):
        yield i

    yield from gen_builder()


gen = gen_builder_2()
for i in gen:
    print(i)
