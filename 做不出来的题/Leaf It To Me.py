def tree(label, branches=[]):
    return [label] + list(branches) 

def is_leaf(t):
    return not branches(t)
def label(t): 
    return t[0] 
def branches(t):
    return t[1:]


def max_path(t, k):
    """ Return a list of the labels on any path in tree t of length at most k with the greatest sum
    >>> t1 = tree(6, [tree(3, [tree(8)]), tree(1, [tree(9), tree(3)])])
    >>> max_path(t1, 3)
    [6, 3, 8]
    >>> max_path(t1, 2)
    [3, 8]
    >>> t2 = tree(5, [t1, tree(7)])
    >>> max_path(t2, 1)
    [9]
    >>> max_path(t2, 2)
    [5, 7]
    >>> max_path(t2, 3)
    [6, 3, 8]
    """
    # def helper(t, k, on_path):
    #     if t == None:
    #         return []
    #     elif k==1:
    #         return [label(t)]
    #     a = __________________________________________________________
    #     if ______________________________________________________________________:
    #         return max(___________________, key = sum)
    #     else:
    #         b = __________________________________________________________
    #         return max(___________________, key = sum)
    # return helper(t, k, False)

    def helper(t, k, on_path):
        if k == 0 or t == None:
            return []
        elif not on_path and k == 1:
            return [label(t)]
        a = helper(t, k - 1, True)
        if not on_path:
            b = helper(branches(t), k, False)
            return max([a] + b, key=sum)
        else:
            return [label(t)] + max(a, [], key=sum)
    return helper(t, k, False)


