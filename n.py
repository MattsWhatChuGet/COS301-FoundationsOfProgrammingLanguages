x=10
def f(x):
    def g():
        return x
    return g
print(f(3)())