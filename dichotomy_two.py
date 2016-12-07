import sympy as sm

import numpy as np
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify


def dichotomy_method(target_function, x_acc, iter_max, a, b):
    x, y, z = sm.symbols("x y z")
    fun_expr = sm.sympify(target_function)
    iter_count = 0
    while (abs(b - a) > x_acc) & (iter_count < iter_max):
        mid_test = (b+a)/2
        left_test = (a + mid_test)/2
        right_test = (mid_test + b)/2
        if (fun_expr.subs(x, left_test) < fun_expr.subs(x, mid_test)) & (fun_expr.subs(x, mid_test) < fun_expr.subs(x, right_test)):
            b = right_test
        elif (fun_expr.subs(x, left_test) > fun_expr.subs(x, mid_test)) & (fun_expr.subs(x, mid_test) < fun_expr.subs(x, right_test)):
            a = left_test
            b = right_test
        else:
            a = left_test
        iter_count += 1

    x_opt = (b+a)/2

    return fun_expr.subs(x, x_opt), x_opt, iter_count
