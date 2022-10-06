import functools

def myfunc(a, b = 2):
    print("called myfunc with: ", (a, b))

def show_details(name, f, is_partial = False):
    print("{}:".format(name))
    print(' object : ', f)
    if not is_partial:
        print('__name__:',f.__name__)
    if is_partial:
        print("   func:",f.func)
        print("   args:", f.args)
        print("   keywords:",f.keywords)
    return


if __name__ == "__main__":
    show_details('my_func', myfunc)
    myfunc('a', 3)

    # set a different value for 'b', but require
    # the caller to provide a

    p1 = functools.partial(myfunc, b = 4)
    show_details('partial with named default', p1, True)
    p1('passing a')
    p1('overrides b', b = 5)

    print()

    # set default values for both a and b
    p2 = functools.partial(myfunc, 'default a', b = 99)
    show_details('partial with defaults', p2, True)
    p2()
    p2(b = 'Overrides b')
    print()

    print("Insufficient arguments")
    # p1()




