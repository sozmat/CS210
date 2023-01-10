import math
import doctest
def pi_arch(num_sides: int) -> float:
    """Estimates pi using Archimedes method

    :param num_sides: integer
    :return:an estimation of pi that is float

    >>> round(pi_arch(100_000),2)
    3.14
    >>> round(pi_arch(512_983),2)
    3.14
    """
    inner_angle_b = 360.0 / num_sides
    half_angle_a = inner_angle_b / 2
    one_half_side_s = math.sin(math.radians(half_angle_a))
    side_s = one_half_side_s * 2
    polygon_circumference = num_sides * side_s
    pi = polygon_circumference / 2
    return pi

print(pi_arch(8))
doctest.testmod()