# using itertools.product()
from itertools import product


def cartesian_product(A, B):

    res = product(A, B)

    res_list = [str(x) for x in res]

    return res_list


if __name__ == '__main__':
    # A = [1, 2]
    # B = [3, 4]

    # initialize list and tuple
    A = input().strip().split()
    B = input().strip().split()

    A = [int(x) for x in A]
    B = [int(x) for x in B]

    _cartesian_product = cartesian_product(A, B)

    print(' '.join(_cartesian_product))
