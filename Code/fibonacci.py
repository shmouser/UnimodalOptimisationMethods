import sympy as sm
import numpy as np
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify


def calculate_fib_list(left, right, epsilon, x_acc):
    fibonacci_list = []
    a = 1
    b = 1
    while abs(right-left)/a + epsilon > x_acc:
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list


def fibonacci_method(target_function, epsilon, x_acc, iter_max, a, b):
    x, y, z = sm.symbols("x y z")
    fun_expr = sm.sympify(target_function)
    iter_count = 0
    fib_list = calculate_fib_list(a, b, epsilon, x_acc)
    fib_list_length = len(fib_list)
    if fib_list_length > iter_max:
        print("Превышено максимальное число итераций")
        return 0, 0, 0
    print(fib_list)
    iter_count = 3
    #while (abs(b - a) > x_acc) & (iter_count < iter_max) & ((fib_list_length - iter_count - 2) > 0):
    for i in range(fib_list_length):
        lambda_fib = fib_list[fib_list_length - iter_count + 1]/fib_list[fib_list_length - iter_count + 2]
        iter_count += 3
        left_test = a + (b-a)*lambda_fib
        right_test = b - (b-a)*lambda_fib
        next_edge = right_test if fun_expr.subs(x, left_test) < fun_expr.subs(x, right_test) else left_test
        if next_edge == left_test:
            a = next_edge
        else:
            b = next_edge
    last_test = (b + a) / 2
    last_edge = last_test + epsilon if fun_expr.subs(x, last_test - epsilon) < fun_expr.subs(x, last_test + epsilon) \
        else last_test - epsilon
    if last_edge > last_test:
        b = next_edge
    else:
        a = next_edge
    x_opt = (b + a) / 2
    iter_count -= 3

    return fun_expr.subs(x, x_opt), x_opt, iter_count

