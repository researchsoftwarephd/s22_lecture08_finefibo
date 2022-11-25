"""Our great module for producing Fibonacci numbers!
"""
import sys

def fibo_number(n):
    """This function does what it says on the name.

    Args:
        n: index of the nth fibonacci number.

    Returns:
        The nth Fibonacci number.
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_number(n - 1) + fibo_number(n - 2)


def run_from_cli():
    """This function is used to run the program from the command line."""

    n = int(sys.argv[1])
    f = fibo_number(n)
    print(f)