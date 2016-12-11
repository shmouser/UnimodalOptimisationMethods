import sys
import Code.dichotomy_one
import Code.dichotomy_two
import Code.golden_ratio
import Code.fibonacci
import matplotlib.pyplot as plt
import numpy as np


def main():
    target_function = "x*(x-7)"
    accuracy = 0.001
    epsilon = 0.000001
    max_iter = 100
    a = -30
    b = 22

    print("Метод дихотомии-1")
    y_opt, x_opt, iter_num_done = Code.dichotomy_one.dichotomy_method(target_function, epsilon, accuracy, max_iter, a, b)
    # print("func value ", y_opt, " at ", x_opt, " iterations done ", iter_num_done)
    print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    print()

    print("Метод дихотомии-2")
    y_opt, x_opt, iter_num_done = Code.dichotomy_two.dichotomy_method(target_function, accuracy, max_iter, a, b)
    print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    print()

    print("Метод золотого сечения")
    y_opt, x_opt, iter_num_done = Code.golden_ratio.golden_ratio_method(target_function, accuracy, accuracy, max_iter, a, b, 1.68)
    print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    print()

    print("Метод Фибоначчи")
    y_opt, x_opt, iter_num_done = Code.fibonacci.fibonacci_method(target_function, epsilon, accuracy, max_iter, a, b)
    print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    print()

    # построить график зависимости числа итераций от точности

    max_accuracy = 0.0000001
    min_accuracy = 0.00001
    step = max_accuracy * 10
    x_range = np.arange(max_accuracy, min_accuracy, step)
    epsilon = max_accuracy / 10
    dichotomy_one_iter_list = []
    dichotomy_two_iter_list = []
    golden_ratio_iter_list = []
    fibonacci_iter_list = []
    for i in x_range:
        dichotomy_one_iter_list.append(Code.dichotomy_one.dichotomy_method(target_function, epsilon, i, max_iter, a, b)[2])
        dichotomy_two_iter_list.append(Code.dichotomy_two.dichotomy_method(target_function, i, max_iter, a, b)[2])
        golden_ratio_iter_list.append(Code.golden_ratio.golden_ratio_method(target_function, epsilon, i, max_iter, a, b, 1.68)[2])
        fibonacci_iter_list.append(Code.fibonacci.fibonacci_method(target_function, epsilon, i, max_iter, a, b)[2])
    print(dichotomy_one_iter_list)
    print(dichotomy_two_iter_list)
    print(golden_ratio_iter_list)
    print(fibonacci_iter_list)


if __name__ == '__main__':
    sys.exit(main())
