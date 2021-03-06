# -*- coding: utf-8 -*-
# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
#
# Sample Input 1:
# 4.5
#
# Sample Output 1:
# 7.25
#
# Sample Input 2:
# -4.5
#
# Sample Output 2:
# -5.25
#
# Sample Input 3:
# 1
#
# Sample Output 3:
# -0.5
def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif x > -2 and x <= 2:
        return -(x / 2)
    elif x > 2:
        return (x - 2) ** 2 + 1
