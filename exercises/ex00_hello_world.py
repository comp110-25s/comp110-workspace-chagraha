"""My First Exercise in COMP110"""

"""Finished Exercise 00"""

__author__ = "730663068"


def greet(name: str) -> str:
    """A welcome first function definition"""
    return "hello," + name + "!"


if __name__ == "__main__":
    print(greet(name=input("what is your name? ")))
