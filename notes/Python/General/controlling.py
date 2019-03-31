def controltest(func, x):
    for i in range(0, x):
        func(x)

if __name__ == "__main__":
    from testing import testfunc
    controltest(testfunc, 3)

