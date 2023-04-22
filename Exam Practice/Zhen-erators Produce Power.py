def integers ( n ):
    while True :
        yield n
        n += 1

def drop (n , s ):
    for _ in range ( n ):
        next ( s )
    for elem in s :
        yield elem

def powers_of_two ( ints = integers ( 1 )):
    """
    >>> p = powers_of_two ()
    >>> [ next (p) for _ in range (10)]
    [1 , 2 , 4 , 8 , 16 , 32 , 64 , 128 , 256 , 512]
    """
    curr = next(ints)
    yield curr
    yield from powers_of_two(drop(curr-1,ints)) 