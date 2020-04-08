"""
Based on github.com/TheAlgorithms/Python version
Newton's Method - https://en.wikipedia.org/wiki/Newton%27s_method
"""

def newton(function1, function2, starting_int):
    """
    function1 is the f(x) and function2 is the f'(x)
    """
    precision = 10 ** -5
    x0 = starting_int
    while True:
        x1 = x0 - function1(x0) / function2(x0)
        if abs(x0 - x1) < precision:
            return x1
        x0 = x1


def f(x):
    return (x ** 3) - (2 * x) - 5


def f2(x):
    return 3 * (x ** 2) - 2


if __name__ == "__main__":
    print(newton(f, f2, 3))
