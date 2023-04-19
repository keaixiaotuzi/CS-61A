def tree(label, branches=[]):
    return [label] + list(branches) 

def is_leaf(t):
    return not branches(t)
def label(t): 
    return t[0] 
def branches(t):
    return t[1:]


def print_tree(t, indent=0):
    print('  .' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def count_ways(t, total):
    """Return the number of ways that any sequence of consecutive nodes in a root-to-leaf path
    can sum to total.
    >>> t1 = tree(5, [tree(1, [tree(2, [tree(1)]),
    ... tree(1, [tree(4, [tree(2, [tree(2)])])])]),
    ... tree(3, [tree(2, [tree(2),
    ... tree(3)])]),
    ... tree(3, [tree(1, [tree(3)])])])
    >>> count_ways(t1, 7)
    4
    >>> count_ways(t1, 4)
    6
    >>> t2 = tree(2, [tree(-10, [tree(12)]),
    ... tree(1, [tree(1),
    ... tree(-1, [tree(2)])])])
    >>> count_ways(t2, 2)
    6
    >>> count_ways(t2, 4)
    3
    """
   #  def paths(__________________________________):
   #      ways = 0
   #      if _____________________________________:
   #          ____________________________________
   #      ways += sum(____________________________________________________________________________)
   #      if _____________________________________:
   #          ____________________________________________________________________________________
   #      return ways
   #  return _____________________________________________________________________

    def paths(t,total, on_path):
        ways = 0
        if t == None:
            return 0
        ways += sum([paths(b, total-label(t), True) for b in branches(t)]+[paths(b, total, False) for b in branches(t) if not on_path])
        if label(t) == total and on_path:
            ways += 1
        # print(t, total, ways)
        return ways
    return paths(t,total, False)



# t1 = tree(5, [tree(1, [tree(2, [tree(1)]),
# tree(1, [tree(4, [tree(2, [tree(2)])])])]),
# tree(3, [tree(2, [tree(2),
# tree(3)])]),
# tree(3, [tree(1, [tree(3)])])])
# print_tree(t1)