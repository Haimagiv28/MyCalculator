import math
import numpy as np


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def multy(a, b):
    return a*b


def divide(a, b):
    return a/b


def power(a, b):
    return pow(a, b)


def linear_plot(a, b):
    # y = a*x+b

    x = np.linspace(-2, 2, 1)
    y = a*x + b
    res = {
        "x": x.tolist(),
        "y": y.tolist()
    }
    return res
