import sys
import Code.dichotomy_one
import Code.dichotomy_two
import Code.golden_ratio
import Code.fibonacci
import matplotlib.pyplot as plt
import numpy as np


def main():
    target_function = "x**2 - 1"
    accuracy = 0.001
    epsilon = 0.000001
    max_iter = 100
    a = -10
    b = 9

    print("Метод дихотомии-1")
    y_opt, x_opt, iter_num_done, final_segment = Code.dichotomy_one.dichotomy_method(target_function, epsilon, accuracy, max_iter, a, b)
    # print("func value ", y_opt, " at ", x_opt, " iterations done ", iter_num_done)
    print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    print()

    print("Метод дихотомии-2")
    y_opt, x_opt, iter_num_done, final_segment = Code.dichotomy_two.dichotomy_method(target_function, epsilon,  accuracy, max_iter, a, b)
    print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    print()

    print("Метод золотого сечения")
    y_opt, x_opt, iter_num_done, final_segment = Code.golden_ratio.golden_ratio_method(target_function, epsilon, accuracy, max_iter, a, b, 1.68)
    print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    print()

    print("Метод Фибоначчи")
    y_opt, x_opt, iter_num_done, final_segment = Code.fibonacci.fibonacci_method(target_function, epsilon, accuracy, max_iter, a, b)
    print('func value is %f at x = %f, iterations done %d' % (y_opt, x_opt, iter_num_done))
    print()

    # построить график зависимости числа итераций от точности

    max_accuracy = 0.0000001
    min_accuracy = 0.0001
    step = max_accuracy * 25
    x_range = np.arange(max_accuracy, min_accuracy, step)
    epsilon = max_accuracy / 15
    dichotomy_one_iter_list = []
    dichotomy_two_iter_list = []
    golden_ratio_iter_list = []
    fibonacci_iter_list = []

    dichotomy_one_seg_list = []
    dichotomy_two_seg_list = []
    golden_ratio_seg_list = []
    fibonacci_seg_list = []

    for i in x_range:
        *first, tmp_1, tmp_2 = Code.dichotomy_one.dichotomy_method(target_function, epsilon, i, max_iter, a, b)
        dichotomy_one_iter_list.append(tmp_1)
        dichotomy_one_seg_list.append(tmp_2)
        *first, tmp_1, tmp_2 = Code.dichotomy_two.dichotomy_method(target_function, epsilon, i, max_iter, a, b)
        dichotomy_two_iter_list.append(tmp_1)
        dichotomy_two_seg_list.append(tmp_2)
        *first, tmp_1, tmp_2 = Code.golden_ratio.golden_ratio_method(target_function, epsilon, i, max_iter, a, b, 1.68)
        golden_ratio_iter_list.append(tmp_1)
        golden_ratio_seg_list.append(tmp_2)
        *first, tmp_1, tmp_2 = Code.fibonacci.fibonacci_method(target_function, epsilon, i, max_iter, a, b)
        fibonacci_iter_list.append(tmp_1)
        fibonacci_seg_list.append(tmp_2)
    # print(dichotomy_one_iter_list)
    # print(dichotomy_two_iter_list)
    # print(golden_ratio_iter_list)
    # print(fibonacci_iter_list)

    plt.figure(1)
    plt.plot(x_range, dichotomy_one_iter_list, label='Dichotomy-1')
    plt.plot(x_range, dichotomy_two_iter_list, label='Dichotomy-2')
    plt.plot(x_range, golden_ratio_iter_list, label='Golden Ratio')
    plt.plot(x_range, fibonacci_iter_list, label='Fibonacci')
    plt.grid(True)
    plt.xscale('log')
    plt.title('f  = ' + target_function)
    plt.xlabel('accuracy')
    plt.ylabel('iterations')
    plt.legend()

    plt.figure(2)
    plt.plot(x_range, dichotomy_one_seg_list, label='Dichotomy-1')
    plt.plot(x_range, dichotomy_two_seg_list, label='Dichotomy-2')
    plt.plot(x_range, golden_ratio_seg_list, label='Golden Ratio')
    plt.plot(x_range, fibonacci_seg_list, label='Fibonacci')
    plt.grid(True)
    plt.xscale('log')
    plt.yscale('log')
    plt.title('f  = ' + target_function)
    plt.xlabel('accuracy')
    plt.ylabel('final interval')
    plt.legend()

    plt.show()


if __name__ == '__main__':
    sys.exit(main())
