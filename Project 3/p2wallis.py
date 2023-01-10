import doctest
import math
def pi_wallis(num_pairs:int) -> float:
    """Estimates pi using Wallis method

    :param num_pairs: integer
    :return: an estimation of pi that is float

    >>> round(pi_wallis(300_765),2)
    3.14
    >>> round(pi_wallis(67_783),2)
    3.14
    """
    acc = 1
    num = 2

    for pairs in range(num_pairs):
        left_term = num / (num - 1)
        right_term = num / (num + 1)

        acc = acc * left_term * right_term

        num = num + 2
    pi = acc * 2
    return pi

doctest.testmod()
