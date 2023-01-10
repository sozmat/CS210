
import math
import random
import p1arch
import p2wallis
import p3mc

def pi_allpi(err_tol: float):
    """
    Determines the input parameter needed for the function based off of the error tolerance given

    >>> pi_allpi(0.1)
    Archimedes: num_sides = 8
    Wallis: num_pairs = 8
    Monte Carlo: num_darts = 5

    :param err_tol: float, gives the range that is allowed for archimedes pi estimations to fall into
    :return: None
    """
    err_tolerance = math.pi + - err_tol     #define error tolerance

    for num_sides in range(3, math.inf):            #loop archimedes to find solution that falls in err_tol range
        pi_arch(num_sides)
        if pi_arch(num_sides) == err_tolerance: break
        return num_sides

    for num_pairs in range(1, math.inf):            #loop wallis to find solution that falls in err_tol range
        pi_wallis(num_pairs)
        if pi_arch(num_pairs) == err_tolerance: break
        return num_pairs
        print("Wallis: num_pairs =", num_pairs)

    for num_darts in range(3, math.inf):            #loop monte carlo to find solution that falls in err_tol range
        pi_mc(num_darts)
        if pi_arch(num_darts) == err_tolerance: break
        return num_darts

    print("Monte Carlo: num_darts:", num_darts)
    print("Wallis: num_pairs =", num_pairs)
    print("Archimedes: num_sides =", num_sides)

    return None

print(pi_allpi(0.001))





