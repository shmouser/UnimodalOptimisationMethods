import sys
import Code.dichotomy_one
import Code.dichotomy_two
import Code.golden_ratio
import Code.fibonacci
import matplotlib.pyplot as plt
import numpy as np


def main():
    target_function = "x**2 - 2"
    accuracy = 0.001
    epsilon = 0.0001
    max_iter = 100
    a = -3
    b = 2


    # print("Метод дихотомии-1")
    # y_opt, x_opt, iter_num_done = Code.dichotomy_one.dichotomy_method(target_function, epsilon, accuracy, max_iter, a, b)
    # # print("func value ", y_opt, " at ", x_opt, " iterations done ", iter_num_done)
    # print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    # print()

    # print("Метод дихотомии-2")
    # y_opt, x_opt, iter_num_done = Code.dichotomy_two.dichotomy_method(target_function, accuracy, max_iter, a, b)
    # print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    # print()

    # print("Метод золотого сечения")
    # y_opt, x_opt, iter_num_done = Code.golden_ratio.golden_ratio_method(target_function, accuracy, accuracy, max_iter, a, b, 1.68)
    # print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    # print()

    # print("Метод Фибоначчи")
    # y_opt, x_opt, iter_num_done = Code.fibonacci.fibonacci_method(target_function, epsilon, accuracy, max_iter, a, b)
    # print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    # print()

    # построить график зависимости числа итераций от точности

    # x_range = np.arange(0.0000001, 0.0001, 0.000005)
    # dichotomy_one_iter_list = []
    # dichotomy_two_iter_list = []
    # golden_ratio_iter_list = []
    # fibonacci_iter_list = []
    # for accuracy in x_range:
    #     dichotomy_one_iter_list.append(dichotomy_one.dichotomy_method(target_function, epsilon, accuracy, max_iter, a, b)[2])
    #     dichotomy_two_iter_list.append(dichotomy_two.dichotomy_method(target_function, accuracy, max_iter, a, b)[2])
    #     golden_ratio_iter_list.append(golden_ratio.golden_ratio_method(target_function, accuracy, accuracy, max_iter, a, b, 1.68)[2])
    #     fibonacci_iter_list.append(fibonacci.fibonacci_method(target_function, epsilon, accuracy, max_iter, a, b)[2])
    # print(dichotomy_one_iter_list)
    # print(dichotomy_two_iter_list)
    # print(golden_ratio_iter_list)
    # print(fibonacci_iter_list)


if __name__ == '__main__':
    sys.exit(main())
