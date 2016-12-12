import sympy as sm
import numpy as np
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify


def calculate_fib_list(left, right, x_acc):
    fibonacci_list = []
    a = 1
    b = 1
    fibonacci_list.append(a)
    while abs(right-left)/b > x_acc:
        fibonacci_list.append(b)
        a, b = b, a + b
    return fibonacci_list


def fibonacci_method(target_function, epsilon,  x_acc, iter_max, a, b):
    x, y, z = sm.symbols("x y z")
    fun_expr = sm.sympify(target_function)
    fib_list = calculate_fib_list(a, b, x_acc)
    n = len(fib_list) - 1  #fib_list[n] будет указывать на последний элемент
    if n + 1 > iter_max:
        print("Превышено максимальное число итераций")
        return 0, 0, 0
    left = a + fib_list[n-2] * (b - a) / fib_list[n]
    right = a + fib_list[n - 1] * (b - a) / fib_list[n]
    y_left = fun_expr.subs(x, left)
    y_right = fun_expr.subs(x, right)
    for i in range(n - 1, 1, -1):
        if y_left < y_right:
            b = right
            right = left
            y_right = fun_expr.subs(x, left)
            left = a + fib_list[n - 2] * (b-a)/fib_list[n]
            y_left = fun_expr.subs(x, left)
        else:
            a = left
            left = right
            y_left = y_right
            right = a + fib_list[n - 1] * (b-a)/fib_list[n]
            y_right = fun_expr.subs(x, right)
    last_test = (a + b) / 2
    last_edge = last_test + epsilon if fun_expr.subs(x, last_test - epsilon) < fun_expr.subs(x, last_test + epsilon)\
        else last_test - epsilon
    if last_edge > last_test:
        b = last_edge
    else:
        a = last_edge
    return fun_expr.subs(x, last_edge), last_edge, n - 1, abs(b - a)

