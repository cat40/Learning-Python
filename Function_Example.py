def f1(arg1, arg2, arg3):
    print arg1, arg2, arg3
    #this will print the three specified parmeter

def f2(arg1, arg2, arg3):
    return arg1, arg2, arg3
    #this will return the three specified parmeters as a tuple

def f3(arg1, arg2, arg3):
    for thing in range(arg1, arg2, arg3):
        yield thing
    #Makes a generator object out of the list supplied by range().
    #Essentially the same as xrange()
