import sympy as sm
import numpy as np
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify


def dichotomy_method(target_function, epsilon, x_acc, iter_max, a, b):
    if epsilon*10 > x_acc:
        print("epsilon должна быть много меньше x_acc")
        return 0, 0, 0
    x, y, z = sm.symbols("x y z")
    fun_expr = sm.sympify(target_function)
    iter_count = 0
    while (abs(b - a) > x_acc) & (iter_count < iter_max):
        next_test = (b+a)/2
        next_edge = next_test + epsilon if fun_expr.subs(x, next_test - epsilon) < fun_expr.subs(x, next_test + epsilon) else next_test - epsilon
        if next_edge > next_test:
            b = next_edge
        else:
            a = next_edge
        iter_count += 1

    x_opt = (b+a)/2

    return fun_expr.subs(x, x_opt), x_opt, iter_count, abs(b - a)


