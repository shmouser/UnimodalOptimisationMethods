import sympy as sm

import numpy as np
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify


def golden_ratio_method(target_function, epsilon, x_acc, iter_max, a, b, golden_ratio):
    x, y, z = sm.symbols("x y z")
    fun_expr = sm.sympify(target_function)
    iter_count = 0
    while (abs(b - a) > x_acc) & (iter_count < iter_max):
        left_test = b - (b-a)/golden_ratio
        right_test = a + (b-a)/golden_ratio
        next_edge = right_test if fun_expr.subs(x, left_test) < fun_expr.subs(x, right_test) else left_test
        if next_edge == left_test:
            a = next_edge
        else:
            b = next_edge
        iter_count += 1

    last_test = (b + a)/2
    last_edge = last_test + epsilon if fun_expr.subs(x, last_test - epsilon) < fun_expr.subs(x, last_test + epsilon) \
        else last_test - epsilon
    if last_edge > last_test:
        b = last_edge
    else:
        a = last_edge
    x_opt = (b + a)/2

    return fun_expr.subs(x, x_opt), x_opt, iter_count, abs(b - a)


