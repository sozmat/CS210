def fb(n):
    """Plays the game Fizzbuzz
    :param n: an integer number
    :return: fizz if divisible by 3, buzz if divisible by 5, fizzbuzz if divisible by both 3 and 5
    >>> fb(3)
    1
    2
    fizz
    Game over!
    >>> fb(5)
    1
    2
    fizz
    4
    buzz
    Game over!
    """
    if type(n) == int:
        for i in range(1,n+1):
            if (i % 3 == 0):
                if (i % 5 == 0):
                    print("fizzbuzz")
            if (i % 5 == 0):
                if (i % 3 != 0):
                    print("buzz")
            if (i % 3 == 0):
                if (i % 5 != 0):
                    print("fizz")
            if (i % 3 != 0):
                if (i % 5 != 0):
                    print(i)
            i = i + 1
        print("Game over!")
    if type(n) != int:
        print("n must be integer to play game! try again")
    return None

print(fb(15))

import doctest
doctest.testmod()