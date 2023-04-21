# Write generate_constant, a generator function that repeatedly yields the same value forever.
def generate_constant(x):
   """A generator function that repeats the same value X forever.
   >>> two = generate_constant(2)
   >>> next(two)
   2
   >>> next(two)
   2
   >>> sum([next(two) for _ in range(100)])
   200
   """
   while True:
      yield x

def black_hole(seq, trap):
   """A generator that yields items in SEQ until one of them matches TRAP, in
   which case that value should be repeatedly yielded forever.
   >>> trapped = black_hole([1, 2, 3], 2)
   >>> [next(trapped) for _ in range(6)]
   [1, 2, 2, 2, 2, 2]
   >>> list(black_hole(range(5), 7))
   [0, 1, 2, 3, 4]
   """
   for i in seq:
      if i == trap:
         yield from generate_constant(i)
      else:
         yield i
