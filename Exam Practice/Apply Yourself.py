def times(f, x):
    """Return a function g(y) that returns the number of f's in f(f(...(f(x)))) == y.
    >>> times(lambda a: a + 2, 0)(10) # 5 times: 0 + 2 + 2 + 2 + 2 + 2 == 10
    5
    >>> times(lambda a: a * a, 2)(256) # 3 times: square(square(square(2))) == 256
    3
    """
    def repeat(z):
        """Yield an infinite sequence of z, f(z), f(f(z)), f(f(f(z))), f(f(f(f(z)))), ...."""
        yield z
        yield from repeat(f(z))
    def g(y):
        n = 0
        for w in repeat(x):
            if w==y:
                return n
            n += 1
    return g