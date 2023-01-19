import numpy as np
import json


def add(a, b):
    return ("{:.3f}".format(a+b))


def sub(a, b):
    return ("{:.3f}".format(a-b))


def multy(a, b):
    return ("{:.3f}".format(a*b))


def divide(a, b):
    return ("{:.3f}".format(a/b))


def power(a, b):
    return ("{:.3f}".format((a**b)))


def linear_plot(a, b):
    # y = a*x+b
    min_range = np.random.uniform(-10, 10)
    # the range will be between -10 to 10
    max_range = np.random.uniform(-10, 10)
    if min_range > max_range:
        # make sure the min is smaller than the max
        min_range, max_range = max_range, min_range
    x = np.random.uniform(min_range, max_range, 10)
    y = a*x + b
    res = {
        "x": x.tolist(),
        "y": y.tolist()
    }
    return res


def percent(a, b):  # 20 , 10  # the percent of x from y
    x = b  # 20
    y = x * (a*0.01)
    return ("{:.2f}".format(y))
